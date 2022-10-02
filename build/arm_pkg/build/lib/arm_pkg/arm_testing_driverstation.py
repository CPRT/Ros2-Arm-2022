from math import radians
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int8, Float32
from geometry_msgs.msg import Pose

from arm_interfaces.msg import LiveTune
from arm_interfaces.msg import SixFloats

class ArmTestingDriverstation(Node):


    def __init__(self):
        super().__init__("arm_testing_driverstation")

        # Setup fields
        self.prevCommandStr = "No previous commands"
        
        self.STOP_COMMANDS = ["s","q", "e", ""]
        self.OTHER_COMMANDS = ["p", "i", "d", "iZ", "mI", "eI", "eO", "eT", "sH", "sL", "gc", "v", "rad", "deg"]

        # Setup publishers
        self.liveTunePub = self.create_publisher(
            LiveTune, "arm_liveTune", 10)

        self.statePub = self.create_publisher(
            Int8, "cmd_arm_state", 10)


        msg_test5 = LiveTune()
        msg_test5.arm_motor_number = 0
        msg_test5.command = "v"
        msg_test5.value = 0.0
        self.liveTunePub.publish(msg_test5)

        self.create_timer(0.2, self.loopRun)

    def armAngles_callback(self, msg: SixFloats):
        self.angles = msg

    def armEncoderRaw_callback(self, msg: SixFloats):
        self.encoderRaw = msg

    def loopRun(self):
        display = ( "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "----\n"
                    "Driverstation to run LiveTune to tune the arm\n"
                    "----\n\n"

                    "Input q to quit\n\n"

                    "Any of the following inputs will stop the motors:\n"
                    "s, e, '' or ' '  \n\n"

                    "All other commands must be the motor number (0 to 6), a command, then a value, seperated by spaces\n"
                    "Examples:\n"
                    "motor command value\n"
                    "0 p 1.0\n\n"
                    
                    
                    "Here is the list of all the commands:\n\n"

                    '"s" or "e" or ""   stops the motors from moving\n\n'

                    '"p", "i", "d" or "iZ"    changes the values of the constants for PID + IZone\n\n'
                    
                    '"mI", "eI", "eO" or "eT"   sets the values for motorInvert, encoderInvert, encoderOffset and encoderTicksPerRotation     \n\n'

                    '"sH", "sL"   sets the values for softLimits, high and low\n\n'

                    '"gc"  sets gravity compensation constant\n\n'

                    '"v" sets a voltage of a given motor\n\n'

                    '"rad" sets a radian setpoint for the PID of a given motor\n\n'

                    '"deg" converts to radians and uses the "rad" command\n\n'

                    '\n\n'

                    "Your previous command:\n"
                    f"{self.prevCommandStr}"

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
            
            self.prevCommandStr = "suceeded -> motors stopped\n"

            return


        u = u.split(" ")

        motorNum = -1
        try:
            motorNum = int(u[0])

        except Exception as e:
            self.prevCommandStr = "failed -> motor number failed to convert to int\n"
            return

        floatValue = 0.0
        try:
            floatValue = float(u[2])
        except Exception as e:
            self.prevCommandStr = "failed -> value failed to convert to float\n"
            return

        if (not u[1] in self.OTHER_COMMANDS):
            self.prevCommandStr = "failed -> invalid command\n"
            return

        if (u[1] == "deg"):
            u[1] = "rad"
            floatValue = radians(floatValue)
        
        try:
            self.sendLiveTuneMsg(motorNum, u[1], floatValue)
            self.prevCommandStr = f"suceeded -> msg sent: {motorNum} {u[1]} {floatValue:.5f}\n"

        except Exception as e:

            self.prevCommandStr = "failed to send the msg\n" + str(e) + "\n"


    def sendLiveTuneMsg(self, motorNum:int, command:str, value:float):
        msg = LiveTune()
        msg.arm_motor_number = motorNum
        msg.command = command
        msg.value = value

        self.liveTunePub.publish(msg)
                

def main(args=None):
    rclpy.init(args=args)
    node = ArmTestingDriverstation()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()