from PIL import Image
import numpy as np
import glob
import os
import sys

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

def sequenceTo2DArr(seq, medianSampleLength):
    # output = [[]]
    distance = []

    out = []
    # want to return an array of distances, corresponding with angles
    seqLen = len(seq)
    # print("Seq len: " + str(len(seq)))
    #print("medianSampleLength: " + str(medianSampleLength))

    for m in range(medianSampleLength):
        if m < seqLen:
            out.append([seq[m].distance, (seq[m].angle)])
            # print(out)
            # raw_input()
        else:
            out.append([sys.maxint, sys.maxint])

    # print(out)
    # print("Outlen: " + str(np.array(out).shape))
    # raw_input()
    # print("OUT: ")
    # print(out)
    # print("\n")
    return out

def formatRawLidar(lidarText):
    data = open(lidarText, 'r').read()
    data = data.split('\n')
    data = data[:len(data)-1]

    lidars = []
    output = [[]]

    for d in data:
        lidars.append(LidarInput(d))

    #print(lidars)

    for l in range(len(lidars)-1): # get sequences of lidar (360 degrees)
        output[len(output)-1].append(lidars[l])

        if lidars[l+1].angle < lidars[l].angle:
            output.append([])

    #print output
    return output # [[], [5.6, 6.3], []],

def parseLidarData(lidarText, imageTimeStampsTxt):
    lidarArr = formatRawLidar(lidarText)

    sampleLengths = []
    for g in lidarArr:
        sampleLengths.append(len(g))

    medianSampleLength = int(np.round(np.median(sampleLengths)))

    g = open(imageTimeStampsTxt, 'r').read()
    imageTStamps = g.split('\n')
    imageTStamps.pop(len(imageTStamps)-1)

    for imagT in imageTStamps:
        imagT = long(imagT)

    lidarTimeStamps = [[]]
    output = [[]]
    lastLidar = []

    for l in lidarArr:
        lastLidar.append(l[len(l)-1].timestamp)

    smallest = 45849584958
    chosenOne = 0

    for imIndex in range(len(imageTStamps)-1):

        closest = min(lastLidar, key=lambda x: abs(long(x) - long(imageTStamps[imIndex])))

        for l in lidarArr:
             if long(l[len(l)-1].timestamp) == long(closest):
                 newArr = sequenceTo2DArr(l, medianSampleLength)
                 #raw_input()
                 output.append(newArr)
                #  output.append([])
                #  output.append(sequenceTo2DArr(l, medianSampleLength))
                 break

    # NEED (360, 2) SHAPE!!!!
    #output = output[:len(output)-1]
    output = output[1:]
    #print("SecodaryOutLen: " + str(len(output)))
    #output.append([])
    output = np.array(output)

    return output

def sampleArrayForInference(sampleArr):
    # Output: [(distance, angle), (distance, angle)]
    output = []

    for s in sampleArr:
        output.append((s.distance, s.angle))

    return output

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

        output = []

        for m in range(39):
            if m < 39:
                output.append([lidarsOfInterest[m].distance, (lidarsOfInterest[m].angle)])
            else:
                output.append([lidarsOfInterest.maxint, lidarsOfInterest.maxint])
        # print(output)
        return output
            # if lidars[l+1].angle < lidars[l].angle:
            #     if found == False:
            #         found = True
            #     else:
            #         lidarsOfInterest.append(lidars[l])

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

# j = formatRawLidarForInference('/media/ricky/UBUNTU/data/scandata.txt')
# print(j)
# #m = mapImageToJoy('/media/ricky/ZED/joydata.txt', '/media/ricky/ZED/timestamp.txt')
#d = parseLidarData('/media/ricky/ZED/data/scandata.txt', '/media/ricky/ZED/data/timestamp.txt')
#ayy = formatRawLidar('/media/ricky/ZED/data/scandata.txt')
#b = parseLidarData('/media/ricky/ZED/data/scandata.txt', '/media/ricky/ZED/data/timestamp.txt')
# #x, m = mapImageToJoy('/media/ricky/ZED/joydata.txt', '/media/ricky/ZED/timestamp.txt')
# #y, h = getTrainingData('/media/ricky/ZED/images/')
# print(b)
# print("\n")
# print(b[0])
# print("\n")
# print(b[0][0])
# print("\n")
#print(b[0][0][0])
