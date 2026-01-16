from threading import Thread

def royxat(values):
    result = []
    for i in values:
        result.append(i * 2)
    print(result)

raqam = [2, 5, 6, 8, 12, 44, 23, 89, 96, 69, 10]

th = Thread(target=royxat, args=(raqam,))
th.start()
th.join()