#!/bin/bash

header="{ stamp: 'now' }"
ros2 topic pub --once /servo_node/delta_joint_cmds control_msgs/JointJog \
  "{ header: ${header}, joint_names: ["first_joint"], velocities: [-1] }"  
