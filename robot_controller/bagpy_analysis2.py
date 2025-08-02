#Ilias Varthalitis AM: 4637
#Aristeidis Panagiotou AM:4754

import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt
from tf.transformations import euler_from_quaternion


def quaternion_to_yaw(x, y, z, w):
    euler = euler_from_quaternion([x, y, z, w])
    return euler[2]  

b = bagreader('robot_trajectories2.bag')

vel_data = b.message_by_topic('/cmd_vel')
odom_data = b.message_by_topic('/odom')
veldf = pd.read_csv(vel_data)
odomdf = pd.read_csv(odom_data)

veldf['Time'] = veldf['Time'] - veldf['Time'].min()
odomdf['Time'] = odomdf['Time'] - odomdf['Time'].min()

odomdf['yaw'] = odomdf.apply(lambda row: quaternion_to_yaw(row['pose.pose.orientation.x'],row['pose.pose.orientation.y'],row['pose.pose.orientation.z'],row['pose.pose.orientation.w']), axis=1)

# First movement 
start_time = 0
end_time = 3
cmd_vel_movement = veldf[(veldf['Time'] >= start_time) & (veldf['Time'] <= end_time)]
odom_movement = odomdf[(odomdf['Time'] >= start_time) & (odomdf['Time'] <= end_time)]

if not cmd_vel_movement.empty and not odom_movement.empty:
    plt.figure(figsize=(14, 7))

    plt.subplot(2, 1, 1)
    plt.plot(cmd_vel_movement['Time'].to_numpy(), cmd_vel_movement['angular.z'].to_numpy(), label='Angular Z Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Angular Velocity (rad/s)')
    plt.legend()
    plt.title('First Movement: Angular Velocity')

    plt.subplot(2, 1, 2)
    plt.plot(odom_movement['Time'].to_numpy(), odom_movement['yaw'].to_numpy(), label='Yaw')
    plt.xlabel('Time (s)')
    plt.ylabel('Yaw (rad)')
    plt.legend()
    plt.title('First Movement: Angle')

    plt.tight_layout()
    plt.show()
else:
    print("No data found for the first movement in the range 0 to 1.8")

# Second movement 
start_time = 3
end_time = 53
cmd_vel_movement = veldf[(veldf['Time'] >= start_time) & (veldf['Time'] <= end_time)]
odom_movement = odomdf[(odomdf['Time'] >= start_time) & (odomdf['Time'] <= end_time)]

if not cmd_vel_movement.empty and not odom_movement.empty:
    plt.figure(figsize=(14, 7))

    plt.subplot(2, 1, 1)
    plt.plot(cmd_vel_movement['Time'].to_numpy(), cmd_vel_movement['linear.x'].to_numpy(), label='Linear X Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Linear Velocity (m/s)')
    plt.legend()
    plt.title('Second Movement: Linear Velocity')

    plt.subplot(2, 1, 2)
    plt.plot(odom_movement['Time'].to_numpy(), odom_movement['pose.pose.position.x'].to_numpy(), label='Position X')
    plt.plot(odom_movement['Time'].to_numpy(), odom_movement['pose.pose.position.y'].to_numpy(), label='Position Y')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.legend()
    plt.title('Second Movement: Position')

    plt.tight_layout()
    plt.show()
else:
    print("No data found for the second movement in the range 1.8 to 33.8")

# Third movement 
start_time = 53
end_time = 58
cmd_vel_movement = veldf[(veldf['Time'] >= start_time) & (veldf['Time'] <= end_time)]
odom_movement = odomdf[(odomdf['Time'] >= start_time) & (odomdf['Time'] <= end_time)]

if not cmd_vel_movement.empty and not odom_movement.empty:
    plt.figure(figsize=(14, 7))

    plt.subplot(2, 1, 1)
    plt.plot(cmd_vel_movement['Time'].to_numpy(), cmd_vel_movement['angular.z'].to_numpy(), label='Angular Z Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Angular Velocity (rad/s)')
    plt.legend()
    plt.title('Third Movement: Angular Velocity')

    plt.subplot(2, 1, 2)
    plt.plot(odom_movement['Time'].to_numpy(), odom_movement['yaw'].to_numpy(), label='Yaw')
    plt.xlabel('Time (s)')
    plt.ylabel('Yaw (rad)')
    plt.legend()
    plt.title('Third Movement: Angle')

    plt.tight_layout()
    plt.show()
else:
    print(f"No data found for the third movement in the range 33.8 to 40")


