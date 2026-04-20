from random import randrange

class Node:
    """
    Класс для хранения узлов списка.
    data - полезная нагрузка.
    next - поле для связи со следующим элементом.
    """
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    """
    Класс для хранения головы списка.
    """
    def __init__(self):
        self.head = None

    def createRandomList(self, n, a = 0, b = 100):
        """
        Создание случайного списка из n элементов. Случайные значения берутся
        из диапазона [a, b]
        """
        # Создаем первый элемент списка
        self.head = Node(randrange(a, b + 1))
        # Чтобы не потерять начало списка, используем дополнительную переменную
        p = self.head
        # В цикле создаем еще n-1 элементов и связываем их между собой
        for i in range(n-1):
            e = Node(randrange(a, b + 1))
            p.next = e
            p = p.next

    def printList(self):
        """
        Печать списка.
        Последовательно просматриваем все элементы списка и выводим их.
        """
        p = self.head
        while p != None:
            print(p.data, end=" ")
            p = p.next
        print()

    def addFirst(self, a = 0):
        """
        Добавление первого элемента в список
        """
        e = Node(a)
        e.next = self.head
        self.head = e
        
# Пример 1
# Ручное заполнение списка. Создаем список
testList = LinkedList()
# Добавляем первый элемент
testList.head = Node("Mon")
# Создаем еще два узла
e2 = Node("Tue")
e3 = Node("Wed")
# Соединяем начало списка со вторым узлом
testList.head.next = e2
# Соединяем второй узел с третьим
e2.next = e3
# Печатаем список
testList.printList()
# Создаем еще один узел
e4 = Node("Fri")
# Добавляем узел в конец списка
# Чтобы не потерять начало списка, используем дополнительную переменную
p = testList.head
# Доходим до последнего элемента списка, перемещаясь по связям
while p.next != None:
    p = p.next
# Связываем последний элемент с созданным
p.next = e4
# Снова печатаем список
testList.printList()

# Пример 2
# Создание и вывод списка, заполненного случайными значениями
mylist = LinkedList()
mylist.createRandomList(15, -100, 100)
mylist.printList()
mylist.addFirst(5)
mylist.printList()
mylist.addFirst(42)
mylist.printList()
n = Node(randrange(0, 101))
p = mylist.head
# Доходим до последнего элемента списка, перемещаясь по связям
while p.next != None:
    p = p.next
# Связываем последний элемент с созданным
p.next = n
mylist.printList()

