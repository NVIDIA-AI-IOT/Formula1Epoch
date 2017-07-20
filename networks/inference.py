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
import helperFunctions
from os.path import expanduser
import h5py
import sys
# sys.path.append('..')
# from common import helperFunctions

home = expanduser('~') + '/'
imageModelName = home + 'Formula1Epoch/networks/steerNet/steer.h5'
lidarModelName = home + 'Formula1Epoch/networks/LiNet/lidar.h5'

imageModel = keras.models.load_model(imageModelName)
lidarModel = keras.models.load_model(lidarModelName)

cap = cv2.VideoCapture(0) #make sure this is right
width = 672
height = 376
name = 10000

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def infer(arr):
    global name
    global model

    ret, frame = cap.read()
    resized = cv2.resize(frame, (width, height))

    o = model.predict(np.array([resized]), batch_size=32, verbose=2)
    imOut = o[0][0]
    imgJstk = clamp(imOut, -10, 10)

    lidarData = sampleArrayForInference(arr)
    lidarOutput = model.predict(np.array([lidarData]), batch_size=32, verbose=2)

    output = lidarOutput[0][0]
    lidarJstk = clamp(output, -10, 10)

    jstk = (imgJstk + lidarJstk) /2
    return jstk

# infer()
