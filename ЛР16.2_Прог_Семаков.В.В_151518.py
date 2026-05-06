from collections import deque

count = 0
oper = deque()
unOper = deque()

def calc(COUNT, STR, OPER, UNOPER):
    STR = input()
    while STR != "stop":
        op = STR[0]
        num = STR[1::]
        count = COUNT
        if STR is r"[+-*/]\s{1}\d+":
            OPER.append(STR)
            return oper(count, op, num)
        # if STR is "undo" and OPER is not None:
        #     save = OPER.pop()
        #     UNOPER.append(save)
        #     return unOper(count, )

def oper(COUNT, OP, NUM):
    if OP is "+":
        COUNT += NUM
    if OP is "-":
        COUNT -= NUM
    if OP is "*":
        COUNT *= NUM
    if OP is "/":
        COUNT /= NUM
    return COUNT
        
def unOper(COUNT, OP, NUM):
    if OP is "+":
        COUNT -= NUM
    if OP is "-":
        COUNT += NUM
    if OP is "*":
        COUNT /= NUM
    if OP is "/":
        COUNT *= NUM


