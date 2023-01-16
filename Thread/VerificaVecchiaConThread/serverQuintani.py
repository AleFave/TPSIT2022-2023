from socket import socket, AF_INET, SOCK_STREAM
import threading

indirizzoLeggi = ("127.0.0.1", 6000)

def invio_msg(messaggio):
    with socket(AF_INET, SOCK_STREAM) as s: #creo un socket per inviare il messaggio pi recente
        s.connect(indirizzoLeggi)
        s.send(messaggio.encode())
        print("mandato")

def leggi_file(): #funzione per leggere i dati da file (non mi splitta)
    f = open("confserver.txt", "r")
    righe = f.read()
    indirizzo, porta = righe.split(";")
    int(porta)
    print(indirizzo, porta)
    return indirizzo, porta

def chat_server():
    messsaggi = []
    indirizzo, porta = leggi_file()
    print(indirizzo, porta)
    with socket(AF_INET, SOCK_STREAM) as s:
        
        s.bind(("0.0.0.0", 5000)) #I parametri indirizzo e porta non collabora, quindi uso la forza bruta
        s.listen()
        client, client_address = s.accept()
        running = True
        while running:
            msg = client.recv(4096)
            msg = msg.decode('utf-8')
            messsaggi.append(msg)
            print(messsaggi[-1])
            if msg == "leggi":
                mes = messsaggi[0]
                t = threading.Thread(target=invio_msg, args=(mes))
                t.start()
                t.join()
            elif msg == "fine":
                print("server sospeso")
                running = False


if __name__ == "__main__":
    chat_server()