import subprocess, re

flag = False
ip_area = input("Введите диапозон адрессов: ")
lst_ips = ip_area.split("-")
print(lst_ips)
for i in lst_ips:
    ip_patern = re.findall(r"[1-255].", i)
    if ip_patern:
        flag = True
        print("+")
    else:
        flag = False
        print("-")
        break

# lst_octets = []
# for i in lst_ips:
#     lst_octets.append(i.split("."))
# # lst_octets = [lst_ips[i].split(".") for i in lst_ips] #как сдалить через генерацию???
# print(lst_octets)
# while flag:
#     for i in lst_octets:
#         for j in i:
#             if j.isdigit() and 0 <= int(j) <= 255:
#                 flag = True
#             else:
#                 print("Неверный ввод")
#                 flag = False
#                 break
#     for a 
#     result = subprocess.Popen(['print'])