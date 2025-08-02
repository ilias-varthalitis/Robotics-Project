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

initial_angles = [0, 0]
final_angles = [np.deg2rad(25), np.deg2rad(-30)]

move_duration = 5
steps = int(move_duration * 10)  

for step in range(steps):
    current_angles = [
        initial_angles[0] + (final_angles[0] - initial_angles[0]) * (step / steps),
        initial_angles[1] + (final_angles[1] - initial_angles[1]) * (step / steps)
    ]
    
    joint1_pub.publish(Float64(current_angles[0]))
    joint2_pub.publish(Float64(current_angles[1]))

    rate.sleep()

