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
from rplidar import RPLidar
# sys.path.append('..')
# from common import helperFunctions

lidar = RPLidar('/dev/ttyUSB0') #make sure to change accordingly
info = lidar.get.info()
health = lidar.get_health()

home = expanduser('~') + '/'
imageModelName = home + 'Formula1Epoch/networks/steerNet/steer.h5'
lidarModelName = home + 'Formula1Epoch/networks/LiNet/lidar.h5'
concatModelName = home + 'Formula1Epoch/networks/LiNet/concat.h5'
imageModel = keras.models.load_model(imageModelName)
lidarModel = keras.models.load_model(lidarModelName)
concatModel = keras.models.load_model(concatModelName)
#cap = cv2.VideoCapture(0) #make sure this is right
width = 800
height = 600
name = 10000

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def infer():
    global concatModel

    imInp = imSubNet()
    liInp = liSubNet()
    inputAr = np.array([imInp, liInp])

    jstk = concatModel.predict(inputAr, batch_size=32, verbose=2)

    return jstk

def imSubNet():
    global name
    global imageModel

    frame = cv2.imread('/home/ubuntu/Formula1Epoch/jetson-inference/detectnet-console/pic.jpg')
    resized = cv2.resize(frame, (width, height))
    o = imageModel.predict(np.array([resized]), batch_size=32, verbose=2)
    imOut = o[0][0]
    return imOut

def liSubNet():
    global lidarModel
    liarr = getLiDARVals()
    output = lidarModel.predict(np.array(liarr), batch_size=32, verbose=2)
    liOut = output[0]
    return liOut

def getLiDARVals():
    scan = (lidar.iter_scans())[len(lidar.iter_scans())-1]
    array = scan #[None] #Get lidar array here
    new_scans = []
    for i in range(360):
        new_scans.append((0,i,sys.maxint))
    for scan in array:
        # print("THIS IS WHAT A SCAN LOOKS LIKE:")
        # print(scan)
        # raw_input()
        angleint = int(scan[1])
        if (angleint >= 360):
            angleint = 359
        new_scans[angleint] = (scan[0], angleint, scan[2])
    #raw_input()
    array = new_scans
    return array

# infer()
