import numpy as np
from keras.models import Model, load_model, Sequential
from keras.optimizers import Adam
from keras.layers import Input, Convolution2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
from helperFunctions import imageToPixels
from keras.utils import plot_model
import keras
import time
from PIL import Image
import cv2

cap = cv2.VideoCapture(0) #make sure this is right
width = 672
height = 376
name = 10000
model = keras.models.load_model('/home/ubuntu/model.h5')

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def infer():
	global name
	global model
        ret, frame = cap.read()
        resized = cv2.resize(frame, (width, height))

	o = model.predict(np.array([resized]), batch_size=32, verbose=2)
	output = o[0]
	jstk = output[0]
	jstk = clamp(jstk, -10, 10)
	return jstk
