# 55 дБА в дневное время (с 7:00 до 23:00) шум воды из крана;
# 45 дБА в ночное время (с 23:00 до 7:00) работа стиральной машины.
import argparse as ap
import datetime as dt

class hub:
    """
    The centaral system procceses the data and make issues commands
    """
    def __init__(self):
        self.statistics_list = []
        self.alert = ""
        self.sensor_data = {}
        self.actuator_data = {}
                # print(self.database["sensors"], self.database["actuators"])

    def noise_database(self, SENSOR, ACTUATOR):
        self.sensor_data = {"sensors": {f"{i.name}": i.noise_registration() for i in SENSOR}}
        for i in self.sensor_data["sensors"].values():
            # print(i)
            for j in i:
                # print(j)
                if int(j) > 55:
                    self.statistics_list = [j + " ШУМНО!!!"]
                    self.alert = f"{j} ШУМНО!!!"
                else:
                    self.statistics_list = [j + " тихо..."]
        self.actuator_data = {"actuators": {f"{j.name}": self.statistics_list for j in ACTUATOR}}
        print(self.sensor_data)
        print(self.actuator_data)
        return self.sensor_data, self.actuator_data

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
        self.registration = []
    def noise_registration(self):
        self.registration.append(input(f"Введите частоту для {self.name}: "))
        return self.registration

class noise_actuator:
    """
    The actuator executes commands
    """
    def __init__(self, NAME):
        self.name = f"NA_{NAME}"
    def display(DATA):
        if DATA:
            print(DATA)

# system_status = ""

# parser = ap.ArgumentParser()

# parser.add_argument("sh", help="Система умный дом")
# parser.add_argument("-a", "--activate", help="Запуск системы умный дом")
# parser.add_argument("-d", "--deactivate", help="Отключение системы умный дом")

# arg = parser.parse_args()

# if arg.sh:
#     if arg.activate:
#         system_status = "active"
#     if arg.deactivate:
#         system_status = "deactive"

ns_1 = noise_sensor("1")
na_1 = noise_actuator("1")
ns_2 = noise_sensor("2")
na_2 = noise_actuator("2")
# print(ns_1.name)
# print(na_1.name)
system_center = hub()
system_center.noise_database([ns_1, ns_2], [na_1, na_2])
# while system_status == "active":
#     pass