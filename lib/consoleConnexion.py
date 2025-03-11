import socket
import sys

def console_connexion(host="127.0.0.1", consolePort=58591, playerCount=1):
    """
    Connecte le client à la console avec le nombre de joueurs spécifié.

    :param host: Adresse IP du serveur
    :param consolePort: Port de la console
    :param playerCount: Nombre de joueurs
    :return: L'objet clientSocket
    """
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((host, consolePort))
        clientSocket.sendall(f"Jeu 1 démarré avec {playerCount} joueur(s)".encode())
        return clientSocket
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        return None
