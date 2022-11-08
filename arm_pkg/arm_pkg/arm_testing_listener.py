from time import time
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int8, Float32
from geometry_msgs.msg import Pose

from arm_interfaces.msg import LiveTune
from arm_interfaces.msg import SixFloats

import time
import csv
from datetime import datetime

class ArmTestingListener(Node):


    def __init__(self):
        super().__init__("arm_testing_listener")

        # Setup fields
        self.angles = SixFloats()
        self.encoderRaw = SixFloats()

        self.loopInterval = 0.01
        self.timeSinceStartup = 0
        self.timeSinceNewData = 0

        self.startTime = time.time()

        csvFilePath = "/home/erik/Downloads/ArmNodeTesting-LoggingFiles_FAll2022/"
        csvFilename = "Logging_" + datetime.now().strftime("%d-%m-%Y_%H:%M:%S")

        try:
            self.csvFile = open(csvFilePath + csvFilename, 'w')
        except:
            print("FIled to file the folder: " + csvFilePath)
            try:
                print("Opening csv where this file is located")
                self.csvFile = open(csvFilename, 'w')
            except:
                exit


        self.csvWriter = csv.writer(self.csvFile)

        csvRow = (  f"TIME BLANK RAD m0 m1 m2 m3 m4 m5 BLANK RAW m0 m1 m2 m3 m4 m5").split()
        self.csvWriter.writerow(csvRow)
        

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
        measuredTime = time.time() - self.startTime
        timeDifference = measuredTime - self.timeSinceStartup

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
                    f"Time since listener startup: {self.timeSinceStartup:.3f} seconds \n"
                    f"Measured time: {measuredTime:.3f} \n"
                    f"Difference: {timeDifference:.3f} \n"

        )

        print(display)

        self.timeSinceStartup += self.loopInterval
        self.timeSinceNewData += self.loopInterval

        csvRow = [  measuredTime,
                    " ",
                    "RAD",
                    self.angles.m0,
                    self.angles.m1,
                    self.angles.m2,
                    self.angles.m3,
                    self.angles.m4,
                    self.angles.m5,
                    " ",
                    "RAW",
                    self.encoderRaw.m0,
                    self.encoderRaw.m1,
                    self.encoderRaw.m2,
                    self.encoderRaw.m3,
                    self.encoderRaw.m4,
                    self.encoderRaw.m5,]

        self.csvWriter.writerow(csvRow)


                

def main(args=None):
    rclpy.init(args=args)
    node = ArmTestingListener()
    rclpy.spin(node)

    # Close the csv
    node.csvFile.close()

    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()