import threading 
from lancio import Lancio
def main():
    for i in range (1000):
        thread1 = Lancio("prova 1") 
        thread1.start()

if __name__ == "__main__":
    main()