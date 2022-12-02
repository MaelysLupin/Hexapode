#!/usr/bin/env python3

import rospy
import numpy as np
from std_msgs.msg import Float64
from sensor_msgs.msg import Imu
import tf.transformations

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def callback1(msg):
    print(tf_to_transform_matrix(msg.orientation))

def tf_to_transform_matrix(tf_msg):
    
    # Make the quaternion a numpy array
    q = np.array([tf_msg.x,
                tf_msg.y,
                tf_msg.z,
                tf_msg.w])
    
    # Form the transform matrix from the translation and the quaternion
    angle = tf.transformations.euler_from_quaternion(q)
    
    return angle

if __name__ == '__main__':
    rospy.init_node('zero', anonymous=True)
    pub1 = rospy.Publisher('rrbot/verin_joint1_position_controller/command', Float64, queue_size=1)
    pub2 = rospy.Publisher('rrbot/verin_joint2_position_controller/command', Float64, queue_size=1)
    pub3 = rospy.Publisher('rrbot/verin_joint3_position_controller/command', Float64, queue_size=1)
    pub4 = rospy.Publisher('rrbot/verin_joint4_position_controller/command', Float64, queue_size=1)
    pub5 = rospy.Publisher('rrbot/verin_joint5_position_controller/command', Float64, queue_size=1)
    pub6 = rospy.Publisher('rrbot/verin_joint6_position_controller/command', Float64, queue_size=1)
    sub1 = rospy.Subscriber('imu', Imu, callback1, queue_size=1)
    rate = rospy.Rate(3)


    while not rospy.is_shutdown():
        pub1.publish(-0.295225)
        pub2.publish(-0.2446879)
        pub3.publish(-0.2446879)
        pub4.publish(-0.295225)
        pub5.publish(-0.519522)
        pub6.publish(-0.519522)


        rate.sleep()



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# if __name__ == '__main__':
#     rospy.init_node('talker', anonymous=True)
#     pub1 = rospy.Publisher('rrbot/verin_joint1_position_controller/command', Float64, queue_size=1)
#     pub2 = rospy.Publisher('rrbot/verin_joint2_position_controller/command', Float64, queue_size=1)
#     pub3 = rospy.Publisher('rrbot/verin_joint3_position_controller/command', Float64, queue_size=1)
#     pub4 = rospy.Publisher('rrbot/verin_joint4_position_controller/command', Float64, queue_size=1)
#     pub5 = rospy.Publisher('rrbot/verin_joint5_position_controller/command', Float64, queue_size=1)
#     pub6 = rospy.Publisher('rrbot/verin_joint6_position_controller/command', Float64, queue_size=1)
#     rate = rospy.Rate(40) # 10hz


#     x1=-0.1
#     x2=-0.2
#     x3=-0.3
#     x4=-0.4
#     x5=-0.5
#     x6=-0.6

#     y1=0
#     y2=8
#     y3=16
#     y4=24
#     y5=32
#     y6=40

#     z1=z2=z3=z4=z5=z6=0


#     while not rospy.is_shutdown():

#         pub1.publish(x1)
#         if y1<=39:
#             x1-=0.0125
#         else :
#             x1+=0.0125
#             z1+=1
#         y1+=1
#         if z1==40:
#             y1=0
#             z1=0

#         pub2.publish(x2)
#         if y2<=39:
#             x2-=0.0125
#         else :
#             x2+=0.0125
#             z2+=1
#         y2+=1
#         if z2==40:
#             y2=0
#             z2=0

#         pub3.publish(x3)
#         if y3<=39:
#             x3-=0.0125
#         else :
#             x3+=0.0125
#             z3+=1
#         y3+=1
#         if z3==40:
#             y3=0
#             z3=0

#         pub4.publish(x4)
#         if y4<=39:
#             x4-=0.0125
#         else :
#             x4+=0.0125
#             z4+=1
#         y4+=1
#         if z4==40:
#             y4=0
#             z4=0

#         pub5.publish(x5)
#         if y5<=39:
#             x5-=0.0125
#         else :
#             x5+=0.0125
#             z5+=1
#         y5+=1
#         if z5==40:
#             y5=0
#             z5=0

#         pub6.publish(x6)
#         if y6<=39:
#             x6-=0.0125
#         else :
#             x6+=0.0125
#             z6+=1
#         y6+=1
#         if z6==40:
#             y6=0
#             z6=0

#         rate.sleep()