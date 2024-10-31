import launch
import launch_ros
from launch_param_builder import ParameterBuilder
from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_move_group_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("zebra_zero", package_name="moveit_zebra_zero").to_moveit_configs()
    
    servo_params = {
	"moveit_servo": ParameterBuilder("moveit_zebra_zero")
	.yaml("config/zebra_servo_config.yaml")
	.to_dict()
    }
    acceleration_filter_update_period = {"update_period": 0.01}
    planning_group_name = {"planning_group_name": "arm"}
    servo_node = launch_ros.actions.Node(
	package="moveit_servo",
	executable="servo_node",
	parameters =[
		servo_params,
		acceleration_filter_update_period,
                planning_group_name,
                moveit_config.robot_description,
		moveit_config.robot_description_semantic,
		moveit_config.robot_description_kinematics,
		moveit_config.joint_limits,
	],
	output="screen",
    ) 
    return launch.LaunchDescription(
	[
		servo_node
	]
    )
