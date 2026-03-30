import argparse, os, re

parser = argparse.ArgumentParser()

parser.add_argument("fc", help="Консольный файловый менеджер")
parser.add_argument("--create", "-c", type=str, help="Создание файла")
parser.add_argument("--delete", "-d", type=str, help="Удаление файла")
parser.add_argument("--read", "-r", type=str, help="Чтение файла")
parser.add_argument("--replace", "-R", type=str, help="Изменение файла")
parser.add_argument("--search", "-s", type=str, help="Поиск файла")

args = parser.parse_args()

if args.fc:
    if args.create:
        with open(f"{os.getcwd()}\\{args.create}", "w") as w:
            w.write(f"{args.fc}")
        w.close()
    if args.delete:
        os.remove(f"{os.getcwd()}\\{args.delete}")
    if args.read:
        with open(f"{os.getcwd()}\\{args.read}", "r") as r:
            read = r.read()
        r.close
        print(read)
    if args.replace:
        with open(f"{os.getcwd()}\\{args.replace}", "w") as w:
            w.write(f"{args.fc}")
        w.close()
    if args.search:
        for i in os.listdir(f"{os.getcwd()}"):
            print(i)
            name = i.split(".")
            print(name)
            print(i.replace(name[-1], ""))
            if args.search == i.replace(name[-1], ""):
                print(i)