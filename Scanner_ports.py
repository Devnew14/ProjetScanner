import socket  #module socket qui permet de communiquer sur un réseau 
#pour voir si un port répond ou pas

def scan_port(ip, port):   #on cree une fonciton qui teste un seul port sur une adresse IP
    sock = socket.socket() #on cree un canal de communication 
    sock.settimeout(0.5)  #limite de temps 
    try:
        sock.connect((ip, port))  #tente d'ouvrir une connexion au port demandé 
        sock.close()
        return True  #Si reussie , il envoie True
    except:
        return False

ip = input("IP à scanner : ")

for port in range(1, 1001):  # scan des ports 1 à 100
    if scan_port(ip, port):
        print(f"Port ouvert : {port}")


#Ce script :

# te demande une IP

# teste les ports 1 à 100

# affiche seulement ceux qui répondent

# utilise socket pour essayer de se connecter à chaque port