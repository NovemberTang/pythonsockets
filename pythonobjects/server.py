import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 4571))

    python_dictionary = {'a': 1, 'b': 2}

    custom_object = Product(1, 'iPhone', 1000)

    s.listen()

    print('Server is listening...')
    client, addr = s.accept()
    print(f'Connected to {addr}')
    print(f'Client: {client}')
    
    pickle_dict = pickle.dumps(python_dictionary)
    pickle_obj = pickle.dumps(custom_object)

    print('Type of pickle_dict', type(pickle_dict))
    print('Type of pickle_obj', type(pickle_obj))

    client.send(pickle_dict)
    client.send(pickle_obj)