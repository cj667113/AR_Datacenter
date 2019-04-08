# Description
This project was an attempt to build an AR datacenter, so that the administrators need not log into every device to observe data about devices in their environments. Rather, the idea was to augment the administrator's reality in such a way that device data could readibly be seen to the administrators.

This is built off of aframe.io, utilizing javascript plugin and A-frames to create augmented reality. In my project, I set out to-do a few more things on top of this, which was to create a Python script to pull data out of PRTG (network monitor), so that data could be saved into an A-Frame <a-text> with the real-time data. This would allow me to load the new html text tag into the A-Frame object into a real-time fasion to update the data being displayed on the front-end.

# Idea Map
<img src="https://github.com/cj667113/AR_Datacenter/blob/master/Photos/AR_Setup.jpg" height="60%" width="50%">

<img src="https://github.com/cj667113/AR_Datacenter/blob/master/Photos/marker-LoPRTS.png" height="35%" width="50%"><img src="https://github.com/cj667113/AR_Datacenter/blob/master/Photos/AR_LoPRTS.png" height="35%" width="50%">

# Setup steps
The first step is to setup a PRTG server to collect data from devices on the network. For every device that is generating data to PRTG there is a sensor ID that corrosponds. Utilizing this ID, we can plug it into the Python script along with the channel name to pull out the data in real-time and generate A-text tags that can be used.

The next step is to create a server with SSL/TLS encryption with a valid certificate. This is needed to be able to initialize the camera on that webpage through javascript. There are many tutorials to do this, but I heavily recommend using the one from Digital Ocean.
