class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
class Link:
    def __init__(self):
        self.head = None
    def PrintList(self):
        p = self.head
        while p != None:
            print(p.data, end = " ")
            p = p.next
        print()

testlist = Link()

testlist.head = Node("1")

testlist.head.next = e2

e2 = Node("2")

e2.next = e3

e3 = Node("3")

testlist.PrintList()