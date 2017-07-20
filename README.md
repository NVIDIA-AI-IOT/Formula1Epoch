  [![title.png](https://s22.postimg.org/w9sb0vysh/title.png)](https://postimg.org/image/bpnh2ej19/)

During a fire, or other emergency, the Formula 1 Epoch R.C. car can be deployed to drive autonomously around a building and account for people still left in a building. The code included was deployed on the Jetson TX1 and TX2 on the racecar below:

  ![car.png](https://augustt198.github.io/bwsi-report/assets/img/racecar_hardware.png)

The models and code can be generalized to work on other platforms.

# PeopleNet
We created a neural network using Caffe and DIGITS on an Nvidia Tesla P40 and Quadro GPU on a standard Ubuntu host. We strongly recommend using 2 Days to a Demo, or 2D2AD, as shown in the below link to get started with the platform. 
The network is built upon DetectNet and a GoogLeNet base on the DIGITS platform using leg/person data, and can be deployed through the detectnet-camera script in the jetson-inference repository.
https://github.com/dusty-nv/jetson-inference

# SteerNet
We've created code for steering a robot based on solely visual recognition to train our RC Car robot. This is based off of the DIY Donkey Car steering code at this link: https://wroscoe.github.io/keras-lane-following-autopilot.html
We use a basic Neural Network consisting of 3 Convolutional Layers and 1 Fully Connected Layer with a single linear output that correlates to steering. The image is the input.
THe model here is built in Keras, a platform built upon a Tensorflow backend.

