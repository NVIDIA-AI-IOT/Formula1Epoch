import threading
import time
import signal
import sys
from inference import infer
#from sweeppy import Sweep

myGlobalVariable = 0
#dev = '/dev/ttyUSB0'

def ctrlc_exit(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, ctrlc_exit)

class CustomThread(object):
	""" Threading example class
	The run() method will be started and it will run in the background
	until the application exits.
	"""

	def __init__(self, interval=1):
		""" Constructor
		:type interval: int
		:param interval: Check interval, in seconds
		"""
		self.interval = interval
		self.globalVar = 0

		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True
		thread.setDaemon(True)                            # Daemonize thread
		thread.start()                                  # Start the execution

	def returnInference():
		return self.globalVar

	def run(self):
		""" Method that runs forever """

		#self.globalVar = 1

		while (True):
			print('Updating...')
			self.globalVar = infer()

  	        # Do something
  	        #print("myGlobal: " + str(myGlobalVariable))
   	        #time.sleep(self.interval)

	def getVar(self):
		#self.globalVar = infer()
	#	self.globalVar += 0.1
		#if (self.globalVar == 1):
		#	self.globalVar = -1
		return 0.5 #self.globalVar


'''
example = CustomThread()

while(True):
	time.sleep(0.5)
	print("My Global Val: " + str(example.globalVar))
	time.sleep(3)
	print('Checkpoint')
	time.sleep(2)
	print('Bye')
'''
