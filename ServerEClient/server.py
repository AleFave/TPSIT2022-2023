from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE = 1024 #Definisco il numero di byte che voglio leggere ogni volta
mystr = "ciao"

#In python le stringhe si chiamano str, non sono array di byte, con l'istruzione bytes converto la stringa in byte
#Posso usare encode e decode per convertire in byte e non byte

#Possibilità host:
    #Localhost: 127.0.0.1
    #Interfaccia particolare
    #Ascoltare dati da qualsiasi interfaccia (0.0.0.0)
file = open("frasi.csv", "a")

def chatServer():
    #In questo modo apro un oggetto socket chiamato s, questo s si usa solo nel blocco with, una volta usciti da with chiudo automaticamente la risorsa
    with socket(AF_INET, SOCK_DGRAM) as s: #AF_INET = Definisce che uso IP di v4 (IPv4), SOCK_DGRAM si usa per inviare pacchetti
        HOST = "0.0.0.0"
        PORT = int(input("\nInserisci la porta (consigliato 5000) "))
        print("\nServer in ascolto")
        s.bind((HOST,PORT)) #bind ci mette in ascolto
        
        while True:
            msg = s.recvfrom(BUFFER_SIZE) #recvfrom fa in modo che la variabile riceva il messaggio
            msg = msg[0].decode('utf8')
            print(msg)
            file = open("frasi.csv", "a")
            file.write(msg+"\n")
            file.close()

if __name__ == "__main__":
    chatServer()