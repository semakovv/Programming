# 1 #
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("intxt", help="input text in txt file")
# args = parser.parse_args()
# with open("./Task1_output.txt", "w") as w:
#     w.write(args.intxt)
# w.close()
# 2 #
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("intxt", help="input text in txt file")
# parser.add_argument("-f", "--file", help="input name the txt file")
# args = parser.parse_args()
# with open("./Task1_output.txt", "w") as w:
#     w.write(args.intxt)
# w.close()
# if args.file:
#     with open(f"./{args.file}", "w") as w:
#         w.write(args.intxt)
#     w.close()
# 3 #
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("intxt", help="input text in txt file")
# parser.add_argument("-f", "--file", help="input name the txt file")
# args = parser.parse_args()
# with open("./Task1_output.txt", "w") as w:
#     w.write(args.intxt)
# w.close()
# if args.file == "":
#     print("Error")
# else:
#     with open(f"./{args.file}.txt", "w") as w:
#         w.write(args.intxt)
#     w.close()
# 4 # как сделать валидацию?
# import argparse
# try:    
#     parser = argparse.ArgumentParser()
#     parser.add_argument("intxt", help="input text in txt file")
#     parser.add_argument("-f", "--file", help="input name the txt file")
#     parser.add_argument("-r", "--read", help="read the txt file")
#     args = parser.parse_args()
#     with open("./Task1_output.txt", "w") as w:
#         w.write(args.intxt)
#     w.close()
#     if args.file:
#         with open(f"{args.file}", "w") as w:
#             w.write(args.intxt)
#         w.close()
#     if args.read:
#         with open(f"{args.read}") as r:
#             s = r.read()
#         print(s)
#         r.close()
# except Exception as e:
#     print(f"Error: {e}")
# 5 # документация?
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("intxt", help="input text in txt file")
# parser.add_argument("-f", "--file", help="input name the txt file")
# parser.add_argument("-r", "--read", help="read the txt file")
# parser.add_argument("-c", "--count", help="output count words in txt file")
# args = parser.parse_args()
# count = 1
# with open("./Task1_output.txt", "w") as w:
#     w.write(args.intxt)
# w.close()
# if args.file == "":
#     print("Error")
# else:
#     with open(f"./{args.file}.txt", "w") as w:
#         w.write(args.intxt)
#     w.close()
# if args.read:
#     with open(f"./{args.read}.txt") as r:
#         s = r.read()
#     print(s)
#     r.close()
# if args.count:    
#     with open(f"./{args.count}.txt") as r:
#         s = r.read()
#     s = s.split()
#     print(len(s))
#     r.close()
# final
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("intxt", help="input text in txt file")
parser.add_argument("-f", "--file", help="input name the txt file", default="Task1_output.txt")
args = parser.parse_args()
with open("Task1_output.txt", "w") as w:
    w.write(args.intxt)
w.close()
try:
    if args.file:
        with open(f"{args.file}", "w") as w:
            w.write(args.intxt)
        w.close()
except Exception as e:
    print("Error srjhwrjwwhdqwhj")