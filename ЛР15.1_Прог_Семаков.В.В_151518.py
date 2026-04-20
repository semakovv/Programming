import argparse, os, re, datetime

parser = argparse.ArgumentParser()

parser.add_argument("fc", help="Консольный файловый менеджер")
parser.add_argument("--create", "-c", type=str, help="Создание файла")
parser.add_argument("--delete", "-d", type=str, help="Удаление файла")
parser.add_argument("--read", "-r", type=str, help="Чтение файла")
parser.add_argument("--replace", "-R", type=str, help="Изменение файла")
parser.add_argument("--search", "-s", type=str, help="Поиск файла")

args = parser.parse_args()

if args.fc:
    if args.create: #Создание файла
        with open(f"{os.getcwd()}\\{args.create}", "w") as w:
            w.write(f"{args.fc}")
        w.close()
    if args.delete: #Удаление файла
        os.remove(f"{os.getcwd()}\\{args.delete}")
    if args.read: #Чтение файла
        with open(f"{os.getcwd()}\\{args.read}", "r") as r:
            read = r.read()
        r.close
        print(read)
    if args.replace: #Изменение файла
        with open(f"{os.getcwd()}\\{args.replace}", "w") as w:
            w.write(f"{args.fc}")
        w.close()
    if args.search: #Поиск файла
        for i in os.listdir(f"{os.getcwd()}"):
            end_pattern = re.findall(r"\.\w+$", i)
            end = "".join(end_pattern)
            # name = i.replace(end, "")
            stat = os.stat(i)
            date_stat = stat.st_mtime
            date_answer = datetime.date.fromtimestamp(date_stat)
            date_request = datetime.date.strptime(args.search, "%Y-%m-%d")
            size_stat = stat.st_size
            size_answer = str(size_stat) + "kb"
            size_request = str(args.search)
            if args.search in i: #По подстроке
                print(i)
            elif args.search is end: #По разрешению(с точкой в начале!) === по подстроке(но вдруг py.pdf)
                print(i)
            elif date_request == date_answer: #По времени
                print(i)
            elif size_request == size_answer: #По размеру
                print(i)
            else:
                print("Формы поиска:\n-'часть имени'\n-'.(расширение)'\n-'(год)-(месяц)-(день)'\n-'(размер в килобайтах)kb'")
                break

№
                
            
 