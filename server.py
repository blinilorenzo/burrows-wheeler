import socket
from bwt import calcola_bwt

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    server.bind(("127.0.0.1", 5000))

    server.listen()

    print("Server in ascolto...")
    print("Socket di ascolto:", server.getsockname())

    conn, addr = server.accept()

    with conn:
        print("Client connesso:", addr)

        dati = conn.recv(1024)
        testo = dati.decode()
        print("Testo ricevuto:", testo)

        if "$" in testo:
            risposta = "ERRORE: il testo non può contenere il simbolo del dollaro"
        else:
            risposta = calcola_bwt(testo)

        print("Risposta inviata:", risposta)

        conn.sendall(risposta.encode())