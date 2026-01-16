from threading import Thread

def soz(words):
    result = []
    
    for i in words:
        if i.lower() == i.lower()[::-1]:
            result.append(i)
    
    print(result)

sozlar = ['Amma', 'Alla', 'Kazak', 'Dom', 'Lol']

th = Thread(target=soz, args=(sozlar,))
th.start()
th.join()