from PIL import Image
import numpy as np
import scipy.misc
import matplotlib.pyplot as plt
from itertools import product

im = Image.open('/home/ricky/Floors/mememachine.png')
im = im.convert('L') # make the image greyscale
bw = im.point(lambda x: 0 if x<128 else 255, '1') # make every pixel either black or white
image = np.array(bw)

width = len(image[0])
height = len(image)

# FALSE = BLACK

class Pix:
    def __init__(self, coor, marked, val=None):
        self.coor = coor
        self.marked = marked
        self.val = val

coordinates = list(product(xrange(width), xrange(height)))
# print(image)

# for w in range(width)
# for h in range(height):
#     pixelArr.append([])
#     for w in range(width):
#         pix = Pix((h, w), image[h][w])
#         pixelArr[len(pixelArr)-1].append(pix)
#
#

#pixelArr = pixelArr[1:]
startPix = (2,2)


currentCells = [startPix]

rows, cols = image.shape
def blackCount():
    g = 0
    for x in range(cols):
        for y in range(rows):
            if image[x,y] == False:
                g+=1
    return g

def finished():
    for x in range(cols):
        for y in range(rows):
            if image[x, y] == True:
                print("FALSE")
                return False
    return True

def surroundingNeigbors(pix):
    neighbors = []

    pixUp = (pix[0], pix[1]+1)
    pixDown = (pix[0], pix[1]-1)
    pixLeft = (pix[0]-1, pix[1])
    pixRight = (pix[0]+1, pix[1])

    markedUp = image[pixUp[0]][pixUp[1]]
    markedDown = image[pixDown[0]][pixDown[1]]
    markedLeft = image[pixLeft[0]][pixLeft[1]]
    markedRight = image[pixRight[0]][pixRight[1]]

    print(markedUp, markedDown, markedLeft, markedRight)

    if markedUp:
        neighbors.append(pixUp)
    if markedDown:
        neighbors.append(pixDown)
    if markedLeft:
        neighbors.append(pixLeft)
    if markedRight:
        neighbors.append(pixRight)

    print(neighbors)
    return neighbors

while finished() == False:
    print("Black count: " + str(blackCount()))

    for c in currentCells:
        #image[c.coor[0]][c.coor[1]].marked = True

        neighbors = surroundingNeigbors(c)

        if len(neighbors) > 0:
            currentCells = []

            for n in neighbors:
                image[n[0]][n[1]] = False
                currentCells.append(n)
        else:
            print("BLOCKED")
            Image.fromarray(image.astype('uint8')*255).show()
            raw_input()
print("FINISHED")
     # look for neighbors
     # if neighbors unmarked, mark them
     # make new neighbors, the current cells

#     endPoint = (width-1, height-1)

pathFound = False
#
# def finished():
#     for w in width:
#         for h in height:
#             if (image[w])
# while pathFound == False:
