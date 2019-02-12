import bluetooth

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

def main():
    port = 0x1001 # select first bluetooth adapter on server

    serverSocket = openSocket(port) # open server socket
    serverSocket.listen(1)  # listen for the client's connection request

    clientSocket, address = serverSocket.accept() # allow the client to connect
    print("Accepted Connection From: ", address)

    data = clientSocket.recv(1024)  # get the data from the client
    print ("received [%s]" % data)

    clientSocket.close()  # close the client socket
    serverSocket.close()  # close the server socket

def openSocket(port):
    serverSocket = bluetooth.BluetoothSocket(bluetooth.L2CAP) 
    # create bluetooth object and set 
    # l2cap (udp) as the transportation service
    serverSocket.bind(("", port)) # bind to default bluetooth adapter on server
    return serverSocket

main()
