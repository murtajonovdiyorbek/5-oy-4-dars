from threading import Thread

def katta(values):
    
    result = []
    
    for i in ism:
        result.append(i.capitalize())
    print(result)

ism = ['teshavoy', 'baltavoy', 'ali', 'vali']

th = Thread(target=katta, args=(ism,))
th.start()
th.join()