import numpy as np
from keras.models import Model, load_model, Sequential
from keras.optimizers import Adam
from keras.layers import Input, Convolution2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
from helperFunctions import imageToPixels
from keras.utils import plot_model
#import tensorflow as tf
import pygame
import pygame.camera
import keras
from pygame.locals import *
import h5py
import time
from PIL import Image

pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera("/dev/video0",(672,376))
cam.start()
model = keras.models.load_model('/home/ubuntu/model.h5')

global joyVal # usage .get()

def getJoyVal():
	return joyVal

def runInference():
	joyVal = pool.apply_async(runInference).get()

def infer():
	print('running infer')
	image = cam.get_image()
	image = pygame.surfarray.array3d(image)
	print(len(image))
	#time.sleep(10)
	global model
	img = imageToPixels(image)
	im2 = Image.fromarray(img, 'RGB')
	resize = im2.resize((672, 376), Image.NEAREST)
	resize = np.array(resize)
	o = model.predict(np.array([resize]), batch_size=32, verbose=2)
	output = o[0]
	jstk = output[0]
	return jstk

# async_result = pool.apply_async(foo, ('world', 'foo')) # tuple of args for foo
# # do some other stuff in the main process
#
# return_val = async_result.get()  # get the return value from your function.
