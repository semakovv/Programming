# 55 дБА в дневное время (с 7:00 до 23:00) шум воды из крана;
# 45 дБА в ночное время (с 23:00 до 7:00) работа стиральной машины.
from datetime import datetime
class sensor:
    """
    Класс датчика шума
    """
    number = 0
    currentValue = 0
    minValue = 0
    maxValue = 50

    def __init__(self, number, currentValue):
        self.number = number
        self.currentValue = currentValue

    def getCurrentValue(self):
        """
        Метод получения текущего значения датчика
        """
        value = self.number, str(self.currentValue)+"dB"
        return value

    
class flat:
    """
    Класс квартиры
    """
    entrance = 0
    floor = 0
    number = 0

    def __init__(self, entrance, floor, number):
        self.entrance = entrance
        self.floor = floor
        self.number = number

    def getIdFlat(self):
        """
        Метод получения расположения квартиры
        """
        idFlat = {"Подъезд": self.entrance, "Этаж": self.floor, "Номер": self.number}
        return idFlat

class event:
    """
    Класс управления
    """
    status = ""
    time = datetime.now()

    def __init__(self, status, time):
        self.status = status
        self.time = time
    
    def showStatus(self):
        """
        Метод вывода события
        """
        if self.status:
            return self.status, self.time

class manager:
    """
    Класс события
    """
    warning = ""
    time = datetime.now()

    def __init__(self, warning, time):
        self.warning = warning
        self.time = time

    def showWarning(self):
        """
        Метод вывода предупредения
        """
        if self.warning:
            return self.warning, self.time


"Проверка Класса датчика шума"
if __name__ == "__main__":
    n123 = sensor(1, 30)
    print(n123.getCurrentValue())

"Проверка Класса квартиры"
if __name__ == "__main__":
    n123 = flat(1, 2, 3)
    print(n123.getIdFlat())

"Проверка Класса события"
if __name__ == "__main__":
    ev123 = event("Ошибка", datetime.now())
    print(ev123.showStatus())

"Проверка Класса управления"
if __name__ == "__main__":
    wr123 = manager("Предупреждение", datetime.now())
    print(wr123.showWarning())





