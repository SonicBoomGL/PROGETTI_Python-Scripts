import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

# Crea un oggetto socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Collega il server all'indirizzo IP e alla porta
server.bind((bind_ip, bind_port))

# Mette il server in ascolto
server.listen(5)
print(f"[*] Listening on {bind_ip}:{bind_port}")

# Funzione per gestire le connessioni dei client
def handle_client(client_socket):
    # Riceve i dati inviati dal client
    request = client_socket.recv(1024)
    print(f"[*] Received: {request.decode()}")

    # Invia una risposta al client
    client_socket.send(b"ACK!")
    client_socket.close()

while True:
    # Accetta una connessione
    client, addr = server.accept()
    print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

    # Crea un thread per gestire il client
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
