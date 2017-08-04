#import tensorflow as tf
import numpy as np
import sys
sys.path.append('../..')
#import matplotlib
#from matplotlib.pyplot import imshow
from keras.models import Model, load_model, Sequential
from keras.optimizers import Adam
from keras.layers import Input, MaxPooling1D, Convolution2D, MaxPooling2D, Convolution1D, Activation, Dropout, Flatten, Dense
import cv2
import helperFunctions
from keras.utils import plot_model
from os.path import expanduser
import keras
from keras import regularizers
def model():
    #Model with 3 hidden layers
    #Input takes    img = Input(shape = (167, 54), name = 'img')
    #Convolution/Pooling Layer 1
    lid = Input(shape = (2,), name = 'lid')

    '''x = Convolution1D(2, 2)(lid)
    fdsjafldk
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(4, 2)(x)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(4, 2)(x)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)'''

    x = Dense(16, kernel_regularizer=regularizers.l2(0.001))(lid)
    x = Activation('relu')(x)

    x = Dense(32, kernel_regularizer=regularizers.l2(0.003))(x)
    x = Activation('relu')(x)

    x = Dense(64, kernel_regularizer=regularizers.l2(0.005))(x)
    x = Activation('linear')(x)
    x = Dropout(.3)(x)

    jstk = Dense(1, name='jstk')(x)

    net = Model(input=[lid], output=jstk)
    adam = keras.optimizers.Adam(lr=0.00035, beta_1=0.99, beta_2=0.9999, epsilon = 1e-08, decay=0.0005)
    net.compile(optimizer=adam, loss='mean_squared_error', metrics=['accuracy'])
    print(net.summary())
    return net

def trainModel(model, imgIn, jstkOut):
    #Trains predefined model with verbose logging, input image data and output steering data
    print(jstkOut)
    model.fit(x=imgIn, y=jstkOut, batch_size=32, epochs=300, verbose=2, callbacks=None, validation_split=0.2, shuffle=True, initial_epoch=0)
    modelName = 'concatNetT1'
    modelPng = modelName + ".png"
    modelName = modelName + ".h5"
    #Plots the trained model
    #plot_model(modelName, to_file=modelPng)
    model.save(modelName)
    print("Saved as %s" %(modelName) )
    return model

def testModel(model, testX, testY):
    # Test model and evauluate accuracy, prints it
    scores = model.evaluate(testX, testY)
    print("\nAccuracy: " + model.metrics_name[1], scores[1]*100)

def main():
    # #Main Function, starts with path inputs
    # imagePath = raw_input("Please enter the filepath to your images folder")
    # labelPath = raw_input("Please enter the filepath to your labels folder")
    #Uses helper functions to get array of images and outputs
    home = expanduser('~') + '/'
    imageModelName = home + 'Formula1Epoch/SteerNetL2Conv6T1.h5'
    lidarModelName = home + 'Formula1Epoch/networks/LiNet/sickT1.h5'
    imageModel = keras.models.load_model(imageModelName)
    lidarModel = keras.models.load_model(lidarModelName)
    #lidarAr = helperFunctions.parseLidarData('/home/first/Desktop/data2/lidar/lidardata.txt', '/home/first/Desktop/data2/camera/timestamp.txt')
    #jstkAr = helperFunctions.mapImageToJoy('/home/first/Desktop/data2/joydata.txt', '/home/first/Desktop/data2/camera/timestamp.txt')
    #imgAr = helperFunctions.getTrainingData('/home/first/Desktop/data2/camera/images/')
    lidarAr = np.load('lidarT1.npy')
    jstkAr = np.load('jstkT1.npy')
    imgAr = np.load('imageT1.npy')
    print("JoyLength: " + str(len(jstkAr)))
    print("LidarLength: " + str(len(lidarAr)))
    print("image length: "+ str(len(lidarAr)))
    #print()
    #Runs model function to initialize model
    liOut = lidarModel.predict(np.array(lidarAr), batch_size=32, verbose=2)
    #liOut = np.load('liout.npy')
    np.save('lioutT1', liOut)
    #imOut = np.load('imout.npy')
    imOut = imageModel.predict(np.array(imgAr), batch_size=32, verbose=2)
    np.save('imoutT1', imOut)
    #concat = model()
    newInput = []
    count = 1
    for i, d in enumerate(liOut):
        #print(count)
        count += 1
        #print(imOut[i][0])
        #print(liOut[i][0])
        newInput.append([imOut[i][0], liOut[i][0]])
    # print(newInput)
    #Trains model with the function
    concat = keras.models.load_model('concatNet.h5')
    trModel = trainModel(concat, np.array(newInput), np.array(jstkAr))
    #testModel(trModel, testX, testY)

main()
