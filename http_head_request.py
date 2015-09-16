import socket

HOST = 'www.ubuntu.com'
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname(HOST), PORT))
s.sendall('HEAD / HTTP/1.1\r\n')
data = s.recv(10240)
s.close()
print "RECEIVED:\n==============\n", data
