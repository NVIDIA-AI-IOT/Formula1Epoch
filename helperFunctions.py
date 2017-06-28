from PIL import Image
import numpy as np
import glob

# All standalone helper functions can be defined here

def getTrainingData(path):
    # return training sata
    pixelList = []

    for filename in glob.glob(path+"*.jpg"):
        im = Image.open(filename)
        #print(im)
        pixelList.append(imageToPixels(im))
        print(len(pixelList))

    trainX, finalX = splitImage(pixelList)
    return trainX, finalX

def imageToPixels(image):
    resize = image.resize((672, 376), Image.NEAREST)
    #temp = np.array(resize)
    image_convert = np.swapaxes(np.swapaxes(resize, 1, 2), 0, 1)
    img = np.array(image_convert)
    #print(img)
    return img

def parseTextFile(path):
    # works forheight csv or txt files
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

def splitImage(array):
    # 4/5 of data is training data, the rest is testing data
    split = len(array)*4/5
    normalArray = array[:split]
    testArray = array[split:]
    return normalArray, testArray

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

image = imageToPixels(Image.open("/home/ricky/test.jpg"))
x, y = getTrainingData("/home/ricky/testDir/")
print(x)
print(len(x))
print("\n\n")
print(x[0])
print(len(x[0]))
print("\n\n")
print(x[0][0])
print(len(x[0][0]))
print("\n\n")
print(x[0][0][0])
print("\n\n")
print(x[0][0][0][0])
