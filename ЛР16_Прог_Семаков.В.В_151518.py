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
