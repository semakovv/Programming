import argparse, os, subprocess, re

parser = argparse.ArgumentParser()

parser.add_argument("fc", type = str, help = "fc")

args = parser.parse_args()

if args.fc:
    date_os = os.stat("./123.py").st_mtime
    print(date_os)
    date_subp = subprocess.run("dir", shell=True, stdout=subprocess.PIPE)
    print(date_subp.stdout.decode('cp866'))
    date_subp1 = [i.split("\r") for i in date_subp.stdout.decode('cp866').strip().split("\n") if i != ""]
    for i in date_subp1:
        for j in i:
            j = re.sub(r"\s+", "-", j)
    print(date_subp1)
        