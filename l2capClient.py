
import bluetooth

sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

bd_addr = "B8:27:EB:DC:E7:05"
port = 0x1001

sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
