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
from drive import Drive

#lidar = RPLidar('/dev/ttyUSB0') #make sure to change accordingly

imageModelName ='/home/nvidia/Formula1Epoch/networks/SteerNet/ImageNet/image.h5'
lidarModelName = '/home/nvidia/Formula1Epoch/networks/SteerNet/LiNet/lidar.h5'
concatModelName = '/home/nvidia/Formula1Epoch/networks/SteerNet/ConcatNet/concat.h5'
imageModel = keras.models.load_model(imageModelName)
lidarModel = keras.models.load_model(lidarModelName)
concatModel = keras.models.load_model(concatModelName)
#cap = cv2.VideoCapture(0) #make sure this is right
width = 800
height = 600
name = 10000

drive = Drive()

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def infer():
    global concatModel

    imnp = imSubNet()
    linp = liSubNet()
    return linp
    inputAr = np.array([imnp, linp])
    inputAr = np.expand_dims(inputAr, axis=0)

    #jstk = concatModel.predict(inputAr, batch_size=32, verbose=2)
    #print("Joystick: " + str(jstk[0][0]))
    #jstk =  (imnp + linp) / 2
    jstk = linp
    #jstk = jstk[0][0]
    logs = open('/home/nvidia/Formula1Epoch/inferLog.txt', 'a')
    if jstk >= 0.8:
        drive.set_jstk_turn(1)
    elif jstk <= 0.2 and drive.get_jstk_turn() == 1:
        drive.set_jstk_turn(0)
        drive.nextTurn()
        logs.write("next turn")
    if drive.getTurn() == 1:
        logs.write("right")
        print "right"
        logs.close()
        return jstk * -1 + 0.2
    else:
        print "left"
	print "-"
    logs.write("left")
    logs.close()
    return jstk

def imSubNet():
    global name
    global imageModel
    frame = cv2.imread('/home/nvidia/Formula1Epoch/jetson-inference/pic.jpg')
    frame = np.array(frame)
    if drive.getTurn() == "right":
        frame = np.array(drive.invertImg(frame.tolist()))
    try:
        frame = np.expand_dims(frame, axis=0)
        o = imageModel.predict(np.array(frame), batch_size=32, verbose=2)
        imOut = o[0][0]
        print("Image: " + str(imOut))
        return imOut
    except:
        pass
    return 0

def liSubNet():
    global lidarModel
    lidararr = np.array(getLiDARVals())
    if getLiDARVals() == 0:
        return 0
    if drive.getTurn == "right":
        lidararr = np.array(drive.invertLidar(lidararr.tolist()))
    lidarr = np.expand_dims(lidararr, axis=0)
    try:
    	output = lidarModel.predict(lidarr, batch_size=32, verbose=2)
    	liOut = output[0][0]
    	return liOut
    except:
        return 0

def getLiDARVals():
    try:
        array = np.load('/home/nvidia/lidar.npy')
    except:
        print('lidar data not loaded')
        return 0

    new_scans = []
    for i in range(360):
        new_scans.append((0,i,0))
    for scan in array:
        angleint = int(scan[1])
        if (angleint >= 360):
            angleint = 359
        new_scans[angleint] = (scan[0], angleint, scan[2])
    array = new_scans
    return array

#for r in range(1000):
#	infer()
#while True:
#	infer()
#	time.sleep(0.5)
