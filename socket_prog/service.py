"""
1. get the hostname, port
2. form the url based on the hostname and port number
3. wait for the client request
4. if the client sends any request, 
	then need to accept that request and process the request, 
	send response back to the client
"""


import socket
port=8889
hostname=socket.gethostname()
try:
	s=socket.socket() # tcp ipv4
	print s
	s.bind((hostname, port))
	while True:
		s.listen(30)
		print "running on %s:%s"%(hostname,port)
		#print s.accept()
		client_sockt, client_info = s.accept()
		client_sockt.send("hello firefox, how are you doing??")
		req_data = client_sockt.recv(1024)
		if int(req_data)%2==0:
			resp="EVEN"
		else:
			resp="ODD"
		client_sockt.send(resp)

except Exception as err:
	print err
finally:
	s.close()