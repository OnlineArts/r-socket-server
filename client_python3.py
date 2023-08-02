#!/usr/bin/env python3
import socket

msg = input("Message:\n")

while msg != "q" or msg != "q":
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(("localhost", 6011))

	msg_str = "%s\n" % msg
	client_socket.sendall(msg_str.encode())
	ans = client_socket.recv(50)
	print("Your upper cased text: %s" % ans.decode('utf8') )
	msg = input("Message: \n")

	client_socket.close()


#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#	s.connect(("localhost", 6011))
#	s.sendall(b"Hallo!")
#	data = s.recv(1024)
#print("recieved", repr(data))