import socket
from product import Product

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 4571))

    python_dictionary = {'a': 1, 'b': 2}

    custom_object = Product(1, 'iPhone', 1000)

    s.listen()

    print('Server is listening...')
    client, addr = s.accept()
    print(f'Connected to {addr}')
    print(f'Client: {client}')
    
    client.send(bytes(str(python_dictionary), 'utf-8'))
    client.send(bytes(str(custom_object), 'utf-8'))