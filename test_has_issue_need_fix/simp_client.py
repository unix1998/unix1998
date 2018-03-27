import socket
import sys
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 19999

# connection to hostname on the port.
try:
   s.connect(('10.77.8.14', port))
   # Receive no more than 1024 bytes
   msg = s.recv(1024)
   print (" connection successful")
except socket.error as e:
    print("Cannot connect to ")
    print(host," on port: ",str(port))
    print(e)
s.close()

print (msg.decode('ascii'))
