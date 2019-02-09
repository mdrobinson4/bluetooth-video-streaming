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
                camera, rawCapture = initCamera(resolution, frameRate)
        except:
            print ("Error Initializing Camera")

        sock = connectToServer(bd_addr, port) # connect to the server
        if (sock == 0):
            return
  	# sendImageStream(sock)

      
        sock.send("hello!!")  # send sample message
        sock.close()  # close socket
  
def initCamera(resolution, frameRate):
        try:
                camera = PiCamera()
        except:
                print("THERE WAS AN ERROR")
                return
        camera.resolution = (resolution[0], resolution[1])
        camera.framerate = frameRate
        rawCapture = PiRGBArray(camera, size=(resolution[0], resolution[1]))
        time.sleep(0.1)
        return camera, rawCapture

def connectToServer(address, port):
        sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
        try:
            sock.connect((address, port))
        except:
            print("Unable to connect to server")
            sock = 0
        return sock

def sendImageStream(socket):
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		# grab the raw NumPy array representing the image, then initialize the timestamp
		# and occupied/unoccupied text
		image = frame.array

		# show the frame
		# cv2.imshow("Video Stream", image)
		key = cv2.waitKey(1) & 0xFF

		# clear the stream in preparation for the next frame
		rawCapture.truncate(0)
		socket.send(image)
  
if __name__== "__main__":
  	main()
