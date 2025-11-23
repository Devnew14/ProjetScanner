import socket

ip = "127.0.0.1"
port = 8000


# Exemple de socket
sock = socket.socket()
sock.settimeout(0.2)


# ajout de try , except
try:  
    sock.connect((ip, port))
    print("Port 8000 ouvert !")
except:
    print("Port 8000 fermé.")


#Exemple de port ouvert , pour effectuer un test de scan 