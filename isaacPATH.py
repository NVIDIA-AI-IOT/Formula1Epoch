from PIL import Image
import numpy as np
import scipy.misc

im = Image.open('/home/iwilcove/Desktop/building.png')
im = im.convert('L') # make the image greyscale
bw = im.point(lambda x: 0 if x<128 else 255, '1') # make every pixel either black or white

im2 = im.load()
coordinates = []
paths = []

print(bw.size)
print(bw.size[0])
print(bw.size[1])

for w in range(bw.size[0]):
	coordinates.append([])
	for h in range(bw.size[1]):
    		coordinates[w].append(bw.getpixel((w,h)))

print(coordinates)

print(len(coordinates))
print(len(coordinates[0]))

scipy.misc.toimage(coordinates, cmin=0.0, cmax=255.0).save('outfile.jpg')

path_found = False
startpos_x = 2
startpos_y = 2

paths.append([])
paths[0].append(2)
paths[0].append((startpos_x, startpos_y))

a_path = [(2,2)]

def currX():
	return path[len(path) - 1][0]

def currY():
	return path[len(path) - 1][1]

def pathExists(path):
	for p in paths:
		if (path[1:] == p[1:]):
			return True
	return False

while (path_found != True):

	'''

	if (coordinates[a_path[len(a_path) - 1][0]][a_path[len(a_path) - 1][1] + 1] == 255):
		print ("down")
		a_path.append((a_path[len(a_path) - 1https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F30455742%2F7895722859%2F1%2Foriginal.jpg?w=800&rect=0%2C42%2C598%2C299&s=905a3ca8a5ad3b49c8a45f8879e73edd][0], a_path[len(a_path) - 1][1] + 1))
		im.putpixel((a_path[len(a_path) - 1][0], a_path[len(a_path) - 1][1] + 1), 150)
	else:
		print ("hit bottom at " + str((a_path[len(a_path) - 1][0], a_path[len(a_path) - 1][1])))
		im.save("xd.png")	
		im.show()
		path_found = True

	'''

	pathlen = len(paths)

	for p in range(pathlen):

		path = paths[p]

		# Get and set current/up/down/left/right pixel values
		pix = coordinates[currX()][currY()]

		pixup = coordinates[currX()][currY() - 1]
		pixdown = coordinates[currX()][currY() + 1]
		pixleft = coordinates[currX() - 1][currY()]
		pixright = coordinates[currX() + 1][currY()]

		#print ("   " + str(pixup) + "\n" + str(pixleft) + " o " + str(pixright) + "\n" + "   " + str(pixright))

		#print("Current pixel is: " + str(pix))

		append_tuple = (0, 0)

		if (pixup == 255):
			stop_path = False
			proposed_path = []
			proposed_path.append(0)
			for step in range(1, len(paths[p])):
					proposed_path.append(paths[p][step])
					if (paths[p][step] == (currX(), currY() - 1)):
						stop_path = True
			proposed_path.append((currX(), currY() - 1))
			# Add to the original path
			if not stop_path:
				if (paths[p][0] == 0):
					paths[p].append((currX(), currY() - 1))
				elif not pathExists(proposed_path):
					paths.append(proposed_path)

		if (pixleft == 255):
			stop_path = False
			proposed_path = []
			proposed_path.append(1)
			for step in range(1, len(paths[p])):
					proposed_path.append(paths[p][step])
					if (paths[p][step] == (currX() - 1, currY())):
						stop_path = True
			proposed_path.append((currX() - 1, currY()))
			if not stop_path:
				if (paths[p][0] == 1):
					paths[p].append((currX() - 1, currY()))
				elif not pathExists(proposed_path):
					paths.append(proposed_path)

		if (pixdown == 255):
			stop_path = False
			proposed_path = []
			proposed_path.append(2)
			for step in range(1, len(paths[p])):
					proposed_path.append(paths[p][step])
					if (paths[p][step] == (currX(), currY() + 1)):
						stop_path = True
			proposed_path.append((currX(), currY() + 1))
			if not stop_path:
				if (paths[p][0] == 2):
					paths[p].append((currX(), currY() + 1))
				elif not pathExists(proposed_path):
					paths.append(proposed_path)

		if (pixright == 255):
			stop_path = False
			proposed_path = []
			proposed_path.append(3)
			for step in range(1, len(paths[p])):
					proposed_path.append(paths[p][step])
					if (paths[p][step] == (currX() + 1, currY())):
						stop_path = True
			proposed_path.append((currX() + 1, currY()))
			if not (stop_path):
				if (paths[p][0] == 3):
					paths[p].append((currX() + 1, currY()))
				elif not pathExists(proposed_path):
					paths.append(proposed_path)

		im.putpixel((currX(), currY()), 200)
	
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
	for c in range(1, len(paths[largestIndex])):
		im.putpixel(paths[largestIndex][c], 100)
	im.save("IdealPath.png")
	
	im.show()
