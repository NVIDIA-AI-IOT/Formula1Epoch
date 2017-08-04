import helperFunctions
import numpy as np
#Formats into raw data saved as string
lidarAr = helperFunctions.parseLidarData('/home/first/Desktop/data/lidar/lidardata.txt', '/home/first/Desktop/data/camera/timestamp.txt')
jstkAr = helperFunctions.mapImageToJoy('/home/first/Desktop/data/joydata.txt', '/home/first/Desktop/data/camera/timestamp.txt')
imgAr = helperFunctions.getTrainingData('/home/first/Desktop/data/camera/images/')
np.save('lidarT1', lidarAr)
np.save('jstkT1', jstkAr)
np.save('imageT1', imgAr)
