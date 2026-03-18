# try?
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("intxt", type=str, help="Приложение для создания файла txt", )
parser.add_argument("-f", "--file", type=str, help="Имя файла txt, по умолчанию Task1_output.txt", default="Task1_output")
parser.add_argument("-r", "--read", type=str, help="Чтение файла txt, по умолчанию Task1_output.txt", default="Task1_output")
parser.add_argument("-c", "--count", type=str, help="Кол-во слов файла txt, по умолчанию Task1_output.txt", default="Task1_output")
try:
    args = parser.parse_args()
except Exception as e:
    print("Error")

if args.intxt:
    with open("./Task1_output.txt", "w") as w:
        w.write(f"{args.intxt}")
    w.close()
if args.file:
    with open(f"./{args.file}.txt", "w") as w:
        w.write(f"{args.intxt}")
    w.close()
if args.read:
    with open(f"./{args.read}.txt", "r") as r:
        read = r.read()
    print(read)
    r.close()
if args.count:
    with open(f"./{args.count}.txt", "r") as r:
        read = r.read()
    lst = read.split()
    print(len(lst))

