from socket import AF_INET, SOCK_DGRAM, SOCK_RDM, socket

PORT = int(input("\nInserisci la porta (consigliato 5000) "))

def chatClient():
    with socket(AF_INET, SOCK_DGRAM) as s:
        while True:
            msg = input("Inserisci il messaggio da inviare: ")
            msg = msg.encode('utf8')

            s.sendto(msg, ("192.168.112.255", PORT)) #.255 perchè è il broadcast + inserire proprio IP

if __name__ == "__main__":
    chatClient()