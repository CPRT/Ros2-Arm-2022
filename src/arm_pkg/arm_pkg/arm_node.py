import rclpy
from rclpy.node import Node

from math import pi

import diagnostic_msgs.msg
from geometry_msgs.msg import Pose

from arm_interfaces.msg import LiveTune
from arm_interfaces.msg import SixFloats

from .roboclaw_driver import Roboclaw
from .PidController import PidController
from .ArmKinematics import inverseKinematics
from .GravityCompensation import gravityCompensation

from example_interfaces.msg import Int8

class ArmNode(Node):
    def __init__(self):
        super().__init__("arm_node")
        # self.get_logger().info("This node just says 'Hello'")

        self.ERRORS = {0x000000: (diagnostic_msgs.msg.DiagnosticStatus.OK, "Normal"),
                       0x000001: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "E-Stop"),
                       0x000002: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "Temperature1"),
                       0x000004: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "Temperature2"),
                       0x000008: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "Main Voltage High"),
                       0x000010: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "Logic Voltage High"),
                       0x000020: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "Logic Voltage Low"),
                       0x000040: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "M1 Driver Fault"),
                       0x000080: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "M2 Driver Fault"),
                       0x000100: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "M1 Speed"),
                       0x000200: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "M2 Speed"),
                       0x000400: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "M1 Position"),
                       0x000800: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "M2 Position"),
                       0x001000: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "M1 Current"),
                       0x002000: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "M2 Current"),
                       0x010000: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "M1 Over Current"),
                       0x020000: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "M2 Over Current"),
                       0x040000: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "Main Voltage High"),
                       0x080000: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "Main Voltage Low"),
                       0x100000: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "Temperature1"),
                       0x200000: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "Temperature2"),
                       0x400000: (diagnostic_msgs.msg.DiagnosticStatus.OK, "S4 Signal Triggered"),
                       0x800000: (diagnostic_msgs.msg.DiagnosticStatus.OK, "S5 Signal Triggered"),
                       0x01000000: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "Speed Error Limit"),
                       0x02000000: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "Position Error Limit")}

        ## 
        ## Defining stuff
        ##

        # Core variables to run this node
        self.loopCalculatePID = False
        self.isHoming = False
        self.enableVoltageMode = False
        self.HOME_SETPOINT_MOTORANGLES_RAD = self.declare_parameter("arm_home_rad").value
        
        self.setpointMotorAngles = self.HOME_SETPOINT_MOTORANGLES_RAD
        self.REACHED_SETPOINT_TOLERANCE_RAD = 0.05236
        self.massOnEndEffector = 0

       
        default_pids = [ 
            PidController(False, 0, 0, 0, 0, 0, 0, 12),
            PidController(False, 0, 0, 0, 0, 0, 0, 12),
            PidController(False, 0, 0, 0, 0, 0, 0, 12),
            PidController(False, 0, 0, 0, 0, 0, 0, 12),
            PidController(False, 0, 0, 0, 0, 0, 0, 12),
            PidController(False, 0, 0, 0, 0, 0, 0, 12),
           ]

         # Tunable constants of PID, should be live tunable
        self.pidControllers = self.declare_parameter("pidcontrollers", default_pids).value

        softLimitLow = self.declare_parameter("soft_limit_low", [0,0,0,0,0,0]).value
        softLimitHigh = self.declare_parameter("soft_limit_high", [0,0,0,0,0,0]).value

        i = 0
        for controller in self.pidControllers:
            controller[i].setSoftLimits(softLimitLow[i], softLimitHigh[i])
            i += 1

        self.gearReduction = self.declare_parameter("gear_reduction", [1,1,1,1,1,1]).value

        self.encoderTicksPerRotation = self.declare_parameter("encoder_ticks", [0,0,0,0,0,0]).value

        self.encoderOffset = self.declare_parameter("encoder_offset", [0,0,0,0,0,0]).value

        # Invert encoder direction (multiply by 1 or -1) based on boolean
        self.invertEncoderDirection = self.declare_parameter("invert_encoder", [False, False, False, False, False, False]).value
        for direction in self.invertEncoderDirection:
            # If invertDirection is true then multiply by -1
            if (direction):
                direction = -1
            else:
                direction = 1


        # Effects the influence of gravity comp on the arms, it's live tunable
        self.gravityCompNewtonMetersToVoltage = 0

        # self.timeSinceCommandRecieved = rospy.get_rostime()   #rospy.Time.now()

        self.get_logger().info("ArmNode: Connecting to roboclaws")

        dev_name = self.declare_parameter("~dev", "/dev/ttyACM0").value
        baud_rate = int(self.declare_parameter("~baud", "19200").value)

        self.addresses = self.declare_parameter("~addresses", [131,132,133]).value

        self.roboclaw = Roboclaw(dev_name, baud_rate)

        try:
            print("success=-------------------------")
            self.roboclaw.Open()
        except Exception as e:
            print("success=--==========================")
            self.get_logger().fatal("ArmNode: Could not connect to Roboclaw")
            self.get_logger().debug(e)
            rclpy.shutdown()


        versions = []
        for address in self.addresses:
            try:
                versions.append(self.roboclaw.ReadVersion(address))
            except Exception as e:
                self.get_logger().warn("ArmNode: Problem getting roboclaw version for " + f"[{address}]")
                self.get_logger().debug(e)
                pass

        for version in versions:
            if not version[0]:
                self.get_logger().warn("ArmNode: Problem getting roboclaw version for " + f"[{address}]")
            else:
                self.get_logger().debug("ArmCode: " + repr(version[1]))



        # Setup subscribers
        self.cmd_arm_state_subscriber = self.create_subscription(
            Int8, "cmd_arm_state", self.arm_state_callback, 10)

        self.cmd_arm_subscriber = self.create_subscription(
            Pose, "cmd_arm", self.cmd_arm_callback, 10)

        self.arm_setVoltage_subscriber = self.create_subscription(
            SixFloats, "arm_setVoltage", self.cmd_setVoltage_callback, 10)

        self.cmd_liveTune_subscriber = self.create_subscription(
            LiveTune, "arm_liveTune", self.callback_liveTune, 10)

        # Setup publishers
        self.angles_publisher = self.create_publisher(
            SixFloats, "armAngles", 10)

        self.encoder_raw_publisher = self.create_publisher(
            SixFloats, "armEncodersRaw", 10)

        # TODO: This needs forward kinematics equations which is lower priority
        # self.pose_publisher = self.create_publisher(
        #     PUTMSGHERE, "armPose", 10)

        # Setup timers
        self.mainLoopTimer = self.create_timer(
            self.declare_parameter("loop_execute_interval", 0.02).value, self.runMainLoop)


        # Give some info after roboclaw has initialized
        self.create_rate(1).sleep()

        self.get_logger().debug("ArmCode: dev %s" % dev_name)
        self.get_logger().debug("ArmCode: baud %d" % baud_rate)

        strAddress = []
        for address in self.addresses:
            strAddress += [str(address)]

        self.get_logger().debug("ArmCode: addresses %s" % str(",".join(strAddress)))


    # Subscriber to change the state of the arm. 
    # state should be an int
    # state == 0 -> Disable (emergency disable)
    # state == 1 -> Home then disable (safe disable)
    # state == 2 -> Enable
    # state == 3 -> Enable Voltage Control Only (disable kinematics+PID)
    def arm_state_callback(self, state: Int8):
        if (state.data == 0):
            self.stopMotors()
            self.loopCalculatePID = False
            self.isHoming = False

        elif (state.data == 1):
            self.loopCalculatePID = True
            self.isHoming = True
            self.setpointMotorAngles = self.HOME_SETPOINT_MOTORANGLES_RAD

        elif (state.data == 2):
            if (self.loopCalculatePID == False):
                self.setpointMotorAngles = self.HOME_SETPOINT_MOTORANGLES_RAD

            self.loopCalculatePID = True
            self.isHoming = False


    # Change the setpoint to a new value. The arm has to be enabled to go to this setpoint
    def cmd_arm_callback(self, pose: Pose):    
        if (self.isHoming == False):
            self.setpointMotorAngles = inverseKinematics(pose)

            # Ensure values calculated do not go beyond mechanical endstops
            i = 0
            for angle in self.setpointMotorAngles:
                lowLimit, highLimit = self.pidControllers[i].getSoftLimits()
                angle = self.clampValue(angle, lowLimit, highLimit)
                i += 1

    # Change the addiitonal mass that is on the End Effector
    def additionalMassOnEndEffector_callback(self, mass):
        self.massOnEndEffector = mass

    # This updates the heartbeat monitor so it knows it has received a command recently
    def feedMonitor(self):
        self.timeSinceCommandRecieved = 0 # TODO: Deal with the heartbeat monitor

    def runMainLoop(self):
        ##
        ## Check vitals. A basic 'motor controller is ok' check
        ##
        for address in self.addresses:

            # Get error reported from roboclaw and log it
            statusMessage = ""
            errorCode = 0x000000
            try:
                errorCode = self.roboclaw.ReadError(address)[1]
            except OSError as e:
                self.get_logger().warn("ArmNode: " + f"[{address}] Diagnostics OSError: {e.errno}")
                self.get_logger().debug("ArmNode: " + str(e))

            state, message = self.ERRORS[errorCode]
            # statusMessage.summary(state, f"[{address}] {message}")

            # Store info about the voltage input to the roboclaw and board temperature 1 and 2
            try:
                # MainBatteryVoltage/10 to get volts
                mainBatteryVoltage = float(self.roboclaw.ReadMainBatteryVoltage(address)[1] / 10)

                statusMessage.add("Main Batt V:", mainBatteryVoltage)
                statusMessage.add("Logic Batt V:", float(self.roboclaw.ReadLogicBatteryVoltage(address)[1] / 10))
                statusMessage.add("Temp1 C:", float(self.roboclaw.ReadTemp(address)[1] / 10))
                statusMessage.add("Temp2 C:", float(self.roboclaw.ReadTemp2(address)[1] / 10))
            except OSError as e:
                self.get_logger().warn("ArmNode: " + f"[{address}] Diagnostics OSError: {e.errno}")
                self.get_logger().debug("ArmNode: " + str(e))

            # TODO: Make statusMessage avaiable to read someher


        ##
        ## Measure encoders and publish data
        ##

        ## Measure encoders and publish
        encoderRadians = [0, 0, 0, 0, 0, 0]
        encoderRaw = [0, 0, 0, 0, 0, 0]

        i = 0
        for address in self.addresses:

            ##
            ## Store all encoder positions
            ##
            try:
                encoderCount1 = float(self.roboclaw.ReadEncM1(address)[1]) * self.invertEncoderDirection[i]
            except OSError as e:
                self.get_logger().warn("ArmNode: " + f"[{address}] ReadEncM1 OSError: {e.errno}")
                self.get_logger().debug("ArmNode: " + str(e))
            
            try:
                encoderCount2 = float(self.roboclaw.ReadEncM2(address)[1]) * self.invertEncoderDirection[i+1]
            except OSError as e:
                self.get_logger().warn("ArmNode: " + f"[{address}] ReadEncM2 OSError: {e.errno}")
                self.get_logger().debug("ArmNode: " + str(e))

            encoderRadians1 = encoderCount1 / self.encoderTicksPerRotation[i] * 2*pi / self.gearReduction[i]
            encoderRadians2 = encoderCount2 / self.encoderTicksPerRotation[i+1] * 2*pi / self.gearReduction[i+1]

            encoderRadians1 = encoderRadians1 + self.encoderOffset[i]
            encoderRadians2 = encoderRadians2 + self.encoderOffset[i+1]

            encoderRadians[i] = encoderRadians1
            encoderRadians[i+1] = encoderRadians2

            encoderRaw[i] = encoderCount1
            encoderRaw[i+1] = encoderCount2

            i += 2
        



        self.angles_publisher.publish(SixFloats(encoderRadians[0], encoderRadians[1], encoderRadians[2], encoderRadians[3], encoderRadians[4], encoderRadians[5]))
        self.encoder_raw_publisher.publish(SixFloats(encoderRaw[0], encoderRaw[1], encoderRaw[2], encoderRaw[3], encoderRaw[4], encoderRaw[5]))


        # TODO: Calculate forward kinematics and publish

        # self.pose_publisher.publish(...)


        ##
        ## If we are homing and reached home then disable
        ## 
        if (self.isHoming): 
            if (self.reachedSetpoint(self.HOME_SETPOINT_MOTORANGLES_RAD, encoderRadians)):
                self.arm_state_callback(0)
                return

        ##
        ## PID calculation
        ## If we don't want to calcualte PID then make sure the motors don't move
        ##
        if self.loopCalculatePID == False:
            self.stopMotors()

        else:

            ##
            ## Calculate PID + gravity compensation
            ## Convert voltage to duty cycle and send command to roboclaw
            ##

            # self.setpointMotorAngles from cmd_arm_callback(pose)
            motorAngles = self.setpointMotorAngles

            # Calculate gravity compensation
            gravityCompVolts = gravityCompensation(motorAngles, self.massOnEndEffector, self.gravityCompNewtonMetersToVoltage)
            
            for address in self.addresses:

                # Calculate grav comp and PID for motor 1
                setpoint1 = motorAngles[i]
                feedback1 = encoderRadians1
                voltage1 = self.pidControllers[i].calculate(setpoint1, feedback1, gravityCompVolts[i])

                # Calculate grav comp and PID for motor 2
                setpoint2 = motorAngles[i+1]
                feedback2 = encoderRadians2
                voltage2 = self.pidControllers[i+1].calculate(setpoint2, feedback2, gravityCompVolts[i+1])

                # 32767 is 100% duty cycle (15 bytes)
                dutyCycle1 = voltage1 / mainBatteryVoltage * 32767
                dutyCycle2 = voltage2 / mainBatteryVoltage * 32767

                # Send the command to the roboclaw
                try:
                    self.roboclaw.DutyM1M2(address, dutyCycle1, dutyCycle2)
                except OSError as e:
                    self.get_logger().warn("ArmNode: " + f"[{address}] DutyM1M2 OSError: {e.errno}")
                    self.get_logger().debug("ArmNode: " + e)

                # Feed so the heartbeat monitor knows it got a pulse 
                self.feedMonitor()

                # Iterate the loop
                i += 2

     

    def cmd_setVoltage_callback(self, volts: SixFloats): # CHANGE POSE
        voltages = [volts.m0, volts.m1, volts.m2, volts.m3, volts.m4, volts.m5]

        i = 0
        for address in self.addresses:

            try:
                # MainBatteryVoltage/10 to get volts
                mainBatteryVoltage = self.roboclaw.ReadMainBatteryVoltage(address)[1] / 10
            except OSError as e:
                self.get_logger().warn("ArmNode: " + f"[{address}] Diagnostics OSError: {e.errno}")
                self.get_logger().debug(e)

            # 32767 is 100% duty cycle (15 bytes)
            dutyCycle1 = voltages[i] / mainBatteryVoltage * 32767
            dutyCycle2 = voltages[i+1] / mainBatteryVoltage * 32767

            # Send the command to the roboclaw
            try:
                self.roboclaw.DutyM1M2(address, dutyCycle1, dutyCycle2)
            except OSError as e:
                self.get_logger().warn("ArmNode: " + f"[{address}] DutyM1M2 OSError: {e.errno}")
                self.get_logger().debug("ArmNode: " + e)

            # Feed so the heartbeat monitor knows it got a pulse 
            self.feedMonitor()

            i += 2


    def callback_liveTune(self, message: LiveTune):
        #P, I, D, IZone, InvertOutput, InvertEncoder, EncoderOffset -> for a specific motor (address and M1 or M2)
        """ LiveTune message
        
        int armMotorNumber   (0 to 5)
        string command
        float value

        Types of commands:

        "s" or "e" or ""   stops the motors from moving

        "p", "i", "d" or "iZ"    changes the values of the constants for PID + IZone
        
        "mI", "eI", "eO" or "eT"   sets the values for motorInvert, encoderInvert, encoderOffset and encoderTicksPerRotation     

        "sH", "sL"   sets the values for softLimits, high and low

        "gc"  sets gravity compensation constant

        "v" sets a voltage of a given motor

        "rad" sets a radian setpoint for the PID of a given motor
        """
        message.command = message.command.lower()

        if (message.command == "s" or message.command == "e" or message.command == ""):
            self.stopMotors

        elif (message.command == "p"):
            self.pidControllers[message.armMotorNumber].setP = message.value
        elif (message.command == "i"):
            self.pidControllers[message.armMotorNumber].setI = message.value
        elif (message.command == "d"):
            self.pidControllers[message.armMotorNumber].setD = message.value
        elif (message.command == "iZ"):
            self.pidControllers[message.armMotorNumber].setIZone = message.value

        elif (message.command == "mI"):
            self.pidControllers[message.armMotorNumber].setInvertOutput = message.value
        elif(message.command == "eI"):
            self.invertEncoderDirection[message.armMotorNumber] = int(message.value)
        elif(message.command == "eO"):
            self.encoderOffset[message.armMotorNumber] = message.value
        elif(message.command == "eT"):
            self.encoderTicksPerRotation[message.armMotorNumber] = message.value
        
        elif (message.command == "sH"):
            self.pidControllers[message.armMotorNumber].setSoftLimitHigh(message.value)
        elif (message.command == "sL"):
            self.pidControllers[message.armMotorNumber].setSoftLimitLow(message.value)

        elif(message.command == "gc"):
            self.gravityCompNewtonMetersToVoltage = message.value

        elif(message.command == "v"):
            voltages = [0] * 6
            voltages[message.armMotorNumber] = message.value
            # CONVERT VOLTAGE LIST TO 6 RAD VALUE ROS MSG
            self.cmd_setVoltage_callback(voltages)

        elif(message.command == "rad"):
            self.setpointMotorAngles = self.HOME_SETPOINT_MOTORANGLES_RAD

            lowLimit, highLimit = self.pidControllers[message.armMotorNumber].getSoftLimits()
            angle = self.clampValue(message.value, lowLimit, highLimit)

            self.setpointMotorAngles[message.armMotorNumber] = angle

    # This will stop the motors until the topic receives a new value
    def stopMotor(self, address):
        try:
            self.roboclaw.DutyM1M2(address, 0, 0)
        except OSError as e:
            self.get_logger().severe("ArmNode: OSError WHILE TRYING TO STOP MOTORS")
            self.get_logger().severe("ArmNode: " + f"[{address}] stopMotors DutyM1M2 OSError: {e.errno}")
            self.get_logger().debug(e)

    # Stops all motors until the topic receives a new value
    def stopMotors(self):
        for address in self.addresses:
            self.stopMotor(address)



    ##
    ## Helper methods
    ##

    # Clamp the voltage so it doesn't exceed a given max value
    def clampValue(self, value, minValue, maxValue):
        if (value > maxValue):
            return maxValue
        elif (value < minValue):
            return minValue

        return value

    # Check if each motor has reached its setpoint within a tolarable error
    def reachedSetpoint(self, setpoint, motorAngles):
        i = 0
        for angle in motorAngles:
            if (abs(setpoint[i] - motorAngles[i]) > self.REACHED_SETPOINT_TOLERANCE_RAD):
                return False
            i+=1

        return True

def main(args=None):
    rclpy.init(args=args)
    node = ArmNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()



"""

1. Figure out Heartbeat monitor or remove it
2. Launch file (PARAMETERS)
3. Stop motors when the error codes caught are bad
5. Change the timer's interval to something better and with a declare parameter

6. Make another node to run on my laptop and remote control the arm. (mainly to use LiveTune)



Many issues by try catches not creating varaibles that are then used
Check here for isinstance https://github.com/CPRT/h10_rover/blob/main/roboclaw_driver/roboclaw_driver/roboclaw_driver.py



"""