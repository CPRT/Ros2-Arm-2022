import launch

from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument

def generate_launch_description():

    return launch.LaunchDescription ([

        ##
        ## Note: Anywhere there is a list[6] is represents the six arm motors (m0,m1, ... , m5)
        ##

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
            default_value="/dev/serial0"),

        DeclareLaunchArgument(
            '~baud',
            description='Baud Rate',
            default_value="19200"),

        DeclareLaunchArgument(
            '~addresses',
            description='Roboclaw Serial Addresses',
            default_value="[128]"),


        ## All data needed to construct a PidController object
        DeclareLaunchArgument(
            "invert_motor",
            description="list[6] of booleans. True means the motor is going the wrong direction and should be inverted.",
            default_value= "[False,False,False,False,False,False]"
        ),

        DeclareLaunchArgument(
            "pid_kP",
            description="list[6] of floats. Represents the P constant of the PidController.",
            default_value= "[0.0, 0.0, 1.0, 0.0, 0.0, 0.0]"
        ),

        DeclareLaunchArgument(
            "pid_kI",
            description="list[6] of floats. Represents the I constant of the PidController.",
            default_value= "[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]"
        ),

        DeclareLaunchArgument(
            "pid_kD",
            description="list[6] of floats. Represents the D constant of the PidController.",
            default_value= "[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]"
        ),

        DeclareLaunchArgument(
            "pid_kF",
            description="list[6] of floats. Represents the F constant of the PidController.",
            default_value= "[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]"
        ),

        DeclareLaunchArgument(
            "pid_kIZone",
            description="list[6] of floats. Represents the IZone constant of the PidController.",
            default_value= "[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]"
        ),

        DeclareLaunchArgument(
            "max_output",
            description="list[6] of floats. Represents the max output of the motors, usually in volts.",
            default_value= "[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]"
        ),


        ## Other arm node information
        DeclareLaunchArgument(
            "home_rad",
            description="list[6] of floats. This is angle in radians that the arm will home to when safe disabled.",
            default_value="[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]"
        ),

        DeclareLaunchArgument(
            "soft_limit_low",
            description="list[6] of floats. This is angle in radians that the arm will not be allowed to be below.",
            default_value="[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]"   
        ),

        DeclareLaunchArgument(
            "soft_limit_high",
            description="list[6] of floats. This is angle in radians that the arm will not be allowed to be above.",
            default_value="[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]"
        ),

        DeclareLaunchArgument(
            "gear_reduction",
            description="list[6] of floats. This is the gear reduction between the arm axis and the encoder.",
            default_value="[1,1,1,1,1,1]"
        ),

        DeclareLaunchArgument(
            "encoder_ticks",
            description="list[6] of floats. This is the number of ticks per rotation of each encoder.",
            default_value="[1.0, 1.0, 1.0, 1.0, 1.0, 1.0]"
        ),
        
        DeclareLaunchArgument(
            "encoder_offset",
            description="list[6] of floats. This is the offset between the encoder zero and the math zero in radians.",
            default_value= "[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]"
        ),
    
        DeclareLaunchArgument(
            "invert_encoder",
            description="list[6] of booleans. True means the encoder is going the wrong direction and should be inverted.",
            default_value= "[False, False, False, False, False, False]"
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

                        "invert_motor": launch.substitutions.LaunchConfiguration("invert_motor"),
                        "pid_kP": launch.substitutions.LaunchConfiguration("pid_kP"),
                        "pid_kI": launch.substitutions.LaunchConfiguration("pid_kI"),
                        "pid_kD": launch.substitutions.LaunchConfiguration("pid_kD"),
                        "pid_kF": launch.substitutions.LaunchConfiguration("pid_kF"),
                        "pid_kIZone": launch.substitutions.LaunchConfiguration("pid_kIZone"),
                        "max_output": launch.substitutions.LaunchConfiguration("max_output"),
                        "encoder_ticks": launch.substitutions.LaunchConfiguration("encoder_ticks"),

                        "home_rad": launch.substitutions.LaunchConfiguration("home_rad"),
                        "soft_limit_low": launch.substitutions.LaunchConfiguration("soft_limit_low"),
                        "soft_limit_high": launch.substitutions.LaunchConfiguration("soft_limit_high"),
                        "gear_reduction": launch.substitutions.LaunchConfiguration("gear_reduction"),
                        "invert_encoder": launch.substitutions.LaunchConfiguration("invert_encoder"),                 
                    }
                ]
        ),
    ])