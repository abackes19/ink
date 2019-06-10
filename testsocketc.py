# Import socket module
import socket

# Create a socket object
s = socket.socket()

x = 87


# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('192.168.21.135', port))
s.sendall(x)


# receive data from the server
print s.recv(1024)
# close the connection
s.close()
