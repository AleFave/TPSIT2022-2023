from socket import socket, SOCK_STREAM, AF_INET

indirizzoLeggi = ("0.0.0.0", 6000)

def leggi_file(): #funzione per leggere i dati da file (errori nello split)
    f = open("confclient.txt", "r")
    righe = f.read()
    indirizzo, porta = righe.split(";")
    int(porta)
    print(indirizzo, porta)
    return indirizzo, porta

def chat_client():
    #indirizzo, porta = leggi_file()
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(("127.0.0.1",5000))
        running = True
        while running:
            messaggio = "vuoto"
            messaggio = input("Inserisci il messaggio (salva, leggi o fine): ")
            if messaggio == "salva":
                nome = input ("inserisci il nome utente: ") 
                msg = input("inserisci il messaggio: ")
                messaggio = nome + " "+ msg
                print(messaggio)
                s.send(messaggio.encode())
            elif messaggio == "leggi":
                s.send(messaggio.encode())
                with socket(AF_INET, SOCK_STREAM) as sock: #nuovo socket per ricevere l'ultimo messaggio dal server
                    sock.bind(indirizzoLeggi)
                    sock.listen()
                    client, client_address = sock.accept()
                    msg = client.recv(4096)
                    msg = msg.decode('utf-8')
                    print(msg)
            elif messaggio == "fine":
                s.send(messaggio.encode())
                print("Programma stoppato")
                running = False


            

if __name__ == "__main__":
    chat_client()