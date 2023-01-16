import threading
import time

luc = threading.Lock()

def funzione(num):
    print(f"partenza del {num}", threading.current_thread().name)
    print("elabora...")
    time.sleep(2)
    print(f"finito lavoro {num}", threading.current_thread().name)

def main():
    t = threading.Thread(target=funzione, args=(1,), name="Primo") #creazione di un thread, parte subito il metodo run. Il target indica cosa far partire col thread, args passiamo i parametri della funzione. IMPORTANTE LA VIRGOLA
    t.start() # fa partire il thread
    t.join() #controllo i thread, ovvero il programma non va avanti finchè non finisce prima il processo indicato con la join
    q = threading.Thread(target=funzione, args=(2,), name="Secondo")
    q.start()
    q.join()

    funzione(3)
    print("fine chiamata")

if __name__ == "__main__":
    main()