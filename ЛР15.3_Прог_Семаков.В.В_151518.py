import subprocess
flag = True
ip_area = input("Введите диапозон адрессов: ")
print(ip_area)
lst_ips = ip_area.split("-")
print(lst_ips)
lst_octets = []
for i in lst_ips:
    lst_octets.append(i.split("."))
# lst_octets = [lst_ips[i].split(".") for i in lst_ips] #как сдалить через генерацию???
print(lst_octets)
for i in lst_octets:
    for j in i:
        if j.isdigit() and 0 <= int(j) <= 255:
            flag = True
        else:
            flag = False
            break
            print("Неверный ввод")