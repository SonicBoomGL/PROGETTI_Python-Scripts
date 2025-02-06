import socket

target_host = "127.0.0.1"
target_port = 80

# Crea un oggetto socket UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Invia dati
client.sendto(b"AAABBBCCC", (target_host, target_port))

# Riceve dati
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
