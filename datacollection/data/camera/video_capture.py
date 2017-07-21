import numpy as np
import cv2
import sys
import signal
import time

def ctrlc_exit(signal, frame):
	sys.exit(0)

CAPTURING_DATA = True
width = 800
height = 600

signal.signal(signal.SIGINT, ctrlc_exit)

# Capturing images to save into the folder
if CAPTURING_DATA:
	cap = cv2.VideoCapture(1)

file_path = '/home/nvidia/Formula1Epoch/datacollection/data/camera/'  #make sure to change accordingly

start_time = long(time.time() * 100)

while CAPTURING_DATA	:	#If true, captures images to write to a file
	count_file = open(file_path + 'count.txt', 'r')
	curr_count = int(count_file.readline())
	count_file.close()
	timestamp = long(time.time() * 100)
		
	
	timestamp_file = open(file_path + 'timestamp.txt', 'a')
	timestamp_file.write(str(timestamp) + "\n")
	timestamp_file.close()
	
	end_time = timestamp
	total_t = end_time - start_time
	
	if (total_t >= 100 * 1.0/30):
		ret, frame = cap.read()
		frame = cv2.resize(frame, (width, height))
#	resized = np.asarray(frame)
#	cv2.imshow('frame', frame)
		cv2.imwrite(file_path + 'images/' + str(curr_count) + ".png", frame)
		
		count_file=open('count.txt', 'w')
		count_file.write(str(curr_count + 1))
		count_file.close()
		start_time = timestamp
		print("Saved image \n")

cap.release()
cv2.destroyAllWindows()
