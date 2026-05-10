from collections import deque
import re

def operPattern(ST):
    ptrn = re.findall(r"[+-/*]{1} \d+", ST)
    if (ptrn):
        return ST

def oper(ST, TOTAL):

    op = ST[0]
    num = int(ST[2::])

    if op == "+":
        TOTAL += num
    if op == "-":
        TOTAL -= num
    if op == "*":
        TOTAL *= num
    if op == "/":
        TOTAL /= num
    return TOTAL

def unOper(ST, TOTAL):

    op = ST[0]
    num = int(ST[2::])

    if op == "+":
        TOTAL -= num
    if op == "-":
        TOTAL += num
    if op == "*":
        TOTAL /= num
    if op == "/":
        TOTAL *= num
    return TOTAL

st = "+ 0"
total = 0
stackForOper = deque()
stackForUnOper = deque()

while st != "stop":
    st = input()
    print(total)

    if (operPattern(st)):
        stackForOper.append(st)
        total = oper(st, total)
        continue

    if st == "undo":
        save = stackForOper.pop()
        stackForUnOper.append(save)
        total = unOper(save, total)
        continue

    if st == "redo":
        save = stackForUnOper.pop()
        total = oper(save, total)
        continue







