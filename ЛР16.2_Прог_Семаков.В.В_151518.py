from collections import deque

stack = deque()
num = 0
def oper(op):
    while op != "stop":
        stack.append(op)
        if op[0] == "+":
            num += int(op[1::])
        if op[0] == "-":
            num -= int(op[1::])
        if op[0] == "*":
            num *= int(op[1::])
        if op[0] == "/":
            num /= int(op[1::]
        op = input()
        return  num
print(oper(input()))