import numpy as np
from keras.models import Model, load_model, Sequential
from keras.optimizers import Adam
from keras.layers import Input, Convolution2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
from helperFunctions import imageToPixels
from keras.utils import plot_model
#import tensorflow as tf
import keras
from pygame.locals import *
import time
from PIL import Image
import cv2

cap = cv2.VideoCapture(0) #make sure this is right
width = 672
height = 376
name = 10000
model = keras.models.load_model('/home/ubuntu/model.h5')

# global joyVal # usage .get()
#
# def getJoyVal():
# 	return joyVal
#
# def runInference():
# 	joyVal = pool.apply_async(infer).get()

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def infer():
	global name
#	print('running infer')
#	print(len(image))
	#time.sleep(10)
	global model
	#resize.save(str(name)+'.png')
	#name += 1
        ret, frame = cap.read()
        resized = cv2.resize(frame, (width, height))

	o = model.predict(np.array([resized]), batch_size=32, verbose=2)
	output = o[0]
	jstk = output[0]
	#saveImTxt(newIm, jstk)
	#fil = open(str(name)+".txt","w")
	#fil.write(jstk)
	#fil.close
	#name += 1
#	print("ATIJTFDJG: " + str(jstk))
	jstk = clamp(jstk, -10, 10)
	return jstk

# def saveImTxt(image, jstk):
# 		global name
# 		image.save(str(name)+'.png')
# 		fil = open(str(name)+".txt","w")
# 		fil.write(str(jstk))
# 		fil.close
# 		name += 1
