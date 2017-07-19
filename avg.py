import random
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

one = []
two = []
expected = []

for i in range(100):
    one.append(random.uniform(-1, 1)) # image predictions

for i in range(100):
    two.append(random.uniform(-1, 1)) #lidar predictions

for i in range(100):
    expected.append(0) # joysticks

def get_weights(one, two):
    weightOne = 0.0
    weightTwo = 0.0

    for i in range(len(one)):

        if abs(expected[i] - one[i]) < abs(expected[i] - two[i]): # if one is closest
            weightOne += abs(expected[i] - one[i])
        elif abs(expected[i] - one[i]) > abs(expected[i] - two[i]):
            weightTwo += abs(expected[i] - two[i])
        else:
            print("#rip")

    w1 = weightOne / (weightOne+weightTwo)
    w2 = weightTwo / (weightOne+weightTwo)

    print("WeightOne: " + str(w1*100) + "%")
    print("WeightTwo: " + str(w2*100) + "%")

    return (w1, w2)

g, h = get_weights()
