import os
from PIL import Image

path = '.'

files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            basewidth = 854
            img = Image.open(os.path.join(r, file))
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)
            img.save(os.path.join(r, file))
            print(file)
