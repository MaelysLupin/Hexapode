# Description

* Author: Maelys Lupin <maelyslupin6@gmail.com>

## Démarrage

Rviz:

    roslaunch rrbot_description rrbot_rviz.launch

Gazebo:

    roslaunch rrbot_gazebo rrbot_world.launch

ROS Control:

    roslaunch rrbot_control rrbot_control.launch

Example of Moving Joints:

    rostopic pub /rrbot/verin_joint1_position_controller/command std_msgs/Float64 "data: -0.3"

Get the values:

    rostopic echo rrbot/joint_states
    
### Automatisation

Start interface:

    rosrun rrbot_control mobile.py
or  rosrun rrbot_control fixe.py
    
    
#### Démarche complète 

roslaunch rrbot_gazebo rrbot_world.launch
roslaunch rrbot_control rrbot_control.launch
rosrun rrbot_control mobile.py



