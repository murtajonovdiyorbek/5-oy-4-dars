from threading import Thread

def bosh(values):
    i = 0
    matn = ""
    
    while i < len(values):
        if values[i] != ' ':
            matn += values[i]
        i += 1
    
    print(matn)

text = input("matn kiriting... ")

th = Thread(target=bosh, args=(text,))
th.start()
th.join()