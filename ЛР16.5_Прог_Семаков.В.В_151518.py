from collections import Counter as cnt
from collections import deque

def addEl(Q):
    """
    Добавление чисел
    """
    print("Введите последовательность чисел")
    ST = input()
    while ST != "stop":
        Q.append(int(ST))
        ST = input()
    return Q

def searchMinElCnt(DATA):
    """
    Поиск элемента, который реже встречается
    """
    countSave = 9999999
    keySave = 0
    countEl = cnt(DATA)
    for i in countEl:
        if countEl[i] < countSave:
            keySave = i
    return keySave

l = list()
d = deque()
l = addEl(l)
d = addEl(d)

print(searchMinElCnt(l))
print(searchMinElCnt(d))