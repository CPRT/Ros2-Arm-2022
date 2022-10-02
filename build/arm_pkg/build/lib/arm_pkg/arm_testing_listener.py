import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int8, Float32
from geometry_msgs.msg import Pose

from arm_interfaces.msg import LiveTune
from arm_interfaces.msg import SixFloats

class ArmTestingListener(Node):


    def __init__(self):
        super().__init__("arm_testing_listener")

        # Setup fields
        self.angles = SixFloats()
        self.encoderRaw = SixFloats()

        self.loopInterval = 0.01
        self.timeSinceStartup = 0
        self.timeSinceNewData = 0

        # Setup subscribers
        self.encoder_radians = self.create_subscription(
            SixFloats, "arm_angles", self.armAngles_callback, 10)

        self.encoder_raw = self.create_subscription(
            SixFloats, "arm_encoder_raw", self.armEncoderRaw_callback, 10)

        self.create_timer(self.loopInterval, self.loopRun)


    def armAngles_callback(self, msg: SixFloats):
        self.angles = msg
        self.timeSinceNewData = 0

    def armEncoderRaw_callback(self, msg: SixFloats):
        self.encoderRaw = msg
        self.timeSinceNewData = 0

    def loopRun(self):
        display = ( "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "Encoder values in radians: \n"
                    f"m0: {self.angles.m0:.5f} \n"
                    f"m1: {self.angles.m1:.5f} \n"
                    f"m2: {self.angles.m2:.5f} \n"
                    f"m3: {self.angles.m3:.5f} \n"
                    f"m4: {self.angles.m4:.5f} \n"
                    f"m5: {self.angles.m5:.5f} \n\n\n"

                    "Encoder values raw (no offset and raw units from encoder but it is inverted if set True): \n"
                    f"m0: {self.encoderRaw.m0:.5f} \n"
                    f"m1: {self.encoderRaw.m1:.5f} \n"
                    f"m2: {self.encoderRaw.m2:.5f} \n"
                    f"m3: {self.encoderRaw.m3:.5f} \n"
                    f"m4: {self.encoderRaw.m4:.5f} \n"
                    f"m5: {self.encoderRaw.m5:.5f} \n\n\n"

                    f"Time since new data {self.timeSinceNewData:.3f} seconds \n"
                    f"Time since listener startup: {self.timeSinceStartup:.3f} seconds "
        )

        print(display)

        self.timeSinceStartup += self.loopInterval
        self.timeSinceNewData += self.loopInterval


                

def main(args=None):
    rclpy.init(args=args)
    node = ArmTestingListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()