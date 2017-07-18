from PIL import Image, ImageDraw
import sys

x = 0
im = Image.open("/home/ricky/black.jpg")

draw = ImageDraw.Draw(im)
draw.line((x, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
# del draw

# write to stdout
im.show()

for i in range(1000000):
    x+=1
#draw.line((0, 0) + im.size, fill=128)
