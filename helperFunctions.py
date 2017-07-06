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
    for f in glob.glob(path+"*.png"):
#        print("filename: " + f)
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
    trainX, finalX = splitImage(pixelList)
    return trainX, finalX

def imageToPixels(image):
    #Resizes the image and extracts pixels
    resize = image.resize((672, 376), Image.NEAREST)
    image_convert = np.swapaxes(np.swapaxes(resize, 1, 2), 0, 1)
    img = np.array(image_convert)
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
    imageTimeStamps = []

    joysticks = []

    output = []
    joyValues = []

    f = open(joyDataTxt, 'r').read()
    g = open(imageTimeStampTxt, 'r').read()

    iData = g.split('\n')
    iData.pop(len(iData)-1)

    joydata = f.split('---')
    joydata.pop(len(joydata)-1)

    for tStamp in iData:
        imageTimeStamps.append(long(tStamp))

    for d in joydata:
        joy = JoyInput(d)
        joysticks.append(joy)
        joyStickTimeStamps.append(long(joy.timeStamp))

    for im in iData:
        closest = min(joyStickTimeStamps, key=lambda x: abs(x-long(im)))

        for j in joysticks:
            if j.timeStamp == closest:
                output.append(j.axis)
                break

    o = output[49:482]
    print(len(o))
    return o

def remove_duplicates(l):
    return list(set(l))

class JoyInput:
     def __init__(self, joyText):
         self.secs = long(joyText[41:52])
         self.nsecs = long(joyText[64:73])
         comm = joyText.split(',')
         self.axis = float(comm[3])
         self.timeStamp = long(self.secs*1000 + self.nsecs/1000000)

x = mapImageToJoy('/media/ricky/ZED/joydata.txt', '/media/ricky/ZED/timestamp.txt')
y, h = getTrainingData('/home/ricky/testDir2')

print("Output: ")
print(h)
