from PIL import Image
import numpy as np
import glob
import os
import sys
import ast
# sys.path.append('.')

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
    count = 1
    for f in glob.glob(path+"*.png"):   # PIL does not work with JPEG images
        print(count)
        count += 1
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
    count = 1
    for im in imageTStamps:
        # For every image, find the joystick input whose timestamp is closest to the image timestamp
        closest = min(joyStickTimeStamps, key=lambda x: abs(x-long(im)))
        print(count)
        count += 1
        for j in joysticks:
            if j.timeStamp == closest:
                output.append(j.axis)   # We want the raw axis value (left-right) for the respective joyInput.
                break

    output = output[1:] # For prediction purposes, we need to take the joystick val before the image
    output = np.array(output)
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
    print(data)
    data = data.split('\n')
    data = data[:len(data)-3]
    print(data)
    formData = []
    for i, d in enumerate(data):
        if i % 2 == 0:
            f = data[i] + '\n' + data[i+1]
            formData.append(f)
    data = formData
    lidars = []
    output = [[]]

    for d in data:
        lidars.append([(LidarInput(d).params), (LidarInput(d).timestamp)])

    # print(lidars)

    #print output
    return lidars # [[], [5.6, 6.3], []],

def parseLidarData(lidarText, imageTimeStampsTxt):
    lidarArr = formatRawLidar(lidarText)

    sampleLengths = []
    for g in lidarArr:
        sampleLengths.append(len(g))

    medianSampleLength = int(np.round(np.median(sampleLengths)))
    print('wew')
    g = open(imageTimeStampsTxt, 'r').read()
    imageTStamps = g.split('\n')
    imageTStamps.pop(len(imageTStamps)-1)
    for imagT in imageTStamps:
        imagT = long(imagT)

    lidarTimeStamps = [[]]
    output = []
    lastLidar = []

    for l in lidarArr:

        lastLidar.append(l[1])
        #print(lastLidar)

    smallest = 45849584958
    chosenOne = 0

    print("Yes")

    count = 1
    for imIndex in range(len(imageTStamps)-1):
        closest = min(lastLidar, key=lambda x: abs(long(x) - long(imageTStamps[imIndex])))
        print(count)
        count += 1
        for l in lidarArr:
            # new_scans = []
            # for i in range(360):
            #     new_scans.append((0,i,sys.maxint))
            # for scan in l[0]:
            #     angleint = int(scan[1])
            #     if (angleint >= 360):
            #         angleint = 359
            #     new_scans[angleint] = (scan[0], angleint, scan[2])
            if long(l[1]) == long(closest):
                new_scans = []
                for i in range(360):
                    new_scans.append((0,i,0))
                for scan in l[0]:
                    # print("THIS IS WHAT A SCAN LOOKS LIKE:")
                    # print(scan)
                    # raw_input()
                    angleint = int(scan[1])
                    if (angleint >= 360):
                        angleint = 359
                    new_scans[angleint] = (scan[0], angleint, scan[2])
                #raw_input()
                output.append(new_scans)
                # print(new_scans)

                #x = new_scans[0]
                #  output.append([])
                #  output.append(sequenceTo2DArr(l, medianSampleLength))
                break

    # NEED (360, 2) SHAPE!!!!
    #output = output[:len(output)-1]
    #output = output[1:]
    #print("SecodaryOutLen: " + str(len(output)))
    #output.append([])
    output = np.array(output)
    print("Shape")
    print(output.shape)

    print output

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
         se = joyText.split('\n')
         print(se)
         check = se
         for i, d in enumerate(check):
             if check[i] == '':
                 del se[i]
         sec = (se[3].split(': '))[1]
         nsec = (se[4].split(': '))[1]
         comm = joyText.split(',')
         ax = comm[2]
         self.secs = long(sec)
         self.nsecs = long(nsec)
         self.axis = float(ax.strip()) # left-right axis value

         self.timeStamp = long(self.secs*100 + self.nsecs/10000000) # milliseconds
         print(self.timeStamp)

class LidarInput:
    def __init__(self, scanText):
        sp = scanText.split('\n')
        nm = sp[0]
        #nm = nm[1:len(nm)-1]
        nm = eval(nm)
        #print(nm)

        anarr = []
        distarr = []
        strarr = []
        '''for n in nm:
            anarr.append(n[1])
            distarr.append(n[2])
            strarr.append(n[0])'''

        self.params = nm # 0 - 360,000
        self.timestamp = long(sp[1])

# f = parseLidarData("/media/ricky/ZED/lidardata.txt", "/media/ricky/ZED/timestamp.txt")
