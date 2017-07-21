import numpy as np
import os
from keras.models import Model, load_model, Sequential
from keras.optimizers import Adam
from keras.layers import Input, Convolution2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
from helperFunctions import imageToPixels
from keras.utils import plot_model
import keras
import time
from PIL import Image
import cv2
import time
model = keras.models.load_model('/home/ubuntu/model.h5')
width = 672
height = 376

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def infer():
	global model
	global width
	global height
	#img = cv2.imread('/home/ubuntu/Formula1Epoch/jetson-inference/detectnet-console/pic.jpg')
	img = cv2.imread('/home/ubuntu/Desktop/VirtualDrive/demo.png')
	numcap = np.asarray(img)
	#resized = cv2.resize(img, (width, height))
	#resized = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
	#if (np.array([numcap]).shape() == 4):
	if (img is not None): 
		try:
			o = model.predict(np.array([numcap]), batch_size=32, verbose=2)
		except ValueError:
			return 0
		output = o[0]
		jstk = output[0]
		jstk = clamp(jstk, -10, 10)
		return jstk
	return 0
