from PIL import Image
import numpy as np

im = Image.open('/home/ricky/Floors/h1-1.png')
im = im.convert('L') # make the image greyscale
bw = im.point(lambda x: 0 if x<128 else 255, '1') # make every pixel either black or white

bw.show()
im2 = im.load()
coordinates = [] # positions of all of the pixels on the BW image

wallPos = [] # positions of all the walls

for w in range(bw.size[0]):
    for h in range(bw.size[1]):
            coordinates.append((w, h))
            if (bw.getpixel((w,h)) == 0):
                wallPos.append((w, h))

# junctions = [(28, 49), (460, 64), (466, 243), (21, 247), (188, 371), (464, 367), (830, 249), (828, 54), (833, 371), (1084, 240), (1095, 48), (1720, 246), (1713, 440), (1085, 440), (1082, 631), (1708, 628), (1720, 945), (1720, 824), (1077, 823), (1083, 935), (993, 668), (526, 675), (517, 546), (538, 398), (187, 560), (40, 676), (183, 644), (29, 872), (528, 869), (33, 1068), (537, 1069), (1039, 1131), (1721, 1132), (1571, 60)]
