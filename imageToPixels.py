from PIL import Image
from numpy import*

def imageToPixels(image):
    temp=asarray(Image.open(image))
    x=temp.shape[0]
    y=temp.shape[1]*temp.shape[2]

    temp.resize((x,y)) # a 2D array
    return temp
