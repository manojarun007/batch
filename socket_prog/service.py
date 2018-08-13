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
s=socket.socket() # tcp ipv4
print s
s.bind((hostname, port))
s.listen(30)
print "running on %s:%s"%(hostname,port)
#print s.accept()
client_sockt, client_info = s.accept()
client_sockt.send("hello firefox, how are you doing??")
s.close()