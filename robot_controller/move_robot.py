#!/usr/bin/env python3


#Ilias Varthalitis AM: 4637
#Aristeidis Panagiotou AM:4754

import rospy
from geometry_msgs.msg import Twist
import rosbag
from nav_msgs.msg import Odometry

rospy.init_node('robot_controller', anonymous=True)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10)  

velocities = [
    {'linear': 0.0, 'angular': -15.0 * (3.14159265 / 180.0), 'duration': 10},  
    {'linear': 0.1, 'angular': 10.0 * (3.14159265 / 180.0), 'duration': 15}   
]


def odom_callback(msg):
    bag.write('/odom', msg) 

rospy.Subscriber('/odometry/filtered', Odometry, odom_callback)

bag_file = 'robot_trajectories1.bag'
with rosbag.Bag(bag_file, 'w') as bag:
    for vel in velocities:
        twist = Twist()
        twist.linear.x = vel['linear']
        twist.angular.z = vel['angular']

        start_time = rospy.Time.now()
        while (rospy.Time.now() - start_time).to_sec() < vel['duration']:
            pub.publish(twist)
            bag.write('/cmd_vel', twist)
            rate.sleep()

        twist.linear.x = 0.0
        twist.angular.z = 0.0
        pub.publish(twist)
        bag.write('/cmd_vel', twist)
        rospy.sleep(1)

