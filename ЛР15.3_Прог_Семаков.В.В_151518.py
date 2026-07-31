import subprocess

flag = False
ip_area = input("Введите диапозон адрессов: ")
lst_ips = ip_area.split("-")
# print(lst_ips)
ip_first = lst_ips[0].split(".")
ip_last = lst_ips[1].split(".")
# print(ip_first, ip_last, sep = "\n")
def ip_pattern(IP, FLAG):
    for i in IP:
        if 1 < int(i) < 255:
            FLAG = True
        else:
            FLAG = False
        return FLAG

flag = ip_pattern(ip_first, flag)
flag = ip_pattern(ip_last, flag)
if flag:
    for i in range(int(ip_first[-1]), int(ip_last[-1]) + 1):
        ip = ip_first
        ip[-1] = str(i)
        ip = ".".join(ip)
        process = subprocess.run(["ping", f"{ip}"], shell=True, stdout=subprocess.PIPE)
        if process.returncode == 0:
            print(ip)
else:
    print("Неправильнный ввод")



