from PIL import Image
import numpy as np
import signal
import sys

def ctrlc_exit(signal, frame):
	sys.exit(0)

signal.signal(signal.SIGINT, ctrlc_exit)

class Drive(object):

	def __init__(self):
		""" Constructor
		"""
		global drivepath
		drivepath = [1, 1, 1, 1]
		global curr_drive
		curr_drive = drivepath[0]
		global curr_index
		curr_index = 0
		global jstk_turn
		jstk_turn = 0

	def invertImg(self, imgarr):
		newarr = []
		if imgarr is None:
			return 0
		for w in range(0, len(imgarr)):
			newarr.append(imgarr[len(imgarr) - 1 - w])
		return newarr

	def invertLidar(self, lidar_data):
		new_scans = []
		angle_int= 359

		for i in range(359):
			new_scans.append((0,i,0))
		for scan in lidar_data:
			new_scans[359 - angle_int] = (scan[0], angle_int, scan[2])
			angle_int -= 1
			if (angle_int < 0):
				angle_int = 359

		array = new_scans
		return array

	def getTurn(self):
		if curr_drive == 0:
			return "left"
		return "right"

	def nextTurn(self):
		curr_index += 1
		if curr_index == len(drivepath):
			curr_index = 0
		curr_drive = drivepath[curr_index]

	def get_jstk_turn(self):
		return jstk_turn

	def set_jstk_turn(self, val):
		jstk_turn = val

#drive = Drive()
#print(drive.invertImg([[1,0],[0,1],[1,1],[0,0]]))
