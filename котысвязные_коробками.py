class Box:
    def __init__ (self, cat = None):
        self.cat = cat
        self.nextcat = None

class LinkedList:
    def __init__(self):
        self.head = None

    def contains (self, cat):
        lastbox = self.head
        while (lastbox):
            if cat == lastbox.cat:
                return True
            else:
                lastbox = lastbox.nextcat
        return False

    def addToEnd(self, newcat):
        newbox = Box(newcat)
        if self.head is None:
            self.head = newbox
            return
        lastbox = self.head
        while (lastbox.nextcat):
            lastbox = lastbox.nextcat
        lastbox.nextcat = newbox

    def printBox(self):
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

cats.printBox()