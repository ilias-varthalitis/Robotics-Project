#!/usr/bin/env python3

#Ilias Varthalitis AM: 4637
#Aristeidis Panagiotou AM:4754

import rospy
from std_msgs.msg import Float64
import numpy as np

rospy.init_node('rrbot_control', anonymous=True)

joint1_pub = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
joint2_pub = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)

rate = rospy.Rate(10) 

for t in np.arange(0, 10, 0.1):
    if(t<=1):
        theta1 = 0.057205* (t**2)
        theta2 = -0.038785* (t**2)
    elif(t<=9):
        theta1 = 0.057205 + 0.11441*(t-1)
        theta2 = -0.038785 - 0.07757*(t-1)
    else:
        theta1 = 1.102974 - 0.057205*((10-t)**2)
        theta2 = -0.698132 + 0.038785*((10-t)**2)

    joint1_msg = Float64()
    joint2_msg = Float64()

    joint1_msg.data = theta1
    joint2_msg.data = theta2


    joint1_pub.publish(joint1_msg)
    joint2_pub.publish(joint2_msg)
    
    rate.sleep()

