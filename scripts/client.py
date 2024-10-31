#!/usr/bin/env python3

import rclpy
from rclpy.logging import get_logger
from moveit import MoveItPy
import time
from geometry_msgs.msg import PoseStamped
import moveit.planning

def plan_and_execute(
    robot,
    planning_component,
    logger,
    single_plan_parameters=None,
    multi_plan_parameters=None,
    sleep_time=0.0,
):
    """Helper function to plan and execute a motion."""
    # plan to goal
    logger.info("Planning trajectory")
    if multi_plan_parameters is not None:
        plan_result = planning_component.plan(
            multi_plan_parameters=multi_plan_parameters
        )
    elif single_plan_parameters is not None:
        plan_result = planning_component.plan(
            single_plan_parameters=single_plan_parameters
        )
    else:
        plan_result = planning_component.plan(timeout=10.0)

    # execute the plan
    if plan_result:
        logger.info("Executing plan")
        robot_trajectory = plan_result.trajectory
        robot.execute(robot_trajectory, controllers=[])
    else:
        logger.error("Planning failed")

    time.sleep(sleep_time)


def main():
    rclpy.init()
    logger = get_logger("moveit_py.pose_goal")

    # instantiate MoveItPy instance and get planning component
    zebra = MoveItPy(node_name="moveit_py")
    zebra_arm = zebra.get_planning_component("arm")
    logger.info("MoveItPy instance created")

    # zebra_arm.set_start_state(configuration_name="home")
    # zebra_arm.set_goal_state(configuration_name="up")

    # plan_and_execute(zebra, zebra_arm, logger, sleep_time=3.0)

    # set plan start state to current state
    zebra_arm.set_start_state_to_current_state()

    zebra_state = zebra_arm.get_start_state().get_pose("sixth_link")

    logger.info("FOO: " + str(zebra_state.orientation))
    logger.info("FOO: " + str(zebra_state.position))
    # set pose goal with PoseStamped message
    
    pose_goal = PoseStamped()
    pose_goal.header.frame_id = "world"
    pose_goal.pose.orientation.y = 0.7
    pose_goal.pose.orientation.w = 0.7
    pose_goal.pose.position.x = 0.45
    pose_goal.pose.position.y = 0.0
    pose_goal.pose.position.z = 0.2
    zebra_arm.set_goal_state(pose_stamped_msg=pose_goal, pose_link="sixth_link")

    params = moveit.planning.PlanRequestParameters(zebra, "pilz_lin")
    params.planning_time = 10.0
    # plan to goal
    plan_and_execute(zebra, zebra_arm, logger, single_plan_parameters=params, sleep_time=3.0)

if __name__ == '__main__':
    main()

