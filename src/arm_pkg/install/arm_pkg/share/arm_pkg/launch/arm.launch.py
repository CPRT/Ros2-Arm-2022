from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    arm_node = Node(
        package="arm_pkg",
        executable="arm_node",
    )

    ld.add_action(arm_node)

    return ld