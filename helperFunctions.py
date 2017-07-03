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

    #Return training data
    pixelList = []

    #Opens all images in the given filepath
    for filename in glob.glob(path+"*.jpg"):
        im = Image.open(filename)
        #print(im)
        pixelList.append(imageToPixels(im))
    #Splits images into validation and training date
    trainX, finalX = splitImage(pixelList)
    return trainX, finalX

def imageToPixels(image):
    #Resizes the image and extracts pixels
    resize = image.resize((672, 376), Image.NEAREST)
    image_convert = np.swapaxes(np.swapaxes(resize, 1, 2), 0, 1)
    img = np.array(image_convert)
    return img

def parseTextFile(path):
    #Opens text file with given steering values in a '<>,<>,<>' format
    f = open(path, 'r')

    readings = []
    data = []
    #Formats and extracts data, appending to array
    for t in f:
        readings.append(t.strip('\n'))

    for r in readings:

        arr = r.split(',')
        data.append(arr)
    #Splits text data for steering into training and validation
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

#g,x = getTrainingData("testDir")
