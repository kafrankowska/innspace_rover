import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    pkg_path = get_package_share_directory("rover_simulation")

    gazebo_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_path, "launch", "gazebo.launch.py")
        ),
        launch_arguments={
            "world": os.path.join(pkg_path, "worlds", "maze.worlds"),
            "initial_pose_x": "-22",
            "initial_pose_y": "-5",
            "initial_pose_z": "0.3",
            "initial_pose_yaw": "0",
        }.items()
    )

    ld = LaunchDescription()
    ld.add_action(gazebo_cmd)

    return ld