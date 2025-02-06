import socket

target_host = "www.google.com"
target_port = 80

# Crea un oggetto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connette il client al server
client.connect((target_host, target_port))

# Invia una richiesta HTTP
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Riceve la risposta
response = client.recv(4096)

print(response.decode())
client.close()
