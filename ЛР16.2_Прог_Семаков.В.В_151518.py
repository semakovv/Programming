from collections import deque

count = 0
oper = None
unOper = None


def calc(COUNT, OPER):
    STR = ""
    while STR != "stop":
        STR = input()
        count = COUNT
        op = STR[0]
        num = int(STR[1::])
        OPER = deque()
        OPER.append(STR)
        return oper(count, op, num)
        # if STR is "undo" and OPER is not None:
        #     save = OPER.pop()
        #     UNOPER.append(save)
        #     return unOper(count, )

def oper(COUNT, OP, NUM):
    if OP == "+":
        COUNT += NUM
    if OP == "-":
        COUNT -= NUM
    if OP == "*":
        COUNT *= NUM
    if OP == "/":
        COUNT /= NUM
        
def unOper(COUNT, OP, NUM):
    if OP == "+":
        COUNT -= NUM
    if OP == "-":
        COUNT += NUM
    if OP == "*":
        COUNT /= NUM
    if OP == "/":
        COUNT *= NUM

calc(count, oper)


