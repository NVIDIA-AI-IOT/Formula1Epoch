#import tensorflow as tf
import numpy as np
#import matplotlib
#from matplotlib.pyplot import imshow
from keras.models import Model, load_model, Sequential
from keras.optimizers import Adam
from keras.layers import Input,Convolution2D, Convolution1D, MaxPooling2D, Activation, Dropout, Flatten, Dense
import cv2
import helperFunctions
from keras.utils import plot_model
from keras import regularizers
from keras.callbacks import CSVLogger
csv = CSVLogger('SteerNetSimple.csv', separator='\n', append=True)

def model():
    #Model with 3 hidden layers
    #Input takes in image
    lid = Input(shape = (1, 167), name = 'lid')
    x = Convolution1D(8, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(16, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(32, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(64, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(128, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(256, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(512, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    x = Convolution1D(1024, 2)(lid)
    x = Activation('relu')(x)
    x = MaxPooling1D(pool_size=(2))(x)

    merged = Flatten()(x)

    x = Dense(128)(merged)
    x = Activation('linear')(x)
    x = Dropout(.3)(x)

    jstk = Dense(1, name='jstk')(x)

    net = Model(input=[lid], output=[jstk])
    net.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
    print(net.summary())
    return net


def trainModel(model, lidarIn, jstkOut):
    #Trains predefined model with verbose logging, input image data and output steering data
    csv = CSVLogger('SteerNetL2SGD.csv', separator='\n', append=True)
    model.fit(x=lidarIn, y=jstkOut, batch_size=32, epochs=250, verbose=2, callbacks=[csv], validation_split=0.2, shuffle=True, initial_epoch=0)
    modelName = 'lidarNet'
    modelPng = modelName + ".png"
    modelName = modelName + ".h5"
    #Plots the trained model
    #plot_model(steerNet, to_file=modelPng)
    model.save(modelName)
    print("Saved as %s" %(modelName) )
    return model

def testModel(model, testX, testY):
    # Test model and evauluate accuracy, prints it
    scores = model.evaluate(testX, testY)
    print("\nAccuracy: " + model.metrics_name[1], scores[1]*100)

def main():
    #Main Function, starts with path inputs
    #imagePath = raw_input("Please enter the filepath to your images folder")
    #labelPath = raw_input("Please enter the filepath to your labels folder")
    #Uses helper functions to get array of images and outputs
    lidarAr = helperFunctions.parseLidarData('/media/ricky/ZED/data/scandata.txt', '/media/ricky/ZED/data/timestamp.txt')
    jstkAr = helperFunctions.mapImageToJoy('/media/ricky/ZED/data/joydata.txt', '/media/ricky/ZED/data/timestamp.txt')

    print("JoyLength: " + str(len(jstkAr)))
    print("LidarLength: " + str(len(lidarAr)))
    #print()
    #Runs model function to initialize model
    steerModel = model()
    #Trains model with the function
    trModel = trainModel(steerModel, lidarAr, jstkAr)

main()
