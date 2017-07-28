from rplidar import RPLidar
import time
import numpy as np

lidar = RPLidar('/dev/ttyUSB0')

for scan in lidar.iter_scans():
	np.save("/home/nvidia/lidar.npy", scan)
	print("saved")
	#print('saved: ' + str(np.load('/home/nvidia/lidar.npy')))

lidar.stop()
lidar.stop_motor()
lidar.disconnect()
#
