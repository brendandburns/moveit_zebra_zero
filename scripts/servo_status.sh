#!/bin/bash

code=$(ros2 topic echo --once --field code --no-lost-messages /servo_node/status | head -n 1)


case "$code" in
    0)
      echo "No warning"
      ;;
    1)
      echo "Decelerate approaching singularity"
      ;;
    2)
      echo "Halt for singularity"
      ;;
    3)
      echo "Decelerate for leaving singularity"
      ;; 
    4)
      echo "Decelerate for collision"
      ;;
    5)
      echo "Hald for collision"
      ;;
    6)
      echo "Joint bound"
      ;;
    *)
      echo "Unknown code: $code"
      ;;
esac

ros2 topic echo --once /servo/pause_servo
