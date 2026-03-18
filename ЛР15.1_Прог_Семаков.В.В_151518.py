import argparse, os, subprocess

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
            w.write("")
        w.close()
    if args.delete:
        with open(f"{os.getcwd()}{args.delete}", "w") as w:
            w.write("")
        w.close()
    if args.read:
        with open(f"{os.getcwd()}\\{args.read}", "r") as r:
            read = r.read()
        r.close
        print(read)
        print(os.getcwd())
    if args.replace:
        with open(f"{os.getcwd()}\\{args.fc}", "w") as w:
            w.write(f"{args.replace}")
        w.close()
    if args.search:
        result = subprocess.run(["ls", f"{os.getcwd()}\\{args.search}"], shell=True, stdout=subprocess.PIPE)
        print(result.stdout)
    # for name, ex, date, len in :
    #     print(name, ex, date, len)