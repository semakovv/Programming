#https://habr.com/ru/companies/otus/articles/470828/
class Box:
    """
    Класс узлов
    """
    def __init__ (self, cat = None):
        """
        Добавление данных и указателей в узлы
        """
        self.cat = cat
        self.nextcat = None

class LinkedList:
    """
    Класс первого узла
    """
    def __init__(self):
        """
        Добавление первого узла
        """
        self.head = None

    def contains (self, cat):
        """
        Содержится ли элемент в списке
        """
        lastbox = self.head
        while (lastbox):
            if cat == lastbox.cat:
                return True
            else:
                lastbox = lastbox.nextcat
        return False

    def addToEnd(self, newcat):
        """
        Добавление узла в конец списка
        """
        newbox = Box(newcat)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while (lastbox.nextcat):
            lastbox = lastbox.nextcat
        lastbox.nextcat = newbox

    def get(self, catIndex):
        """
        Получение узела по индексу
        """
        lastbox = self.head
        boxIndex = 0
        while boxIndex <= catIndex:
            if boxIndex == catIndex:
                return lastbox.cat
            boxIndex = boxIndex + 1
            lastbox = lastbox.nextcat

    def printBox(self):
        """
        Печать списка
        """
        p = self.head
        while p != None:
            print(p.cat, end = " ")
            p = p.nextcat
        print()


cats = LinkedList()
cats.head = Box("1")
cat2 = Box("2")
cat3 = Box("3")

cats.head.nextcat = cat2
cat2.nextcat = cat3

cats.addToEnd("4")

cat_search = cats.get(2)
print(cat_search)

cats.printBox()