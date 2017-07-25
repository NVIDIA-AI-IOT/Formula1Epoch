import numpy as np
import cv2
import sys
import signal
import time

def ctrlc_exit(signal, frame):
	sys.exit(0)

capturing_data = False
width = 800
height = 600

signal.signal(signal.SIGINT, ctrlc_exit)

# Capturing images to save into the folder
cap = cv2.VideoCapture(1)

file_path = '/home/nvidia/Formula1Epoch/datacollection/data/camera/'  #make sure to change accordingly

start_time = long(time.time() * 100)

while True:	#If true, captures images to write to a file

	capt_file = open('/home/nvidia/racecar-ws/src/racecar/racecar/scripts/captureButton.txt', 'r')
	capt = capt_file.readline()
	if (capt == "1"):
		capturing_data = True
	else:
		capturing_data = False
	capt_file.close()

	if capturing_data:
	
		timestamp = long(time.time() * 100)

		end_time = timestamp
		total_t = end_time - start_time
	
		if (total_t >= 100 * 1.0/5):
			ret, frame = cap.read()
			frame = cv2.resize(frame, (width, height))
	#	resized = np.asarray(frame)
	#	cv2.imshow('frame', frame)
			count_file = open(file_path + 'count.txt', 'r')
			curr_count = int(count_file.readline())
			count_file.close()

			cv2.imwrite(file_path + 'images/' + str(curr_count) + ".png", frame)
		
			count_file=open('count.txt', 'w')
			count_file.write(str(curr_count + 1))
			count_file.close()
			start_time = timestamp
			print("Saved image \n")

			timestamp_file = open(file_path + 'timestamp.txt', 'a')
			timestamp_file.write(str(timestamp) + "\n")
			timestamp_file.close()

cap.release()
cv2.destroyAllWindows()
