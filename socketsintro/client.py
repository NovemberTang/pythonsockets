import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 4571))

message = s.recv(1024) #1024 is the buffer size. It's the max amount of data that can be received at once
print(message.decode('utf-8')) #decode the message from bytes to string

s.close()
