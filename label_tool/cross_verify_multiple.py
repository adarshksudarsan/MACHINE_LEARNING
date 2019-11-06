import os
from PIL import Image
import cv2
import dlib
#import cv2
import argparse as ap
#import get_points
#import cv2
import numpy as np
from matplotlib import pyplot as plt

def conv1(x,y,w,h):
        dw = 1./width
        dh = 1./height
        x = x/dw
        w = w/dw
        y = y/dh
        h = h/dh
        #print x
        #print w
        #print y
        #print h

        xmin=x-(w/2)
        xmax=x+(w/2)
        ymin=y-(h/2)
        ymax=y+(h/2)

        return (xmin, xmax, ymin, ymax)


def switch_labels(folder):

    if folder == "0":
        label="KELLOGS"
    elif folder == "1":
        label="CHOCOLATE"
    elif folder == "2":
        label="CANDLE"
    elif folder == "3":
        label="SHAMPOO"
    elif folder == "4":
        label="BULB"
    elif folder == "5":
        label="PLIERS"
    elif folder == "6":
        label="DETERGENT"
    elif folder == "7":
        label="KOOLAID"
    elif folder == "8":
        label="LIPSTICK"
    elif folder == "9":
            label="BOX"
    return label

path = './new'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    #print(d)
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

for f in files:
    filename = os.path.splitext(f)[0]
    #print filename
    namealone = os.path.basename(filename)
    img = cv2.imread(filename + ".jpg")
    height, width = img.shape[:2]
    #height = 1080
    #width = 1920
    file1 = open(f, "r+")
    #filedata = file1.read()
    for line in file1:
        val = line.split(' ')
        #if val[0] == '3':
        print filename
        print val[1]
        print val[2]
        print val[3]
        print val[4]

        x = float(val[1])
        y = float(val[2])
        w = float(val[3])
        h = float(val[4])
	#val[0] = '4'
        print '###################################'
	xmin, xmax, ymin, ymax=conv1(x,y,w,h)
        print xmin
        print ymin
        print xmax
        print ymax

        #box=(xmin, xmax, ymin, ymax)
        #dxmin, dxmax, dymin, dymax=convert(height, width, box)
        #print xmin
        #print xmax
        #print ymin
        #print ymax
        #val[1]=str(dxmin)
        #val[2]=str(dxmax)
        #val[3]=str(dymin)
        #val[4]=str(dymax)
        #b = " ".join(val)
	#with open(f, 'w') as file:
       	#    file.write(b)
        labname=switch_labels(val[0])
        pt1=(int(xmin), int(ymin))
        pt2=(int(xmax), int(ymax))
        cv2.rectangle(img, pt1, pt2, (0, 0, 0), 3)
        cv2.putText(img, labname, (int(xmin), int(ymin) + 10), 1, 1, (200,34 ,244 ), 2, cv2.LINE_AA)
        #img2 = img.crop((xmin, ymin, xmax, ymax))
        cv2.imwrite(("./out/" + namealone + ".jpg"), img)
    file1.close()
