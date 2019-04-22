# ROS-Kinect
Modification of an existing Python driver for MS Kinect, in order to extract the positional data for the body joint positions/coordinates.

The main idea of this project is to use some sort of camera vision to constantly check for human presence in the robot’s work environment and recognize their position in space, so that the robot can avoid coming into contact and cause harm or injury. I modified an existing python driver for MS Kinect to extract the positional data for the joint positions and human ids, made it so that only the tracked joint coordinates are used, in order to avoid mistakes in the position of inferred joints that are hidden from the cameras sight. 

The coordinates are put in a hierarchy: first the coordinates of a single tracked joint are collected into a message called JointPosition, which is then nested into HumanJoints, a collection of all existing joint positions for a single body together with the body id. The Kinect sensor has the capability of tracking up to 6 bodies in its Field Of View, so to simplify the process of publishing the data, a third level is added which collects all the tracked bodies into a single message called KinectHumans, which is then published to a node, and can be used for further processing and manipulation depending on the intended use case. 

Link for the driver and API: https://github.com/Kinect
