import bluetooth

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

def main():
    resolution = [640, 480] # resolution of camera
    frameRate = 32

    bd_addr = "B8:27:EB:DC:E7:05"
    port = 0x1001 # default bluetooth port, on client

    try:
        socket = connectToServer(bd_addr, port) # connect to the server
    except:
        print ("Unable To Connect To Server")
        return

    try:
        camera, rawCapture = initCamera(resolution, frameRate)
        sendImageStream(socket, camera) # Send image stream to server
    except:
        print ("Error Initializing Camera, Sending Message Instead")
        socket.send("Hello World!!") # Send message to server

    sock.close()  # close socket
  
def initCamera(resolution, frameRate):
    camera = PiCamera()
    camera.resolution = (resolution[0], resolution[1])
    camera.framerate = frameRate
    rawCapture = PiRGBArray(camera, size=(resolution[0], resolution[1]))
    time.sleep(0.1)
    return camera, rawCapture

def connectToServer(address, port):
    socket = bluetooth.BluetoothSocket(bluetooth.L2CAP)
    socket.connect((address, port))
    return socket

def sendImageStream(socket, camera, rawCapture):
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image,
        # then initialize the timestamp
	# and occupied/unoccupied text
        image = frame.array
	# show the frame
    	# cv2.imshow("Video Stream", image)
        key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        socket.send(image)
  
if __name__ == "__main__":
  	main()
