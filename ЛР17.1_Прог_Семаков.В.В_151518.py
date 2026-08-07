# 55 дБА в дневное время (с 7:00 до 23:00) шум воды из крана;
# 45 дБА в ночное время (с 23:00 до 7:00) работа стиральной машины.
import argparse as ap
import datetime as dt

class hub:
    """
    The centaral system procceses the data and make issues commands
    """
    def __init__(self, SENSOR, ACTUATOR):
        self.database = {SENSOR.name: SENSOR.registration}
        self.statistics_list = []
        self.alert = ""
        for i in self.database[SENSOR.name]:
            if int(i) > 55:
                self.statistics_list.append(f"{i} ШУМНО!!!")
                self.alert = f"{i} ШУМНО!!!"
                ACTUATOR.display(self.alert)
            else:
                self.statistics_list.append(f"{i} тихо...")

    def noise_statistics(self):
        return self.statistics_list
    
    def noise_alerts(self):
        print(self.alert)

class noise_sensor:
    """
    The noise sensor detects sound waves
    """
    def __init__(self, NAME):
        self.name = f"NS_{NAME}"
        self.registration = input("Введите частоту: ")
    def registration():
        data = input("Введите частоту: ")
        return data

class noise_actuator:
    """
    The actuator executes commands
    """
    def __init__(self, NAME):
        self.name = f"NA_{NAME}"
    def display(DATA):
        print(DATA)
system_status = ""

parser = ap.ArgumentParser()

parser.add_argument("sh", help="Система умный дом")
parser.add_argument("-a", "--activate", help="Запуск системы умный дом")
parser.add_argument("-d", "--deactivate", help="Отключение системы умный дом")

arg = parser.parse_args()

if arg.sh:
    if arg.activate:
        system_status = "active"
    if arg.deactivate:
        system_status = "deactive"

ns_1 = noise_sensor("1")
na_1 = noise_actuator("1")
print(ns_1.name)
print(na_1.name)
system_center = hub(ns_1, na_1)
# while system_status == "active":
#     pass