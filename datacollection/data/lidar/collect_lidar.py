from rplidar import RPLidar
import time
lidar = RPLidar('/dev/ttyUSB0')

for scan in lidar.iter_scans():
	print(scan)
	timestamp = long(time.time() * 100)
	print (timestamp)

lidar.stop()
lidar.stop_motor()
lidar.disconnect()
