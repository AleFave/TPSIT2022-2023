import threading
import socket
import time

def main():
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        client.connect(("127.0.0.1", 8000))
        op = input("Inserisci operazione aritmetica: ")
        client.sendall(op.encode())
        ans = client.recv(4096).decode()
        print(ans)

if __name__ == "__main__":
    main()