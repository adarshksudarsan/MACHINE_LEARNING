import os
import re

path = '/home/vvdn/New_Yolo_Ann_tool/Labels/001'
files = []

def del_line(check_this):
    with open(check_this, "r") as f:
        lines = f.readlines()
    with open(check_this, "w") as f:
        for line in lines:
            a = line.rstrip('\n')
            a = a.split(" ")
            if('0.0' not in a):
                f.write(line)
	    else:
                print(line)

for r, d, f in os.walk(path):
    for file in f:
        if('.txt' in file):
            files.append(os.path.join(r,file))

for line in files:
    del_line(line)

