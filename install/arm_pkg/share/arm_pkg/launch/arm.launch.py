import launch

from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument

from arm_pkg.PidController import PidController

def generate_launch_description():

    return launch.LaunchDescription ([
        ## loop_execute_interval
        DeclareLaunchArgument(
            "loop_execute_interval",
            description="float. This is the interval at which the runMainLoop function will be called which"+
                            "updates encoder values, recalculated PID and gives a new speed to the roboclaws",
            default_value= "0.02"
        ),

        ## roboclaw information
        DeclareLaunchArgument(
            '~dev',
            description='Linux Serial Device',
            default_value="/dev/ttyACM0"),

        DeclareLaunchArgument(
            '~baud',
            description='Baud Rate',
            default_value=19200),

        DeclareLaunchArgument(
            '~addresses',
            description='Roboclaw Serial Addresses',
            default_value=[131,132,133]),

        ## Other arm node information
        DeclareLaunchArgument(
            "home_rad",
            description="list[6] of floats. This is angle in radians that the arm will home to when safe disabled.",
            default_value=[0,0,0,0,0,0]
        ),

        DeclareLaunchArgument(
            "pidcontrollers",
            description="list[6] of PidControllers. One PidController for each axis.",
            default_value= [ 
                PidController(False, 0, 0, 0, 0, 0, 0, 12),
                PidController(False, 0, 0, 0, 0, 0, 0, 12),
                PidController(False, 0, 0, 0, 0, 0, 0, 12),
                PidController(False, 0, 0, 0, 0, 0, 0, 12),
                PidController(False, 0, 0, 0, 0, 0, 0, 12),
                PidController(False, 0, 0, 0, 0, 0, 0, 12),]
        ),

        DeclareLaunchArgument(
            "soft_limit_low",
            description="list[6] of floats. This is angle in radians that the arm will not be allowed to be below.",
            default_value=[0,0,0,0,0,0]
        ),


        DeclareLaunchArgument(
            "soft_limit_high",
            description="list[6] of floats. This is angle in radians that the arm will not be allowed to be above.",
            default_value=[0,0,0,0,0,0]
        ),

        DeclareLaunchArgument(
            "gear_reduction",
            description="list[6] of floats. This is the gear reduction between the arm axis and the encoder.",
            default_value=[1,1,1,1,1,1]
        ),

        DeclareLaunchArgument(
            "gear_reduction",
            description="list[6] of floats. This is the gear reduction between the arm axis and the encoder.",
            default_value=[1,1,1,1,1,1]
        ),

        DeclareLaunchArgument(
            "encoder_ticks",
            description="list[6] of floats. This is the number of ticks per rotation of each encoder.",
            default_value=[0, 0, 0, 0, 0, 0]
        ),
        
        DeclareLaunchArgument(
            "encoder_offset",
            description="list[6] of floats. This is the offset between the encoder zero and the math zero in radians.",
            default_value= [0, 0, 0, 0, 0, 0]
        ),
    
        DeclareLaunchArgument(
            "invert_encoder",
            description="list[6] of booleans. True means the encoder is going the wrong direction and should be inverted.",
            default_value= [False, False, False, False, False, False]
        ),

        Node(
            package="arm_pkg",
            executable="arm_node",
                parameters=[
                    {
                        "loop_execute_interval": launch.substitutions.LaunchConfiguration("loop_execute_interval"), 

                        "~dev": launch.substitutions.LaunchConfiguration("~dev"),
                        "~baud": launch.substitutions.LaunchConfiguration("~baud"),
                        "~addresses": launch.substitutions.LaunchConfiguration("~addresses"),

                        "home_rad": launch.substitutions.LaunchConfiguration("home_rad"),
                        "pidcontrollers": launch.substitutions.LaunchConfiguration("pidcontrollers"),
                        "soft_limit_low": launch.substitutions.LaunchConfiguration("soft_limit_low"),
                        "soft_limit_high": launch.substitutions.LaunchConfiguration("soft_limit_high"),
                        "gear_reduction": launch.substitutions.LaunchConfiguration("gear_reduction"),
                        "invert_encoder": launch.substitutions.LaunchConfiguration("invert_encoder"),                 
                    }
                ]
        ),
    ])