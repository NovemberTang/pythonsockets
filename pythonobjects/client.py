import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 4571))

    while True:
        data = s.recv(1024)
        if not data:
            print('No data received from server')
            break
        print('Type of data received from server',type(data))
        unpickled_data = pickle.loads(data)
        print('Data received from server',unpickled_data)
        print('Type of deserialized data',type(unpickled_data))
        print('-----------------------------------')
