import argparse, subprocess

parser = argparse.ArgumentParser()

parser.add_argument("proc", help="Консольный диспетчер задач")
parser.add_argument("-list", "-l", help="Вывод запущенных процессов")
parser.add_argument("-run", "--r", help="Запуск процессов")
parser.add_argument("-kill", "-k", help="Завершение процессов")

args = parser.parse_args()

system = subprocess.run("uname")

if system == "Linux":
    if args.list:
        subprocess.run("ps")
    if args.run:
        subprocess.run("systemctl enable {args.run}")
    if args.kill:
        subprocess.run("systemctl disable {args.kill}")
else:
    if args.proc:
        if args.list:
            subprocess.run("tasklist")
        if args.run:
            subprocess.run("start {args.run}")
        if args.kill:
            subprocess.run("taskkill /F /im {args.kill}")

№
