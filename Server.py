import sys
import os
import socket


### Server

port = 49999
buffer_size = 1024
host = '127.0.0.1'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))

s.listen()

print("Waiting...")
c, addr = s.accept()
print("Finished")


print("Got connection from" + str(addr))
test_string = "Established Connection"
test_arr = bytearray(test_string, "utf-8")
c.send(test_arr)
filename_input = input("Enter the path of your file: ")

### user selected file
while(not (os.path.isfile(filename_input))):
	print("Invalid Text File")
	filename_input = input("Enter the path of your file: ")

f = open(filename_input,"r",encoding='utf-8')

### sending lines into the socket from the file
for line in f:
	send_arr = line.encode(encoding= 'UTF-8', errors= 'strict')
	c.send(send_arr)
	rec = c.recv(3)
	recDecode = rec.decode("utf-8","strict")
	while(recDecode != "ACK"):
		c.send(send_arr)
		rec = c.recv(3)
		recDecode = rec.decode("utf-8","strict")

print("Closing Server Side")
c.close()