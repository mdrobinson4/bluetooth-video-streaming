# bluetooth-video-streaming
Stream webcam video between two raspberry pi's

## openCV dependencies:
* sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev<br/>
* sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev<br/>
* sudo apt-get install libxvidcore-dev libx264-dev<br/>
* sudo apt-get install qt4-dev-tools<br/>
* sudo apt-get install libatlas-base-dev
* sudo apt-get install libhdf5-dev
* sudo apt-get install libhdf5-serial-dev
* sudo apt-get install libatlas-dev


## Install openCV:
* pip3 install opencv-python

## Bluetooth Terminal Commands:
* __List Bluetooth Adaptors:__ hciconfig
* __Scan for Bluetooth devices:__ hcitool scan
* __Make Device Discoverable:__ sudo hciconfig hci0 piscan


__*installation source:__ https://www.youtube.com/watch?v=npZ-8Nj1YwY
