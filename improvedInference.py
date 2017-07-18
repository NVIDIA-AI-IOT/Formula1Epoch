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
imageModel = keras.models.load_model('/home/ubuntu/model.h5')
lidarModel = keras.models.load_model('/home/ricky/Formula1Epoch/networks/LiNet/lidar.h5')

f = open('inferences.txt', 'w')

imageInferences = "\n"
lidarInferences = ""

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def formatRawLidarForInference(lidarText):
        data = open(lidarText, 'r').read()
        data = data.split('\n')
        data = data[:len(data)-1]

        lidars = []

        for d in data:
            lidars.append(LidarInput(d))

        found = False
        lidarsOfInterest = []

        reversedLidar = []

        for l in reversed(lidars):
            reversedLidar.append(l)

        reversedLidar = reversedLidar[1:]

        for l in range(len(reversedLidar)-1):

            if reversedLidar[l+1].angle > reversedLidar[l].angle:
                l += 1
                while(reversedLidar[l+1].angle < reversedLidar[l].angle):
                    lidarsOfInterest.append(reversedLidar[l])
                    break

        return lidarsOfInterest

def infer(rawLidar):
    ret, frame = cap.read()
    resized = cv2.resize(frame, (width, height))

    lidar = formatRawLidarForInference(rawLidar)

    g = lidarModel.predict(np.array([lidar]), batch_size=32, verbose=2)

	o = imageModel.predict(np.array([resized]), batch_size=32, verbose=2)'

    f.write('lidar: ' + g + '\nimage: ' + o)

	imageOutput = o[0]
    lidarOutput = g[0]

	jstk = (imageOutput[0]/2 + lidarOutput[0])/2
	jstk = clamp(jstk, -10, 10)
	return jstk
