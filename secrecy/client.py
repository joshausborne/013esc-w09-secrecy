import socket
import threading
from key_utils import generate_rsa_keys, serialize_public_key, deserialize_public_key, encrypt_with_rsa, decrypt_with_rsa, encrypt_with_aes, decrypt_with_aes

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client_socket.connect(('localhost', 40623))
client_socket.connect(('192.168.86.33', 40623))

private_key, public_key = generate_rsa_keys()
client_socket.send(serialize_public_key(public_key))

server_public_key = deserialize_public_key(client_socket.recv(1024))
encrypted_aes_key = client_socket.recv(1024)
aes_key = decrypt_with_rsa(private_key, encrypted_aes_key)

def receive_messages():
    while True:
        data = client_socket.recv(1024)
        if data:
            decrypted_data = decrypt_with_aes(aes_key, data)
            print("Received:", decrypted_data.decode())

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input("Enter message: ")
    encrypted_message = encrypt_with_aes(aes_key, message.encode())
    client_socket.send(encrypted_message)

