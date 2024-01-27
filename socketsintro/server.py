import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 4571)) #or localhost
s.listen(5) # will accept 5 connections before rejecting others

print('Server is listening for connections')

client, address = s.accept() #blocks the process until a connection is made
print(f'Connection from {address} has been established\n')
print(f'Client object: {client}\n')
client.send(bytes('Welcome to my server', 'utf-8'))

s.close()
