import socket
import sys
import time
import errno
import os

### Client

###ClientSide.txt - Les Miserables
###clientshort.txt - Compare Old English/Modern English

port = 49999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

server_address = ('127.0.0.1',port)

success = "ACK"
failure = "NAK"
fail_send = failure.encode(encoding= 'UTF-8', errors= 'strict')
success_send = success.encode(encoding= 'UTF-8', errors= 'strict')

s.connect(server_address)

received = s.recv(1024)

recvDecode = received.decode("utf-8","strict")

print(recvDecode)

f = open("ClientSide.txt", "w", encoding='utf-8')

while received != bytearray():
	received = s.recv(9999)
	try:
		recvDecode = received.decode("utf-8","strict")
	except:
		s.send(fail_send)
	else:
		f.write(recvDecode)
		s.send(success_send)

print("Closing Client Side")
s.close()