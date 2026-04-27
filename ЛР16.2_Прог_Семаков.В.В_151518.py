from collections import deque

def calc(op):
    num = 0
    stack = deque()
    while op is not "stop":
        stack.append(op)
        if op[0] is "+":
            num += int(op[1::])
            print(num)

