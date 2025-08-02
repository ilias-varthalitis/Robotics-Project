#!/usr/bin/env python3

#Ilias Varthalitis AM: 4637
#Aristeidis Panagiotou AM:4754

import rospy
from geometry_msgs.msg import Twist
import rosbag
from nav_msgs.msg import Odometry

def polynomial(my_list, t):
    return my_list[0] + 2 * my_list[1] * t + 3 * my_list[2] * t**2

def odom_callback(msg):
    bag.write('/odom', msg) 


rospy.init_node('robot_controller', anonymous=True)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10)  
rospy.sleep(1.0)   

rospy.Subscriber('/odometry/filtered', Odometry, odom_callback)

start_time = rospy.Time.now().to_sec()

bag_file = 'robot_trajectories2.bag'
with rosbag.Bag(bag_file, 'w') as bag:
    twist = Twist()
    array = [
        [0, 0.12683, -0.02818], 
        [0,0.00646,-0.00008],
        [0, 0.18333, -0.03055]
    ]

    # First movement
    while (rospy.Time.now().to_sec() - start_time) < 3:
        sec = rospy.Time.now().to_sec() - start_time
        twist.linear.x = 0
        twist.angular.z = polynomial(array[0], sec)
        pub.publish(twist)
        bag.write('/cmd_vel', twist)
        rate.sleep()

    # Second movement
    start_time = rospy.Time.now().to_sec()
    while (rospy.Time.now().to_sec() - start_time) < 50:
        sec = rospy.Time.now().to_sec() - start_time
        twist.linear.x = polynomial(array[1], sec)
        twist.angular.z = 0
        pub.publish(twist)
        bag.write('/cmd_vel', twist)
        rate.sleep()

    # Third movement
    start_time = rospy.Time.now().to_sec()
    while (rospy.Time.now().to_sec() - start_time) < 4:
        sec = rospy.Time.now().to_sec() - start_time
        twist.linear.x = 0
        twist.angular.z = polynomial(array[2], sec)
        pub.publish(twist)
        bag.write('/cmd_vel', twist)
        rate.sleep()
