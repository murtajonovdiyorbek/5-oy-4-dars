from threading import Thread

def harf(text):
    i = 0
    matn = ""
    while i < len(text):
        if text[i] == 'e':
            matn += '3'
        else:
            matn += text[i]
        i += 1
    print(matn)

text = input("text kiriting: ")

th = Thread(target=harf, args=(text,))
th.start()
th.join()