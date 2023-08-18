import socket

host = input("Enter Server address: ")
port = int(input("Enter Port: "))

# Creating socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connecting with server
s.connect((host, port))
print("connected")

# Receiving data from server.  Since both server and client have data in byte format, we hav>
recv = s.recv(1024).decode()

print("server -->",recv)
s.close()

