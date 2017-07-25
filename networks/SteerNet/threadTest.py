import threading
import time
import signal
import sys
from inference import infer
from sweeppy import Sweep

myGlobalVariable = 0
dev = '/dev/ttyUSB0'

def signal_handler(signal, frame):
	print ("Exit")
	sys.exit(0)

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
		return globalVar

	def run(self):
		""" Method that runs forever """
#		with Sweep(dev) as sweep:
#			sweep.set_sample_rate(1000)
#			sweep.start_scanning()
#			for scan in sweep.getscans():
#				for samples in scan:
#					scanVar = samples			

		while(True):
			print('Updating...')
#   	        self.globalVar = infer(scanVar)
				
  	        # Do something
  	        #print("myGlobal: " + str(myGlobalVariable))
   	        #time.sleep(self.interval)

	def getVar(self):
		return self.globalVar



#example.run()

#while(True):
#    time.sleep(0.5)
#    print("My Global Val: " + str(example.globalVar))
# time.sleep(3)
# #print('Checkpoint')
# time.sleep(2)
# #print('Bye')
