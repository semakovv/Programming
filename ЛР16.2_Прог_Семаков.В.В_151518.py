from collections import deque

stack = deque()
def oper(op = None, num = 0):
    while op != "stop":
        stack.append(op)
        if op[0] == "+":
            num += int(op[1::])
        if op[0] == "-":
            num -= int(op[1::])
        if op[0] == "*":
            num *= int(op[1::])
        if op[0] == "/":
            num /= int(op[1::])
        print(num)
        return oper(input())
    
print(oper(input()))