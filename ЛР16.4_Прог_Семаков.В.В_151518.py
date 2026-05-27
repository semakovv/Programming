from collections import deque

def addInDeque(D):
    """
    Добавление чисел в дек
    """
    print("Введите последовательность чисел")
    ST = input()
    while ST != "stop":
        if int(ST) > 0:
            D.append(int(ST))
            ST = input()
        else:
            D.appendleft(int(ST))
            ST = input()
    return D

d1 = deque()
d1 = addInDeque(d1)
print(d1)