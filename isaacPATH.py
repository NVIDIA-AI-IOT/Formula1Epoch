from PIL import Image
import numpy as np
import scipy.misc

im = Image.open('/home/iwilcove/Desktop/building.png')
im = im.convert('L') # make the image greyscale
bw = im.point(lambda x: 0 if x<128 else 255, '1') # make every pixel either black or white

im2 = im.load()
coordinates = []
paths = []

for w in range(bw.size[0]):
	coordinates.append([])
	for h in range(bw.size[1]):
            coordinates[w].append(bw.getpixel((h,w)))

print(coordinates)

scipy.misc.toimage(coordinates, cmin=0.0, cmax=255.0).save('outfile.jpg')

path_found = False
startpos_x = 2
startpos_y = 2

paths.append([])
paths[0].append(2)
paths[0].append((startpos_x, startpos_y))

a = 0

while (path_found != True):

	pathlen = len(paths)

	for p in range(1, pathlen):

		path = paths[p]

		# Get and set current/up/down/left/right pixel values
		pix = coordinates[path[len(path) - 1][0]][path[len(path) - 1][1]]

		pixup = coordinates[path[len(path) - 1][0]][path[len(path) - 1][1] - 1]
		pixdown = coordinates[path[len(path) - 1][0]][path[len(path) - 1][1] + 1]
		pixleft = coordinates[path[len(path) - 1][0] - 1][path[len(path) - 1][1]]
		pixright = coordinates[path[len(path) - 1][0] + 1][path[len(path) - 1][1]]

		#print ("   " + str(pixup) + "\n" + str(pixleft) + " o " + str(pixright) + "\n" + "   " + str(pixright))

		#print("Current pixel is: " + str(pix))

		append_tuple = (0, 0)

		if (pixup == 255):
			# Add to the original path
			if (paths[p][0] == 0):
				paths[p].append((path[len(path) - 1][0], path[len(path) - 1][1] - 1))
			else:
				paths.append([])
				paths[len(paths) - 1].append(0)
				for step in range(1, len(paths[p])):
					paths[len(paths) - 1].append(paths[p][step])
				paths[len(paths) - 1].append((path[len(path) - 1][0], path[len(path) - 1][1] - 1))

			im.putpixel((path[len(path) - 1][0], path[len(path) - 1][1] - 1), 150)

		if (pixleft == 255):
			if (paths[p][0] == 1):
				#print(paths[p])
				paths[p].append((path[len(path) - 1][0] - 1, path[len(path) - 1][1]))
				#print(paths[p])
			else:
				a = p
				paths.append([])
				paths[len(paths) - 1].append(1)
				for step in range(1, len(paths[p])):
					paths[len(paths) - 1].append(paths[p][step])
				paths[len(paths) - 1].append((path[len(path) - 1][0] - 1, path[len(path) - 1][1]))
			#print(paths[p])

			im.putpixel((path[len(path) - 1][0], path[len(path) - 1][1] - 1), 150)
		#print(paths[p])

		if (pixdown == 255):
			if (paths[p][0] == 2):
				paths[p].append((path[len(path) - 1][0], path[len(path) - 1][1] + 1))
			else:
				paths.append([])
				paths[len(paths) - 1].append(2)
				for step in range(1, len(paths[p])):
					paths[len(paths) - 1].append(paths[p][step])
				paths[len(paths) - 1].append((path[len(path) - 1][0], path[len(path) - 1][1] + 1))

			im.putpixel((path[len(path) - 1][0], path[len(path) - 1][1] + 1), 150)

		if (pixright == 255):
			if (paths[p][0] == 3):
				paths[p].append((path[len(path) - 1][0], path[len(path) - 1][1] + 1))
			else:
				paths.append([])
				paths[len(paths) - 1].append(3)
				for step in range(1, len(paths[p])):
					paths[len(paths) - 1].append(paths[p][step])
				paths[len(paths) - 1].append((path[len(path) - 1][0] + 1, path[len(path) - 1][1]))

			im.putpixel((path[len(path) - 1][0], path[len(path) - 1][1] + 1), 150)
	
	#print(str(paths) + "\n")

	largestIndex = 0
	largestSize = 2

	im.save("xd.png")	

	#im.show()
	
	for p in range(len(paths)):
		if (len(paths[p]) > largestSize):
			largestIndex = p
			largestSize = len(paths[p])
			print("At index " + str(largestIndex) + " with size " + str(largestSize) + ": " + str(paths[p]))
