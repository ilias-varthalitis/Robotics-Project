#Ilias Varthalitis AM: 4637
#Aristeidis Panagiotou AM:4754

import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt

bag = bagreader('manipulator_trajectories2.bag')

joint_states = bag.message_by_topic('/rrbot/joint_states')

joint_data = pd.read_csv(joint_states)

# Positions
plt.figure(figsize=(10, 10))

plt.subplot(2, 1, 1)
plt.plot(joint_data['Time'].to_numpy(), joint_data['position_0'].to_numpy())
plt.xlabel('Time (s)')
plt.ylabel('Joint 0 Position (radians)')
plt.title('Joint 0 Position')

plt.subplot(2, 1, 2)
plt.plot(joint_data['Time'].to_numpy(), joint_data['position_1'].to_numpy())
plt.xlabel('Time (s)')
plt.ylabel('Joint 1 Position (radians)')
plt.title('Joint 1 Position')

plt.tight_layout()
plt.show()

# Velocities
plt.figure(figsize=(10, 10))

plt.subplot(2, 1, 1)
plt.plot(joint_data['Time'].to_numpy(), joint_data['velocity_0'].to_numpy())
plt.xlabel('Time (s)')
plt.ylabel('Joint 0 Velocity (radians/s)')
plt.title('Joint 0 Velocity')

plt.subplot(2, 1, 2)
plt.plot(joint_data['Time'].to_numpy(), joint_data['velocity_1'].to_numpy())
plt.xlabel('Time (s)')
plt.ylabel('Joint 1 Velocity (radians/s)')
plt.title('Joint 1 Velocity')

plt.tight_layout()
plt.show()
