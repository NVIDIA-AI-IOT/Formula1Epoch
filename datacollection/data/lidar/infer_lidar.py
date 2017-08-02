from rplidar import RPLidar
import time
import numpy as np
import sys
import signal

def ctrlc_exit(signal, frame):
	lidar.stop()
	lidar.stop_motor()
	lidar.disconnect()
	print("\nLiDAR stopped")
	sys.exit(0)

signal.signal(signal.SIGINT, ctrlc_exit)

for i in range (100):

	try:
		lidar = RPLidar('/dev/ttyUSB0')

		print("Reading LiDAR...")

		for scan in lidar.iter_scans():
			np.save("/home/nvidia/lidar.npy", scan)

		lidar.stop()
		lidar.stop_motor()
		lidar.disconnect()
	except:
		pass
