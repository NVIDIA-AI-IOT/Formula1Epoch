#import tensorflow as tf
import numpy as np
#import matplotlib
#from matplotlib.pyplot import imshow
from keras.models import Model, load_model, Sequential
from keras.optimizers import Adam
from keras.layers import Input, Convolution2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
import cv2
import helperFunctions
from keras.utils import plot_model
from keras import regularizers

from keras.callbacks import CSVLogger

csv = CSVLogger('SteerNetSimple.csv', separator='\n', append=True)

def model():
    #Model with 3 hidden layers
    #Input takes in image
    img = Input(shape = (376, 672, 3), name = 'img')
    #Convolution/Pooling Layer 1
    x = Convolution2D(16, 3, 3, kernel_regularizer=regularizers.l2(0.005))(img)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    #Convolution/Pooling Layer 2
    x = Convolution2D(32, 3, 3, kernel_regularizer=regularizers.l2(0.005))(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    #Convolution/Pooling Layer 3
    x = Convolution2D(32, 3, 3 , kernel_regularizer=regularizers.l2(0.005))(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)

    x = Convolution2D(64, 3, 3 , kernel_regularizer=regularizers.l2(0.005))(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Convolution2D(64, 3, 3 , kernel_regularizer=regularizers.l2(0.005))(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    #Flattens into 1D array for Usage in final layer
    merged = Flatten()(x)
    #One final fully connected layer for figuring output values
    x = Dense(128 , kernel_regularizer=regularizers.l2(0.005), activity_regularizer=regularizers.l2(0.005))(merged)
    x = Activation('linear')(x)
    x = Dropout(.3)(x)
    #Final output
    jstk = Dense(1, name='jstk')(x)
    #Compiled and initializes the model
    steerNet = Model(input=[img], output=[jstk])
    steerNet.compile(optimizer='adam', loss='mean_squared_error')
    print(steerNet.summary())
    return steerNet

def trainModel(model, imgIn, jstkOut):
    #Trains predefined model with verbose logging, input image data and output steering data
    csv = CSVLogger('SteerNetL2Conv163264.csv', separator='\n', append=True)
    model.fit(x=imgIn, y=jstkOut, batch_size=32, epochs=200, verbose=2, callbacks=[csv], validation_split=0.2, shuffle=True, initial_epoch=0)
    modelName = 'SteerNetL2Conv163264'
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
    #Main Function, starts with path inputs
    #imagePath = raw_input("Please enter the filepath to your images folder")
    #labelPath = raw_input("Please enter the filepath to your labels folder")
    #Uses helper functions to get array of images and outputs
    imgAr = helperFunctions.getTrainingData('/media/first/ZED/images/')
    jstkAr = helperFunctions.mapImageToJoy('/media/first/ZED/joydata.txt', '/media/first/ZED/timestamp.txt')
    #Runs model function to initialize model
    steerModel = model()
    #Trains model with the function
    trModel = trainModel(steerModel, imgAr, jstkAr)

main()
