from collections import Counter as cnt
from collections import deque

l = [0, -1, 2, 1, 1]
print(cnt(l))

def addInQueue(Q):
    """
    Добавление чисел в очередь
    """
    print("Введите последовательность чисел")
    ST = input()
    while ST != "stop":
        Q.append(int(ST))
        ST = input()
    return Q

d = deque()
d = addInQueue(d)
print(cnt(d))