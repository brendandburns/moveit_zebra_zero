#!/bin/bash

ros2 topic pub --once /servo_node/delta_twist_cmds geometry_msgs/TwistStamped "
header:
  stamp: now
  frame_id: sixth_link 
twist:
  linear:
    x: 0.0
    y: -0.3
    z: 0.0
  angular:
    x: 0.0
    y: 0.0
    z: 0.0"
