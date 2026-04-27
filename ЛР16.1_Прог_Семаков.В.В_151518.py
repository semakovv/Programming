class Node:
    """
    Класс узлов
    """
    def __init__(self, data = None):
        """
        Функция добавления данных и указателей в узел
        """
        self.data = data
        self.next = None

class Link:
    """
    Класс первого узла
    """
    def __init__(self):
        """
        Функция добавления первого узла
        """
        self.head = None

    def printList(self):
        """
        Функция печати узлов
        """
        p = self.head
        while p != None:
            print(p.data, end = " ")
            p = p.next
        print()

    def addToFirst(self, newData = None):
        """
        Функция добавления узла в начало
        """
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def addToEnd(self, newData = None):
        """
        Функция добавления узла в конец
        """
        newNode = Node(newData)
        lastNode = self.head
        while lastNode.next is not None:
            lastNode = lastNode.next
        lastNode.next = newNode

    def delFromFirst(self):
        """
        Функция удаления узла из начала
        """
        self.head = self.head.next

    def delFromEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            postNode = lastNode
            lastNode = lastNode.next
        postNode.next = None
    
    def search(self, searchNode = None):
        lastNode = self.head
        indexNode = 0
        while lastNode.next is not None:
            if searchNode is lastNode:
                return indexNode
        

            
                

testlist = Link()

testlist.head = Node("1")
e2 = Node("2")
e3 = Node("3")
testlist.head.next = e2
e2.next = e3
testlist.printList()

testlist.addToFirst("0")
testlist.printList()

testlist.addToEnd("5")
testlist.printList()

testlist.delFromFirst()
testlist.printList()

testlist.delFromEnd()
testlist.printList()

print(testlist.search("2"))