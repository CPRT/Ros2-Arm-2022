from distutils.log import error
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

from std_msgs.msg import Int8, Float32

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
        self.HOME_SETPOINT_MOTORANGLES_RAD = self.declare_parameter("home_rad", [0.0,0.0,0.0,0.0,0.0,0.0]).value
        
        self.setpointMotorAngles = self.HOME_SETPOINT_MOTORANGLES_RAD
        self.REACHED_SETPOINT_TOLERANCE_RAD = 0.05236
        self.massOnEndEffector = 0

        # Tunable constants of PID
        invert_motor = self.declare_parameter("invert_motor", [False, False, False, False, False, False]).value
        pid_kP = self.declare_parameter("pid_kP", [0.0,0.0,0.0,0.0,0.0,0.0]).value
        pid_kI = self.declare_parameter("pid_kI", [0.0,0.0,0.0,0.0,0.0,0.0]).value
        pid_kD = self.declare_parameter("pid_kD", [0.0,0.0,0.0,0.0,0.0,0.0]).value
        pid_kF = self.declare_parameter("pid_kF", [0.0,0.0,0.0,0.0,0.0,0.0]).value
        pid_kIZone = self.declare_parameter("pid_kIZone", [0.0,0.0,0.0,0.0,0.0,0.0]).value
        max_output = self.declare_parameter("max_output", [0.0,0.0,0.0,0.0,0.0,0.0]).value

        self.get_logger().info("kP: " + str(pid_kP))

        self.pidControllers = []
        for i in range(0,5+1):
            self.pidControllers.append(PidController(invert_motor[i], pid_kP[i], pid_kI[i], pid_kD[i], pid_kF[i], pid_kIZone[i], max_output[i]))     

        softLimitLow = self.declare_parameter("soft_limit_low", [0.0,0.0,0.0,0.0,0.0,0.0]).value
        softLimitHigh = self.declare_parameter("soft_limit_high", [0.0,0.0,0.0,0.0,0.0,0.0]).value

        for i in range(0,5+1):
            self.pidControllers[i].setSoftLimits(softLimitLow[i], softLimitHigh[i])

        self.gearReduction = self.declare_parameter("gear_reduction", [1,1,1,1,1,1]).value

        self.encoderTicksPerRotation = self.declare_parameter("encoder_ticks", [0.0,0.0,0.0,0.0,0.0,0.0]).value
        self.get_logger().info("Ticks per rotation: " + str(self.encoderTicksPerRotation))

        self.encoderOffset = self.declare_parameter("encoder_offset", [0.0,0.0,0.0,0.0,0.0,0.0]).value

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

        self.get_logger().info("Connecting to roboclaws")

        dev_name = self.declare_parameter("~dev", "/dev/ttyACM0").value
        baud_rate = self.declare_parameter("~baud", 19200).value

        self.addresses = self.declare_parameter("~addresses", [131,132,133]).value

        self.roboclaw = Roboclaw(dev_name, baud_rate)


        try:
            
            errorCode = self.roboclaw.Open()
            self.get_logger().info("Connected to roboclaws")

        except Exception as e:

            self.get_logger().fatal("Could not connect to Roboclaw")
            self.get_logger().debug(e)
            rclpy.shutdown()

        if (errorCode == 0):
            self.get_logger().fatal("Could not connect to Roboclaw")
            rclpy.shutdown()

        versions = []
        for address in self.addresses:
            try:
                versions.append(self.roboclaw.ReadVersion(address))
            except Exception as e:
                self.get_logger().warn("Problem getting roboclaw version for " + f"[{address}]")
                self.get_logger().debug(e)
                pass

        for version in versions:
            if not version[0]:
                self.get_logger().warn("Problem getting roboclaw version for " + f"[{address}]")
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
            SixFloats, "arm_angles", 10)

        self.encoder_raw_publisher = self.create_publisher(
            SixFloats, "arm_encoder_raw", 10)

        # TODO: This needs forward kinematics equations but that's lower priority
        # self.pose_publisher = self.create_publisher(
        #     PUTMSGHERE, "arm_pose", 10)

        # Setup timers
        self.mainLoopTimer = self.create_timer(
            self.declare_parameter("loop_execute_interval", 0.02).value, self.runMainLoop)

       
        # self.create_rate(1).sleep()  # This sleep thing caused problems

        # Give some info after roboclaw has initialized
        self.get_logger().debug("ArmCode: dev %s" % dev_name)
        self.get_logger().debug("ArmCode: baud %d" % baud_rate)

        strAddress = []
        for address in self.addresses:
            strAddress += [str(address)]

        self.get_logger().debug("ArmCode: addresses %s" % str(",".join(strAddress)))


        # msg_test = Pose()
        # msg_test.position.x = 0.3
        # msg_test.position.y = 0.0
        # msg_test.position.z = 0.0
        # msg_test.orientation.x = 0.0
        # msg_test.orientation.y = 0.0
        # msg_test.orientation.z = 0.0
        # msg_test.orientation.w = 0.0
        # self.cmd_arm_callback(msg_test)

        # msg_test2 = Int8()
        # msg_test2.data = 0
        # self.arm_state_callback(msg_test2)

        # msg_test3 = Float32()
        # msg_test3.data = 0.01
        # self.additionalMassOnEndEffector_callback(msg_test3)

        # msg_test4 = SixFloats()
        # msg_test4.m0 = 0.0
        # msg_test4.m1 = 0.0
        # msg_test4.m2 = 0.0
        # msg_test4.m3 = 0.0
        # msg_test4.m4 = 0.0
        # msg_test4.m5 = 0.0
        # self.cmd_setVoltage_callback(msg_test4)

        # msg_test5 = LiveTune()
        # msg_test5.arm_motor_number = 0
        # msg_test5.command = "v"
        # msg_test5.value = 0.0
        # self.callback_liveTune(msg_test5)

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
    def additionalMassOnEndEffector_callback(self, mass: Float32):
        self.massOnEndEffector = mass.data

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
                state, message = self.ERRORS[errorCode]
                self.get_logger().info(f"State {state}, Message: {message}")
            except OSError as e:
                self.get_logger().warn("" + f"[{address}] roboclaw.ReadError OSError: {e.errno}")
                self.get_logger().debug("" + str(e))


            # statusMessage.summary(state, f"[{address}] {message}")

            # Store info about the voltage input to the roboclaw and board temperature 1 and 2
            try:
                # MainBatteryVoltage/10 to get volts
                mainBatteryVoltage = float(self.roboclaw.ReadMainBatteryVoltage(address)[1] / 10) # EDGECASE: mainBatteryVoltage None

                # statusMessage.add("Main Batt V:", mainBatteryVoltage)
                # statusMessage.add("Logic Batt V:", float(self.roboclaw.ReadLogicBatteryVoltage(address)[1] / 10))
                # statusMessage.add("Temp1 C:", float(self.roboclaw.ReadTemp(address)[1] / 10))
                # statusMessage.add("Temp2 C:", float(self.roboclaw.ReadTemp2(address)[1] / 10))
            except OSError as e:
                self.get_logger().warn("" + f"[{address}] roboclaw.ReadMainBatteryVoltage OSError: {e.errno}")
                self.get_logger().debug("" + str(e))

            # TODO: Make statusMessage avaiable to read somewhere


        ##
        ## Measure encoders and publish data
        ##

        ## Measure encoders and publish
        encoderRadians = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        encoderRaw = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        i = 0
        for address in self.addresses:
            ##
            ## Store all encoder positions
            ##
            try:
                encoderCount1 = float(self.roboclaw.ReadEncM1(address)[1]) * self.invertEncoderDirection[i]
            except OSError as e:
                self.get_logger().warn("" + f"[{address}] ReadEncM1 OSError: {e.errno}") # EDGECASE: encoderCount1 None
                self.get_logger().debug("" + str(e))
                # self.stopMotors() # TODO: Add this back once we have encoders working
                return # EDGECASE_HANDLED_TEMP
            
            try:
                encoderCount2 = float(self.roboclaw.ReadEncM2(address)[1]) * self.invertEncoderDirection[i+1]
            except OSError as e:
                self.get_logger().warn("" + f"[{address}] ReadEncM2 OSError: {e.errno}") # EDGECASE: encoderCount2 None
                self.get_logger().debug("" + str(e))
                # self.stopMotors() # TODO: Add this back once we have encoders working
                return # EDGECASE_HANDLED_TEMP

            encoderRadians1 = encoderCount1 / self.encoderTicksPerRotation[i] * 2*pi / self.gearReduction[i]
            encoderRadians2 = encoderCount2 / self.encoderTicksPerRotation[i+1] * 2*pi / self.gearReduction[i+1]

            encoderRadians1 = encoderRadians1 + self.encoderOffset[i]
            encoderRadians2 = encoderRadians2 + self.encoderOffset[i+1]

            encoderRadians[i] = encoderRadians1
            encoderRadians[i+1] = encoderRadians2

            encoderRaw[i] = encoderCount1
            encoderRaw[i+1] = encoderCount2

            i += 2
        
        encoderRadiansMsg = SixFloats()
        encoderRadiansMsg.m0 = encoderRadians[0]
        encoderRadiansMsg.m1 = encoderRadians[1]
        encoderRadiansMsg.m2 = encoderRadians[2]
        encoderRadiansMsg.m3 = encoderRadians[3]
        encoderRadiansMsg.m4 = encoderRadians[4]
        encoderRadiansMsg.m5 = encoderRadians[5]

        encoderRawMsg = SixFloats()
        encoderRawMsg.m0 = encoderRaw[0]
        encoderRawMsg.m1 = encoderRaw[1]
        encoderRawMsg.m2 = encoderRaw[2]
        encoderRawMsg.m3 = encoderRaw[3]
        encoderRawMsg.m4 = encoderRaw[4]
        encoderRawMsg.m5 = encoderRaw[5]

        self.angles_publisher.publish(encoderRadiansMsg)
        self.encoder_raw_publisher.publish(encoderRawMsg)


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
            pass
            # self.stopMotors() # TODO: Add this back once we have encoders working

        else:

            ##
            ## Calculate PID + gravity compensation
            ## Convert voltage to duty cycle and send command to roboclaw
            ##

            # self.setpointMotorAngles from cmd_arm_callback(pose)
            motorAngles = self.setpointMotorAngles

            # Calculate gravity compensation
            gravityCompVolts = gravityCompensation(motorAngles, self.massOnEndEffector, self.gravityCompNewtonMetersToVoltage)
            
            i = 0
            for address in self.addresses:

                # Calculate grav comp and PID for motor 1
                setpoint1 = motorAngles[i]
                feedback1 = encoderRadians1 #EDGECASE: encoderRadians1 is None
                voltage1 = self.pidControllers[i].calculate(setpoint1, feedback1, gravityCompVolts[i])

                # Calculate grav comp and PID for motor 2
                setpoint2 = motorAngles[i+1]
                feedback2 = encoderRadians2 #EDGECASE: encoderRadians2 is None
                voltage2 = self.pidControllers[i+1].calculate(setpoint2, feedback2, gravityCompVolts[i+1])

                # 32767 is 100% duty cycle (15 bytes)
                dutyCycle1 = int(voltage1 / mainBatteryVoltage * 32767) #EDGECASE: mainBatteryVoltage is None
                dutyCycle2 = int(voltage2 / mainBatteryVoltage * 32767) #EDGECASE: mainBatteryVoltage is None

                # Send the command to the roboclaw
                try:
                    self.roboclaw.DutyM1M2(address, dutyCycle1, dutyCycle2)

                    # Feed so the heartbeat monitor knows it got a pulse 
                    self.feedMonitor()
                except OSError as e:
                    self.get_logger().warn("" + f"[{address}] DutyM1M2 OSError: {e.errno}")
                    self.get_logger().debug("" + str(e))


                # Iterate the loop
                i += 2

     

    def cmd_setVoltage_callback(self, volts: SixFloats): # CHANGE POSE
        voltages = [volts.m0, volts.m1, volts.m2, volts.m3, volts.m4, volts.m5]

        i = 0
        for address in self.addresses:

            try:
                # MainBatteryVoltage/10 to get volts
                mainBatteryVoltage = self.roboclaw.ReadMainBatteryVoltage(address)[1] / 10 # EDGECASE: mainBatteryVoltage
            except OSError as e:
                self.get_logger().warn("" + f"[{address}] roboclaw.ReadMainBatteryVoltage OSError: {e.errno}")
                self.get_logger().debug(str(e))
                return # EDGECASE_HANDLED_TEMP

            # 32767 is 100% duty cycle (15 bytes)
            dutyCycle1 = int(voltages[i] / mainBatteryVoltage * 32767)
            dutyCycle2 = int(voltages[i+1] / mainBatteryVoltage * 32767)

            # Send the command to the roboclaw
            try:
                self.roboclaw.DutyM1M2(address, dutyCycle1, dutyCycle2)
            except OSError as e:
                self.get_logger().warn("" + f"[{address}] DutyM1M2 OSError: {e.errno}")
                self.get_logger().debug("" + str(e))

            # Feed so the heartbeat monitor knows it got a pulse 
            self.feedMonitor()

            i += 2


    def callback_liveTune(self, message: LiveTune):
        #P, I, D, IZone, InvertOutput, InvertEncoder, EncoderOffset -> for a specific motor (address and M1 or M2)
        """ LiveTune message
        
        int arm_motor_number   (0 to 5)
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
            self.stopMotors()

        elif (message.command == "p"):
            self.pidControllers[message.arm_motor_number].setP = message.value
        elif (message.command == "i"):
            self.pidControllers[message.arm_motor_number].setI = message.value
        elif (message.command == "d"):
            self.pidControllers[message.arm_motor_number].setD = message.value
        elif (message.command == "iZ"):
            self.pidControllers[message.arm_motor_number].setIZone = message.value

        elif (message.command == "mI"):
            self.pidControllers[message.arm_motor_number].setInvertOutput = message.value
        elif(message.command == "eI"):
            self.invertEncoderDirection[message.arm_motor_number] = int(message.value)
        elif(message.command == "eO"):
            self.encoderOffset[message.arm_motor_number] = message.value
        elif(message.command == "eT"):
            self.encoderTicksPerRotation[message.arm_motor_number] = message.value
        
        elif (message.command == "sH"):
            self.pidControllers[message.arm_motor_number].setSoftLimitHigh(message.value)
        elif (message.command == "sL"):
            self.pidControllers[message.arm_motor_number].setSoftLimitLow(message.value)

        elif(message.command == "gc"):
            self.gravityCompNewtonMetersToVoltage = message.value

        elif(message.command == "v"):
            voltages = [0.0] * 6
            voltages[message.arm_motor_number] = message.value

            voltages_msg = SixFloats()
            voltages_msg.m0 = voltages[0]
            voltages_msg.m1 = voltages[1]
            voltages_msg.m2 = voltages[2]
            voltages_msg.m3 = voltages[3]
            voltages_msg.m4 = voltages[4]
            voltages_msg.m5 = voltages[5]

            # CONVERT VOLTAGE LIST TO 6 RAD VALUE ROS MSG
            self.cmd_setVoltage_callback(voltages_msg)

        elif(message.command == "rad"):
            self.setpointMotorAngles = self.HOME_SETPOINT_MOTORANGLES_RAD

            lowLimit, highLimit = self.pidControllers[message.arm_motor_number].getSoftLimits()
            angle = self.clampValue(message.value, lowLimit, highLimit)

            self.setpointMotorAngles[message.arm_motor_number] = angle

    # This will stop the motors until the topic receives a new value
    def stopMotor(self, address):
        self.get_logger().warn("STOPPING MOTORS")
        try:
            self.roboclaw.DutyM1M2(address, 0, 0)
        except OSError as e:
            self.get_logger().fatal("OSError WHILE TRYING TO STOP MOTORS\n " +
                             f"[{address}] stopMotors DutyM1M2 OSError: {e.errno}")
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

# EDGECASE: A setpoint at [0,0,0,0,0,0] causes the kinematics math to fail 

"""


Make another node to run on my laptop and remote control the arm. (mainly to use LiveTune)

Many issues by try catches not creating varaibles that are then used
Check here for isinstance https://github.com/CPRT/h10_rover/blob/main/roboclaw_driver/roboclaw_driver/roboclaw_driver.py



"""