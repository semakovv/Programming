# from collections import deque

# def addInQueue(NUMS, Q):
#     """
#     Добавление чисел в очередь
#     """
#     for i in NUMS:
#         Q.append(int(i))
#     return Q

# def sortQueue(Q1, Q2):
#     """
#     Объединение, сортировка, печать очередей
#     """
#     QLAST = list(Q1 + Q2)
#     QLAST.sort()
#     QLAST = deque(QLAST)
#     print(QLAST)

# q1 = deque()
# q2 = deque()
# nums1 = input()
# nums2 = input()

# q1 = addInQueue(nums1, q1)
# q2 = addInQueue(nums2, q2)
# sortQueue(q1, q2)

from collections import deque

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


