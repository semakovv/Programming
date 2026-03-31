import subprocess
ip_area = input("Введите диапозон адрессов: ")
print(ip_area)
try:
    lst_ips = ip_area.split("-")
    print(lst_ips)
    lst_octets = []
    for i in lst_ips:
        lst_octets.append(i.split("."))
    # lst_octets = [lst_ips[i].split(".") for i in lst_ips] #как сдалить через генерацию???
    print(lst_octets)
    for i in lst_octets:
        
except Exception as e:
    print("Error", e)