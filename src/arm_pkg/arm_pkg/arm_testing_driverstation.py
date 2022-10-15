from math import radians
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int8, Float32
from geometry_msgs.msg import Pose

from arm_interfaces.msg import LiveTune
from arm_interfaces.msg import SixFloats

class ArmTestingDriverstation(Node):


    def __init__(self):
        super().__init__("arm_testing_driverstation")

        # Setup fields
        self.commandStr = "No previous commands"
        self.prevCommandStr = ""
        self.repeatCommandStr = 0

        self.STOP_COMMANDS = ["s","q", "e", ""]
        self.LIVE_TUNE_COMMANDS = ["p", "i", "d", "iZ", "mI", "eI", "eO", "eT", "sH", "sL", "gc", "v", "rad", "deg"]
        self.SIX_FLOATS_COMMANDS = ["cmd", "volt", "v"]
        

        # Setup publishers
        self.liveTunePub = self.create_publisher(
            LiveTune, "arm_liveTune", 10)

        self.statePub = self.create_publisher(
            Int8, "cmd_arm_state", 10)

        self.cmdArmPub = self.create_publisher(
            SixFloats, "cmd_arm", 10)

        self.setVoltsPub = self.create_publisher(
            SixFloats, "arm_setVoltage", 10)

        self.create_timer(0.2, self.loopRun)

    def armAngles_callback(self, msg: SixFloats):
        self.angles = msg

    def armEncoderRaw_callback(self, msg: SixFloats):
        self.encoderRaw = msg

    def loopRun(self):
        if (self.prevCommandStr == self.commandStr):
            self.repeatCommandStr += 1
        else:
            self.repeatCommandStr = 0
            
        self.prevCommandStr = self.commandStr
            
        if (self.repeatCommandStr != 0):
            self.commandStr = self.commandStr.replace("\n", "") + "  " + str(self.repeatCommandStr)


        display = ( "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "----\n"
                    "Driverstation to run LiveTune to tune the arm\n"
                    "----\n\n"

                    "Input q to quit\n\n"

                    "Any of the following inputs will stop the motors:\n"
                    "e, '' or ' '  \n\n"

                    "The following commands will control the state of the arm\n"
                    "'enable'   will enable the robot in state 2\n"
                    "'disable'  will disable the robot exactly like using 'e' or '' or ' '\n"
                    "'Sdisable' or 's' or 'sd' will safe disable, going to the home setpoint then disabling\n\n"

                    "To set the pose of the arm in meters/radians (x,y,z,pitch,roll,yaw) or tag a 'deg' at the end to convert to radians:\n"
                    "cmd x y z pitch roll yaw \n"
                    "cmd 1.0 0.5 0.5 0 0 0  \n\n"
                    "cmd 1.0 0.5 0.5 50 0 0 deg \n\n"

                    "To set the voltages of every motor, use:\n"
                    "volt m0 m1 m2 m3 m4 m5 \n"
                    "v m0 m1 m2 m3 m4 m5 \n"
                    "v 0 0 3.0 0 2.0 0 \n\n"


                    "All LiveTune commands must be the motor number (0 to 6), a command, then a value, seperated by spaces\n"
                    "Examples:\n"
                    "motor command value\n"
                    "0 p 1.0\n\n"
                    
                    "Here is the list of all the LiveTune commands:\n\n"

                    '"e" or ""   stops the motors from moving\n\n'

                    '"p", "i", "d" or "iZ"    changes the values of the constants for PID + IZone\n\n'
                    
                    '"mI", "eI", "eO" or "eT"   sets the values for motorInvert, encoderInvert, encoderOffset and encoderTicksPerRotation     \n\n'

                    '"sH", "sL"   sets the values for softLimits, high and low\n\n'

                    '"gc"  sets gravity compensation constant\n\n'

                    '"v" sets a voltage of a given motor\n\n'

                    '"rad" sets a radian setpoint for the PID of a given motor\n\n'

                    '"deg" converts to radians and uses the "rad" command\n\n'

                    '\n\n'

                    "Your previous command:\n"
                    f"{self.commandStr}"

                    "\n\n\n\n"
        )
        
        u = input(display).lower()
        
        if (u == "q"):
            self.sendLiveTuneMsg(0, "s", 0.0)

            stateMsg = Int8()
            stateMsg.data = 0
            self.statePub.publish(stateMsg)

            rclpy.shutdown()

            return

        elif (u.replace(" ", "") == "" or u in self.STOP_COMMANDS):
            self.sendLiveTuneMsg(0, "s", 0.0)

            stateMsg = Int8()
            stateMsg.data = 0
            self.statePub.publish(stateMsg)
            
            self.commandStr = "suceeded -> arm emergency disabled\n"

            return

        elif (u == "enable"):
            self.sendStateMsg(2)
            self.commandStr = "suceeded -> arm enabled\n"
            return

        elif (u == "disable"):
            self.sendLiveTuneMsg(0, "s", 0.0)
            self.sendStateMsg(0)
            self.commandStr = "suceeded -> arm emergency disabled\n"
            return

        elif (u == "sdisable" or u == "s" or u == "sd"):
            self.sendStateMsg(1)
            self.commandStr = "suceeded -> arm safe disabled, going home\n"
            return

        # Split the operations by spaces
        u = u.split(" ")
        for element in u:
            if element == "":
                u.remove(" ")


        # Must be a SixFloats command
        if len(u) == 7 or len(u) == 8:
            if(not u[0] in self.SIX_FLOATS_COMMANDS):
                self.commandStr = "failed -> invalid command for a SixFloats msg\n"
                return
            
            sixFloatsMsg = SixFloats()
            motorFloats = []

            for i in range(1,6+1):
                try:
                    motorFloats += [float(u[i])]
                except Exception as e:
                    self.commandStr = f"failed -> SixFloats msg failed to convert motor {i-1}'s value to float  " + str(e)
                    return

            if len(u) == 8 and u[7] == "deg":
                
                motorFloats[3] = radians(motorFloats[3])
                motorFloats[4] = radians(motorFloats[4])
                motorFloats[5] = radians(motorFloats[5])

                self.commandStr = f"degs changed -> x: {motorFloats[0]:.3f}, y: {motorFloats[1]:.3f}, z: {motorFloats[2]:.3f}, pitch: {motorFloats[3]:.3f}, roll: {motorFloats[4]:.3f}, yaw: {motorFloats[5]:.3f}"
                
            sixFloatsMsg.m0 = motorFloats[0]
            sixFloatsMsg.m1 = motorFloats[1]
            sixFloatsMsg.m2 = motorFloats[2]
            sixFloatsMsg.m3 = motorFloats[3]
            sixFloatsMsg.m4 = motorFloats[4]
            sixFloatsMsg.m5 = motorFloats[5]

            if (u[0] == "cmd"):
                self.cmdArmPub.publish(sixFloatsMsg)
                self.commandStr = f"suceeded -> arm (radians) set to x: {motorFloats[0]:.3f}, y: {motorFloats[1]:.3f}, z: {motorFloats[2]:.3f}, pitch: {motorFloats[3]:.3f}, roll: {motorFloats[4]:.3f}, yaw: {motorFloats[5]:.3f}\n"
                return

            if (u[0] in ["volts", "v"]):
                self.setVoltsPub.publish(sixFloatsMsg)
                self.commandStr = f"suceeded -> arm volts set to m0: {motorFloats[0]:.3f}, m1: {motorFloats[1]:.3f}, m2: {motorFloats[2]:.3f}, m3: {motorFloats[3]:.3f}, m4: {motorFloats[4]:.3f}, m5: {motorFloats[5]:.3f}\n"
                return
                

        # Must be a LiveTune command:
        if (len(u) < 3):
            # Not a LiveTune Command
            self.commandStr = "failed -> invalid input\n"
            return

        if (not u[1] in self.LIVE_TUNE_COMMANDS):
            self.commandStr = "failed -> invalid command\n"
            return

        motorNum = -1
        try:
            motorNum = int(u[0])

        except Exception as e:
            self.commandStr = "failed -> motor number failed to convert to int for LiveTune\n"
            return

        floatValue = 0.0
        try:
            floatValue = float(u[2])
        except Exception as e:
            self.commandStr = "failed -> value failed to convert to float for LiveTune\n"
            return
        
        if (u[1] == "deg"):
            u[1] = "rad"
            floatValue = radians(floatValue)
        
        
        try:
            self.sendLiveTuneMsg(motorNum, u[1], floatValue)
            self.commandStr = f"suceeded -> msg sent: {motorNum} {u[1]} {floatValue:.5f}\n"

        except Exception as e:

            self.commandStr = "failed to send the msg\n" + str(e) + "\n"


    def sendLiveTuneMsg(self, motorNum:int, command:str, value:float):
        msg = LiveTune()
        msg.arm_motor_number = motorNum
        msg.command = command
        msg.value = value

        self.liveTunePub.publish(msg)
                
    def sendStateMsg(self, state:int):
        stateMsg = Int8()
        stateMsg.data = state
        self.statePub.publish(stateMsg)

def main(args=None):
    rclpy.init(args=args)
    node = ArmTestingDriverstation()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()