from PIL import Image
import numpy as np
import glob
import os

#All standalone helper functions can be defined here

def getTrainingData(p):
    #Parses the filepath to access files
    if p.startswith("/"):
        if p.endswith("/"):
            path = p
        else :
            path = p + "/"
    else:
        if p.endswith("/"):
            path = os.getcwd() + "/" + p
        else:
            path = os.getcwd() + "/" + p + "/"

    print("Path: " + path)
    #Return training data
    pixelList = []

    #Opens all images in the given filepath
    for f in glob.glob(path+"*.png"):   # PIL does not work with JPEG images
        im = Image.open(f)
        # pArr = np.array(im)
        # print("Parr")
        # print(pArr)
        pArr = imageToPixels(im)
        pixelList.append(pArr)

        # pixelArr = imageToPixels(im)
        # print("pixelArr: ")
        # print(pixelArr)
        # pixelList.append(pixelArr)

    #Splits images into validation and training data
    pixelList = pixelList[:len(pixelList)-1]
    trainX = pixelList
    print(len(trainX))
    print(len(trainX[0]))
    w = trainX[0]
    print(len(w[0]))
    z = w[0]
    print(len(z[0]))
    p = z[0]
    print(p[0])
    return np.array(trainX)

def imageToPixels(image):
    #Resizes the image and extracts pixels
    resize = image.resize((672, 376), Image.NEAREST)
    img = np.array(resize)
    return img

def parseTextFile(data):
    trainY, finalY = splitList(data)
    return trainY, finalY

def splitImage(array):
    #4/5 of data is training data, the rest is testing data
    split = len(array)*4/5
    normalArray = array[:split]
    testArray = array[split:]
    #Returns split
    return normalArray, testArray

def splitList(bigAr):
    #4/5 of data is training data, the rest is testing data
    arrayG = bigAr[0]
    array = []

    for l in arrayG:
        array.append([float(l)])

    split = len(array)*4/5
    normalArray = array[:split]
    testArray = array[split:]
    #Returns split
    return normalArray, testArray

def mapImageToJoy(joyDataTxt, imageTimeStampTxt):
    joyStickTimeStamps = [] # Raw output from ROS
    imageTimeStamps = [] # Raw output from imageTimeStamps
    joysticks = []  # Array for the Joystick Objects
    output = []

    f = open(joyDataTxt, 'r').read()
    g = open(imageTimeStampTxt, 'r').read()

    # Format image timestamp data
    imageTStamps = g.split('\n')
    imageTStamps.pop(len(imageTStamps)-1)

    # Format raw ROS joystick data
    joydata = f.split('---')
    joydata.pop(len(joydata)-1)

    # Array of image time stamps is merely for convenience
    for tStamp in imageTStamps:
        imageTimeStamps.append(long(tStamp))

    for d in joydata:
        joy = JoyInput(d)
        joysticks.append(joy)
        joyStickTimeStamps.append(long(joy.timeStamp))

    for im in imageTStamps:
        # For every image, find the joystick input whose timestamp is closest to the image timestamp
        closest = min(joyStickTimeStamps, key=lambda x: abs(x-long(im)))

        for j in joysticks:
            if j.timeStamp == closest:
                output.append(j.axis)   # We want the raw axis value (left-right) for the respective joyInput.
                break

    output = output[1:] # For prediction purposes, we need to take the joystick val before the image
    trainY = output
    for index, item in enumerate(trainY):
        y = trainY[index]
        y = y * 50
        trainY[index] = y
        print(trainY[index])
    return trainY

class JoyInput:
     def __init__(self, joyText):
         self.secs = long(joyText[43:54]) # these are the character locations of these values
         self.nsecs = long(joyText[64:73])
         comm = joyText.split(',')
         self.axis = float(comm[3]) # left-right axis value
         self.timeStamp = long(self.secs*1000 + self.nsecs/1000000) # milliseconds

#x, m = mapImageToJoy('/media/ricky/ZED/joydata.txt', '/media/ricky/ZED/timestamp.txt')
#y, h = getTrainingData('/media/ricky/ZED/images/')
