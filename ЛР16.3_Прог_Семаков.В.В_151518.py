from collections import deque

def addInQueue(Q):
    """
    Добавление чисел в очередь
    """
    print("Введите последовательность")
    NUM = 0
    while not(str(NUM).isdigit()):
        NUM = int(input())
        Q.append(NUM)
    return Q

def sortQueue(Q1, Q2):
    """
    Объединение, сортировка, печать очередей
    """
    QLAST = list(Q1 + Q2)
    QLAST.sort()
    QLAST = deque(QLAST)
    print(QLAST)

q1 = deque()
q2 = deque()

q1 = addInQueue(q1)
q2 = addInQueue(q2)
sortQueue(q1, q2)


