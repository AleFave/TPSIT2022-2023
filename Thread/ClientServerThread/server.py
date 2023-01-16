import threading
import socket
import time
def serverFun(conn,address):
    running = True
    while running:

        msg = conn.recv(4096).decode()
        try:
            ris = eval(msg)
            print(ris)
        except:
            print("errore")

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))
    s.listen()
    running = True
    while running:
        conn, address = s.accept()
        t = threading.Thread(target=serverFun, args=(conn,address))
        #t = MyClassThread(conn)
        t.start()

if __name__ == "__main__":
    main()