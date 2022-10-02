import rclpy
from rclpy.node import Node

class ArmTestingDriverstationNode(Node):
    def __init__(self):
        super().__init__("arm_testing_driverstation")


        self.create_timer(0.1, loopRun)

def loopRun():
    print("test")

def main(args=None):
    rclpy.init(args=args)
    node = ArmTestingDriverstationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()