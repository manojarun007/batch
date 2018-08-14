import socket
port=8889
hostname="khyaathipython"
try:
	s=socket.socket()
	s.connect((hostname,port))
	ack = s.recv(1024)
	print "ack=",ack
	s.send(raw_input("Enter a number:"))
	response = s.recv(1024)
	print "response:",response
except Exception as err:
	print err
finally:
	s.close()
