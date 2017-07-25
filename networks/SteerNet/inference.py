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
from helperFunctions import sampleArrayForInference
import h5py

modelName = '/home/nvidia/racecar-ws/src/racecar/racecar/scripts/lidar.h5'

model = keras.models.load_model(modelName)

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def infer(arr):
    global name
    global model

    lidarData = sampleArrayForInference(arr)

    o = model.predict(np.array([lidarData]), batch_size=32, verbose=2)
    print("O: " + str(o[0][0]))
    output = o[0]
    jstk = output[0]
    jstk = clamp(jstk, -10, 10)
    return jstk

# infer()
