from http.server import executable
import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():
    package_name='rover_description'

    pause_gz = LaunchConfiguration("pause_gz")
    pause_gz_cmd = DeclareLaunchArgument(
        "pause_gz",
        default_value="False",
        description="Whether to pause gazebo")

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','rsp.launch.py'
        )]),launch_arguments={'use_sim_time': 'true'}.items()
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'
        )]),
    )

    # gazebo_client_cmd = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         os.path.join('gazebo_ros', "launch", "gzclient.launch.py")
    #     ),
    # )

    # gazebo_server_cmd = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         os.path.join('gazebo_ros', "launch", "gzserver.launch.py")
    #     ),
    #     launch_arguments={"pause": pause_gz, }.items()
    #)

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description', '-entity', 'my_bot'],
                        output='screen')


    diff_drive_spawner = Node(
        package="controller_manager",
        executable = "spawner.py",
        arguments=["diff_cont"]
    )

    joint_broad_spawner = Node(
        package = "controller_manager",
        executable = "spawner.py",
        arguments = ["joint_broad"],
    )


    return LaunchDescription([rsp,gazebo,
                            spawn_entity, 
                            diff_drive_spawner, 
                            joint_broad_spawner])