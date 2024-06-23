import socket
import threading
from key_utils import generate_rsa_keys, serialize_public_key, deserialize_public_key, encrypt_with_rsa, decrypt_with_rsa, generate_aes_key, encrypt_with_aes, decrypt_with_aes

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket.bind(('localhost', 40623))
server_socket.bind(('192.168.86.33', 40623))
server_socket.listen(5)
print("Server listening on port 40623")

private_key, public_key = generate_rsa_keys()

clients = []

def handle_client(client_socket):
    global clients
    client_public_key = deserialize_public_key(client_socket.recv(1024))
    client_socket.send(serialize_public_key(public_key))
    
    # Secure AES key exchange
    aes_key = generate_aes_key()
    encrypted_aes_key = encrypt_with_rsa(client_public_key, aes_key)
    client_socket.send(encrypted_aes_key)
    
    clients.append((client_socket, aes_key))
    
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            for c, k in clients:
                if c != client_socket:
                    decrypted_data = decrypt_with_aes(aes_key, data)
                    encrypted_data = encrypt_with_aes(k, decrypted_data)
                    c.send(encrypted_data)
        except:
            break
    
    client_socket.close()
    clients.remove((client_socket, aes_key))

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()

