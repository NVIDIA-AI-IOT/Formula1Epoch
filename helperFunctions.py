from PIL import Image
from numpy import asarray
import glob

# All standalone helper functions can be defined here

def getTrainingData(path):
    # return training sata

    pixelList = []

    for filename in glob.glob(path+"*.jpg"):
        im = Image.open(filename)
        pixelList.append(imageToPixels(im))

    trainX, finalX = splitList(pixelList)
    return trainX, finalX

def imageToPixels(image):
    temp=asarray(image)
    x=temp.shape[0]
    y=temp.shape[1]*temp.shape[2]

    temp.resize((x,y)) # a 2D array
    return temp

def parseTextFile(path):
    # works for csv or txt files
    f = open(path, 'r')

    readings = []
    data = []

    for t in f:
        readings.append(t.strip('\n'))

    for r in readings:

        arr = r.split(',')
        data.append(arr)

    trainY, finalY = splitList(data)
    return trainY, finalY

def splitList(bigAr):
    # 4/5 of data is training data, the rest is testing data
    arrayG = bigAr[0]
    array = []

    for l in arrayG:
        array.append([float(l)])

    split = len(array)*4/5
    normalArray = array[:split]
    testArray = array[split:]
    return normalArray, testArray

g, y = parseTextFile('/home/ricky/readings.txt')
print(g)
