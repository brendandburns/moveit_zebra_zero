#!/bin/bash

header="{ stamp: 'now', frame_id: 'world' }"
ros2 topic pub --once /servo_node/pose_target_cmds geometry_msgs/PoseStamped \
  "{ header: ${header}, pose: { position: {x: 0.0, y: 0.0, z: 0.7}, orientation: { x: 0.0, y: 0.0, z: 0.0, w: 1.0 } } }"  
