"""
A launch file for running the motion planning python api tutorial
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder(
            robot_name="zebra_zero", package_name="moveit_zebra_zero"
        )
        .moveit_cpp(
            file_path=get_package_share_directory("moveit_zebra_zero")
            + "/config/pipelines.yaml"
        )
        .to_moveit_configs()
    )

    script = DeclareLaunchArgument(
        "script",
        default_value="client.py",
        description="Python API script file",
    )

    moveit_py_node = Node(
        name="moveit_py",
        package="moveit_zebra_zero",
        executable=LaunchConfiguration("script"),
        output="both",
        parameters=[moveit_config.to_dict()],
    )

    return LaunchDescription(
        [
            script,
            moveit_py_node,
        ]
    )