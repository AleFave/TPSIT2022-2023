def inizioTOfine(func):
    def wrapper():
        print("inizio")
        func()
        print("fine")
    return wrapper

def ciao():
    print("ciao")

ciao = inizioTOfine(ciao)

def hello():
    print("hello")

hello = inizioTOfine(hello)

if __name__ == "__main__":
    ciao()
    hello()
    inizioTOfine()