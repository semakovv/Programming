import argparse, subprocess, os

parser = argparse.ArgumentParser()

parser.add_argument("proc", help="Консольный диспетчер задач")
parser.add_argument("-l", "--list", help="Вывод запущенных процессов")
parser.add_argument("-r", "--run", help="Запуск процессов")
parser.add_argument("-k", "--kill", help="Завершение процессов")

args = parser.parse_args()

system = os.name


if system == "nt":
    if args.proc:
        if args.list:
            subprocess.run("tasklist")
        if args.run:
            subprocess.run("start {args.run}")
        if args.kill:
            subprocess.run("taskkill /F /im {args.kill}")
else:
    if args.list:
        subprocess.run("ps")
    if args.run:
        subprocess.run("systemctl enable {args.run}")
    if args.kill:
        subprocess.run("systemctl disable {args.kill}")
