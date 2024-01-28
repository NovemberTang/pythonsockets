import socket
from product import Product

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 4571))

    while True:
        data = s.recv(1024)
        if not data:
            print('No data received from server')
            break
        print('Message from server',data.decode('utf-8'))
        print('Type of data received from server',type(data))
