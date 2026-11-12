import socket
from bwt import inverti_bwt

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    client.connect(("127.0.0.1", 5000))

    testo = input("Inserisci un testo: ")
    client.sendall(testo.encode())

    risposta = client.recv(1024).decode()

    if "$" in risposta:
        print("BWT ricevuta dal server:", risposta)

        originale = inverti_bwt(risposta)
        print("Testo ricostruito:", originale)
    else:
        print("Risposta del server:", risposta)