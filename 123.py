import argparse, os, subprocess

parser = argparse.ArgumentParser()

parser.add_argument("fc", type = str, help = "fc")

args = parser.parse_args()

if args.fc:
    date_os = os.stat("./123.py").st_mtime
    print(date_os)
    date_subp = subprocess.run("dir", shell=True, stdout=subprocess.PIPE)
    print(date_subp.stdout.decode('cp866'))
    date_subp1 = date_subp.stdout.strip().split("\n")
    print(date_subp1)
        