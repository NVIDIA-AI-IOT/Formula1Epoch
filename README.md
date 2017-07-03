# Formula1Epoch
Repository for the Formula 1 Epoch Team.

# PeopleNet
We created a neural network using Caffe and DIGITS on an Nvidia Tesla P40 and Quadro GPU on a standard Ubuntu host. We strongly recommend using 2 Days to a Demo, or 2D2AD, as shown in the below link to get started with the platform. 
The network is built upon DetectNet and a GoogLeNet base on the DIGITS platform using leg/person data, and can be deployed through the detectnet-camera script in the jetson-inference repository.
https://github.com/dusty-nv/jetson-inference

# SteerNet
We've created code for steering a robot based on solely visual recognition to train our RC Car robot. This is based off of the DIY Donkey Car steering code at this link: https://wroscoe.github.io/keras-lane-following-autopilot.html
We use a basic Neural Network consisting of 3 Convolutional Layers and 1 Fully Connected Layer with a single linear output that correlates to steering. The image is the input.
THe model here is built in Keras, a platform built upon a Tensorflow backend.
