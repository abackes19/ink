# Import socket module
import socket

# Create a socket object
s = socket.socket()

x = 87
y = 92


# Define the port on which you want to connect
port = 2197

# connect to the server on local computer
# first number if on computer: 127.0.0.1
# if on pi: 192.168.21.xxx, xxx being the chip #
s.connect(('127.0.0.1', port))
s.send("%i" % x)
s.send("%i" % y)


# receive data from the server
print s.recv(1024)
# close the connection
s.close()
