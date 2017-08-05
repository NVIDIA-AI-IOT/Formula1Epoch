[![logo.png](https://s2.postimg.org/fwiu26nmh/Copy_of_electron.png)](https://postimg.org/image/sb5m2if4l/)

Repository for the Formula 1 Epoch, or F1Epoch, Team.

## The Problem

### Emergency Applications

The F1Epoch [RACECAR](http://www.jetsonhacks.com/2015/10/06/mit-racecar-walkthrough-nvidia-jetson-tk1/) Robots, **Epoch** and **RaceX**, are deployable in a wide variety of situations that can affect an office environment, from a fire to an earthquake to a furious storm. Meant to replace a fire marshal, these robots will make multiple head count assessments of the building. In essence, it will try to count humans who are still and based on sensors and a timestamp, send a report of the location of the person spotted.

### The Principle Task Explained

The RACECARs are meant to use the principles of deep learning and a few neural networks to drive around given a map of a building and scan for bodies of people. Using an IMU, each person's location relative to the starting point is saved for the use of a rescue team. Using a camera and LIDAR, the RACECARs should learn how to steer and using the camera, should be able to detect people.

  ![car.png](https://augustt198.github.io/bwsi-report/assets/img/racecar_hardware.png)

## The (Proposed) Solution

### Hardware Requirements

For **Epoch** and **RaceX**, we used a NVIDIA Jetson TX1 and TX2, respectively, for reliable edge processing of our multiple neural networks. On each RACECAR we have a [Logitech C720 webcam](https://www.logitech.com/en-us/product/hd-webcam-c270), which replaced the ZED camera that originally came with the RACECARs, used for stereo vision. We also have a [RPLidar](http://www.slamtec.com/en/lidar/a1) and a [Sparkfun 9DOF Razor IMU](https://www.sparkfun.com/products/14001) on each of the robots. We had to reconfigure the kernels to accomodate all the USB ports. We used < and info about hardware of car itself >

### Software Requirements

For both cars, we flashed the Jetsons with [Jetpack](https://developer.nvidia.com/embedded/jetpack). This should install most or all of the C++ dependencies you require for the project (Note: flashing requires an external Ubuntu host machine). Ensure that you have CUDA, the proper GPU driver installations, etc. by following [https://github.com/dusty-nv/jetson-inference](https://github.com/dusty-nv/jetson-inference).

For many of the Python dependencies and drivers for the various parts of the robot, we strongly suggest you check out JetsonHacks.com for simple scripts and tutorials for installation. ROS, or Robot Operating System, is something that can be very finicky to handle at first even though it's a brilliant tool for controlling the car - JetsonHacks even has scripts for that! 

For much of our code pertaining to our PeopleNet - detecting people - we sought help from jetson-inference, a directory created by Dustin Franklin, which you can check out at [https://github.com/dusty-nv/jetson-inference](https://github.com/dusty-nv/jetson-inference). We forked and modified his code to suit our needs for PeopleNet.

### Software Process

We have a navigation network that generates a map using a custom recursive backtracking we created in Python. 

Our PeopleNet was built in C++ with the help of [https://github.com/dusty-nv/jetson-inference "jetson-inference"](https://github.com/dusty-nv/jetson-inference), using the Caffe + DIGITS neural network libraries to train a network on an external GPU server and then deploy it on our Jetsons. We used the DetectNet framework with GoogLeNet weights, compiled with our own self-labeled people images to train.

Our SteerNet - turns the robot at the appropriate time - runs in a separate process in python using Keras a user friendly neural network training library, built on top of a Tensorflow backend. It trains on a GPU server using training data that comprises of image and LiDAR inputs and a joystick output for controlling the steering. We're seeking to get around 40,000 total training samples for training.

## Get Started

### Check out Dusty-NV, jetson-inference, 2 Days to a Demo, and the deployment of models you might create.

[https://github.com/dusty-nv/jetson-inference](https://github.com/dusty-nv/jetson-inference)

### Check out Keras and the usage of SteerNet in DonkeyCar

[https://github.com/fchollet/keras](https://github.com/fchollet/keras)
[https://wroscoe.github.io/keras-lane-following-autopilot.html](https://wroscoe.github.io/keras-lane-following-autopilot.html)

### Check out JetsonHacks for all things installation and configuration

[http://www.jetsonhacks.com/](http://www.jetsonhacks.com/)
[http://www.github.com/jetsonhacks](http://www.github.com/jetsonhacks)

#### Lastly, post issues if there's any further basic guidance you need or something that we've missed!
