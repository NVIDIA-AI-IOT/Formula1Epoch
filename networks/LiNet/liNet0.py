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

def model():
    #Model with 3 hidden layers
    #Input takes    img = Input(shape = (167, 54), name = 'img')
    #Convolution/Pooling Layer 1
    lid = Input(shape = (360, 3), name = 'lid')

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

    merged = Flatten()(lid)

    x = Dense(64)(merged)
    x = Activation('relu')(x)
    x = Dropout(.3)(x)

    x = Dense(32)(x)
    x = Activation('relu')(x)
    x = Dropout(.3)(x)

    x = Dense(128)(x)
    x = Activation('relu')(x)
    x = Dropout(.3)(x)

    x = Dense(40)(x)
    x = Activation('tanh')(x)
    x = Dropout(.3)(x)

    jstk = Dense(1, name='jstk')(x)

    net = Model(input=[lid], output=[jstk])
    net.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
    print(net.summary())
    return net

def trainModel(model, imgIn, jstkOut):
    #Trains predefined model with verbose logging, input image data and output steering data
    print(jstkOut)
    model.fit(x=imgIn, y=jstkOut, batch_size=32, epochs=160, verbose=2, callbacks=None, validation_split=0.2, shuffle=True, initial_epoch=0)
    modelName = 'linetnext'
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
    lidarAr = helperFunctions.parseLidarData('/media/first/UBUNTU/lidardata.txt', '/media/first/UBUNTU/timestamp.txt')
    jstkAr = helperFunctions.mapImageToJoy('/media/first/UBUNTU/joydata.txt', '/media/first/UBUNTU/timestamp.txt')

    print("JoyLength: " + str(len(jstkAr)))
    print("LidarLength: " + str(len(lidarAr)))
    #print()
    #Runs model function to initialize model
    steerModel = model()
    #Trains model with the function
    '''for i,d in enumerate jstkAr:
        jstkAr[i] = 100 * jstkAr[i]'''
    trModel = trainModel(steerModel, lidarAr, jstkAr*100)
    #testModel(trModel, testX, testY)

main()
