from PIL import Image
import numpy as np
import scipy.misc

im = Image.open('/home/ricky/Floors/mememachine.png')
im = im.convert('L') # make the image greyscale
bw = im.point(lambda x: 0 if x<128 else 255, '1') # make every pixel either black or white

im2 = im.load()
coordinates = []
paths = []

coordinates = np.array(im)
#print(coordinates)
newIm = Image.fromarray(coordinates)
#newIm.show()

path_found = False
startpos_x = 2
startpos_y = 2

paths.append([])
paths[0].append("down")
paths[0].append((startpos_x, startpos_y))

a = 0

pathLength = len(paths)
# print len(paths)
p = 0

while (path_found != True):

	while(p != len(paths)):
		print("p: " + str(p))
		print("Path lenth: " + str(pathLength))

		pixup = (paths[p][1][0], paths[p][1][1]-1)
		pixdown = (paths[p][1][0], paths[p][1][1]+1)
		pixleft = (paths[p][1][0]-1, paths[p][1][1])
		pixright = (paths[p][1][0]+1, paths[p][1][1])

		pixvalup = coordinates[pixup[0], pixup[1]]
		pixvaldown = coordinates[pixdown[0], pixdown[1]]
		pixvalleft = coordinates[pixleft[0], pixleft[1]]
		pixvalright = coordinates[pixright[0], pixright[1]]

		print(pixup, pixdown, pixleft, pixright)
		print("Up: " + str(pixvalup))
		print("Down: " + str(pixvaldown))

		print(pixvalup, pixvaldown, pixvalleft, pixvalright)

		if pixvalup == 255:
			paths.append(["up", (pixup[0], pixup[1])])
			print("UP")

		if pixvaldown == 255:
			paths.append(["down", (pixdown[0], pixup[1])])
			print("DOWN")

		print("Path length is now " + str(len(paths)))

		p+=1
	#     if pixvaldown == 255: # down is white
			#paths.append["down", (pixdown[0], pixdown[1])]

	path_found = True
		 #print("Pixup: " + str(pixup))
	#  Get and set current/up/down/left/right pixel values
	#     pix = coordinates[path[len(path) - 1][0]][path[len(path) - 1][1]]
	#
	#     pixup = coordinates[path[len(path) - 1][0]][path[len(path) - 1][1] - 1]
	#     pixdown = coordinates[path[len(path) - 1][0]][path[len(path) - 1][1] + 1]
	#     pixleft = coordinates[path[len(path) - 1][0] - 1][path[len(path) - 1][1]]
	#     pixright = coordinates[path[len(path) - 1][0] + 1][path[len(path) - 1][1]]
	#
	#     #print ("   " + str(pixup) + "\n" + str(pixleft) + " o " + str(pixright) + "\n" + "   " + str(pixright))
	#
	#     #print("Current pixel is: " + str(pix))
	#
	#     append_tuple = (0, 0)
	#
	#     if (pixup == 255):
	#         # Add to the original path
	#         if (paths[p][0] == 0):
	#             paths[p].append((path[len(path) - 1][0], path[len(path) - 1][1] - 1))
	#         else:
	#             paths.append([])
	#             paths[len(paths) - 1].append(0)
	#             for step in range(1, len(paths[p])):
	#                 paths[len(paths) - 1].append(paths[p][step])
	#             paths[len(paths) - 1].append((path[len(path) - 1][0], path[len(path) - 1][1] - 1))
	#
	#         im.putpixel((path[len(path) - 1][0], path[len(path) - 1][1] - 1), 150)
	#
	#     if (pixleft == 255):
	#         if (paths[p][0] == 1):
	#             #print(paths[p])
	#             paths[p].append((path[len(path) - 1][0] - 1, path[len(path) - 1][1]))
	#             #print(paths[p])
	#         else:
	#             a = p
	#             paths.append([])
	#             paths[len(paths) - 1].append(1)
	#             for step in range(1, len(paths[p])):
	#                 paths[len(paths) - 1].append(paths[p][step])
	#             paths[len(paths) - 1].append((path[len(path) - 1][0] - 1, path[len(path) - 1][1]))
	#         #print(paths[p])
	#
	#         im.putpixel((path[len(path) - 1][0], path[len(path) - 1][1] - 1), 150)
	#     #print(paths[p])
	#
	#     if (pixdown == 255):
	#         if (paths[p][0] == 2):
	#             paths[p].append((path[len(path) - 1][0], path[len(path) - 1][1] + 1))
	#         else:
	#             paths.append([])
	#             paths[len(paths) - 1].append(2)
	#             for step in range(1, len(paths[p])):
	#                 paths[len(paths) - 1].append(paths[p][step])
	#             paths[len(paths) - 1].append((path[len(path) - 1][0], path[len(path) - 1][1] + 1))
	#
	#         im.putpixel((path[len(path) - 1][0], path[len(path) - 1][1] + 1), 150)
	#
	#     if (pixright == 255):
	#         if (paths[p][0] == 3):
	#             paths[p].append((path[len(path) - 1][0], path[len(path) - 1][1] + 1))
	#         else:
	#             paths.append([])
	#             paths[len(paths) - 1].append(3)
	#             for step in range(1, len(paths[p])):
	#                 paths[len(paths) - 1].append(paths[p][step])
	#             paths[len(paths) - 1].append((path[len(path) - 1][0] + 1, path[len(path) - 1][1]))
	#
	#         im.putpixel((path[len(path) - 1][0], path[len(path) - 1][1] + 1), 150)
	#
	# #print(str(paths) + "\n")
	#
	# largestIndex = 0
	# largestSize = 2
	#
	# im.save("xd.png")
	#
	# #im.show()
	#
	# for p in range(len(paths)):
	#     if (len(paths[p]) > largestSize):
	#         largestIndex = p
	#         largestSize = len(paths[p])
	#         print("At index " + str(largestIndex) + " with size " + str(largestSize) + ": " + str(paths[p]))
