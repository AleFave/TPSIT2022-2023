import threading 

def inc():
    global var
    for _ in range(10000):
        var += 1

t = []
var = 0
for i in range(1000):
    nome = f"Processo numero {i}"
    t.append(threading.Thread(target=inc, name=nome))
    t[i].start()

for j in range(1000):
    t[j].join()

print(var)