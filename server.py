import socket


host = input("Enter client address: ")
port = int(input("Enter Port: "))


# Creating socket object
# AF_INET --> IpV4
# AF_INET --> IPV6
# SOCK_STREAM --> TCP
# SOCK_STREAM --> UDP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Binding server with localhost
s.bind((host,port))
print("listening")

# Listening for 1 client. For more than 1 client we use threading.
s.listen(1)

# Accepting server request. accept() return socket and a tuple containing remote address and>
client,addr = s.accept()
print("connected")

# sending  data to client. Both client and server receive data in byte format.
client.send(b"Hello Client")
client.close()
server.close()
