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
    #trainX, finalX = splitImage(pixelList)
    return pixelList

def imageToPixels(image):
    #Resizes the image and extracts pixels
    #resize = image.resize((672, 376), Image.NEAREST)
    img = np.array(image)
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
    # GIVEs  ARRAY OF JOYSTICK VALUES
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
    return output

def parseLidarData(lidarText, imageTimeStampsTxt):
    # Outputs the lidar values for every image

    data = open(lidarText, 'r').read()
    data = data.split('\n')
    data = data[:len(data)-1]

    g = open(imageTimeStampsTxt, 'r').read()
    imageTStamps = g.split('\n')
    imageTStamps.pop(len(imageTStamps)-1)

    lidarInputs = []
    lidarTimeStamps = []
    output = []

    for d in data:
        lidarInput = LidarInput(d)
        lidarInputs.append(lidarInput)
        lidarTimeStamps.append(lidarInput.timestamp)

    for im in imageTStamps:
        # For every image, find the joystick input whose timestamp is closest to the image timestamp
        closest = min(lidarTimeStamps, key=lambda x: abs(x-long(im)))

        for l in lidarInputs:
            if l.timestamp == closest:
                outp = (l.angle, l.distance, l.strength)
                output.append(outp)   # We want the angle, distance, and strength
                break

    output = [np.array(output)]
    #print(output[0].shape)
    return output
# (none, 1, 1)
class JoyInput:
     def __init__(self, joyText):
         self.secs = long(joyText[42:53]) # these are the character locations of these values
         self.nsecs = long(joyText[64:73])
         comm = joyText.split(',')
         self.axis = float(comm[2]) # left-right axis value
         self.timeStamp = long(self.secs*1000 + self.nsecs/1000000) # milliseconds

class LidarInput:
    def __init__(self, scanText):
        sp = scanText.split(' ')
        self.angle = long(sp[1])/1000.0 # 0 - 360,000
        self.distance = long(sp[3])
        self.strength = long(sp[5])
        self.timestamp = long(sp[7])

#m = mapImageToJoy('/media/ricky/ZED/joydata.txt', '/media/ricky/ZED/timestamp.txt')
d = parseLidarData('/media/ricky/ZED/data/scandata.txt', '/media/ricky/ZED/data/timestamp.txt')
#x, m = mapImageToJoy('/media/ricky/ZED/joydata.txt', '/media/ricky/ZED/timestamp.txt')
#y, h = getTrainingData('/media/ricky/ZED/images/')
print(d)
