# robolidar: 
## Lidar information system, using serial communications.

### Requirements:
Python 3.5.3 or greater. - because we really need to get away from 2.7.x
pip3 - for ease of module installation.
pyserial - interact over a serial connection to the lidar module.

### Possible FRC requirement:
pynetworktables - To speak to smartdashboard from the Raspberry pi. (http://robotpy.readthedocs.io/en/stable/install/pynetworktables.html#install-pynetworktables)

### Installation:
Clone this repo to your local Pi.

### Command example:
    lidar-manager.py -ms 10 -lr 3
###### Options:
    -p /dev/<device serial/usb port>
    -l - LiDAR Info
    -m - Motor Info
    -v - Version Info
    -d - Device Info
    -ms Adjust Motor Speed [1-10]
    -lr Adjust LiDAR Sample Rate [1,2,3]
