import argparse, os, subprocess

parser = argparse.ArgumentParser()

parser.add_argument("fc", help="Консольный файловый менеджер")
parser.add_argument("--create", "-ct", type=str, help="Создание файла")
parser.add_argument("--delete", "-dt", type=str, help="Удаление файла")
parser.add_argument("--read", "-rd", type=str, help="Чтение файла")
parser.add_argument("--replace", "-rc", type=str, help="Изменение файла")
parser.add_argument("--search", "-sh", type=str, help="Поиск файла")

args = parser.parse_args()

if args.fc:
    if args.create:
        with open(f"{os.getcwd()}{args.fc}", "w") as w:
            w.write("")
        w.close()
    # if args.delete:
    #     with open(f"{os.getcwd()}{args.delete}", "w") as w:
    #         w.write("")
    #     w.close()
    if args.read:
        with open((f"{os.getcwd()}{args.fc}", "r")) as r:
            read = r.read()
        r.close
    if args.replace:
        with open(f"{os.getcwd()}{args.fc}", "w") as w:
            w.write(f"{args.replace}")
        w.close()
    if args.search:
        with open(f"{os.getcwd()}{args.fc}", "w") as w:
            w.write(f"{args.replace}")
        w.close()