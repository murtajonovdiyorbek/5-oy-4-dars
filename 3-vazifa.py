from threading import Thread

def baho(values):
    result = []
    for i in values:
        if i > 75:
            result.append(i)
    print(result)

baholar = [23, 89, 33, 59, 76, 61, 88, 78, 93, 69]

th = Thread(target=baho, args=(baholar,))
th.start()
th.join()