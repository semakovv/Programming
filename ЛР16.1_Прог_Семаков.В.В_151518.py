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
    def AddFirst(self, a = None):
        f = Node(a)
        f.next = self.head
        self.head = f
    def AddEnd(self, a = None):
        e = Node(a)
        e.next = None

testlist = Link()

testlist.head = Node("1")

e2 = Node("2")

e3 = Node("3")

testlist.head.next = e2

e2.next = e3

testlist.PrintList()

testlist.AddFirst("4")

testlist.PrintList()

e4 = testlist.AddEnd("5")

e3.next = e4

testlist.PrintList()
№

