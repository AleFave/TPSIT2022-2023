import threading
import socket
import time

class MyClassThread(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self) # richiamo costruttore della classe genitore, ereditarietà multipla
        self.conn = conn
    
    def run(self):
        while True:

            ricevi = self.conn.recv(4096).decode()
            risp = input("Inserisci una risposta")
            self.conn.sendall(risp.encode())

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))
    s.listen()
    running = True
    while running:
        conn, address = s.accept()
        #t = threading.Thread(target=serverFun, args=(conn,address))
        t = MyClassThread(conn)
        t.start()

if __name__ == "__main__":
    main()