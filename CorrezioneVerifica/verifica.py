import sys
from socket import AF_INET, SOCK_STREAM, socket
BUFF_SIZE = 4096
class Opzioni:
    def __init__(self, portaServer, host, porta):
        self.portaServer = portaServer
        self.host = host
        self.porta = porta

    def get_socket(self):
        return self.host, self.porta
    
def richiediDati(sock, percorso):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(sock)
        s.sendall(f"GET {percorso}.json HTTP/1.0\n\n".encode())
        data =  True
        dati = []
        while data != None:
            data = s.recv(BUFF_SIZE)
            if data != None:
                dati.append(data)
        dati = b''.join(dati)
        return dati
    
def main(args):
    opt = Opzioni(args[1], args[2], args[3])
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0", int(opt.portaServer)))
        s.listen() 
        while True:
            client, client_address = s.accept()
            data = client.recv(BUFF_SIZE)
            data = data.decode()
            campi = data.split(" ")
            dati = richiediDati(opt.get_socket, campi[1])
            client.sendall(dati)

if __name__ == "__main__":
    main(sys.argv)