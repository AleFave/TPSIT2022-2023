
from socket import AF_INET, SOCK_DGRAM, SOCK_RDM, socket

def chatClient():
    with socket(AF_INET, SOCK_DGRAM) as s:
        PORT = int(input("\nInserisci la porta (consigliato 5000) "))
        while True:
            msg = input("Inserisci il messaggio da inviare: ")
            msg = msg.encode('utf8')

            s.sendto(msg, ("192.168.0.255", PORT)) #.255 perchè è il broadcast + inserire proprio IP

if __name__ == "__main__":
    chatClient()