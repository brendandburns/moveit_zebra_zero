from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_spawn_controllers_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("zebra_zero", package_name="moveit_zebra_zero").to_moveit_configs()
    return generate_spawn_controllers_launch(moveit_config)
