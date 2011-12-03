'''
Created on Dec 3, 2011

@author: nebril
'''
import htdDisplayer
import sys

names = open(sys.argv[1])
for name in names.readlines():
    print name
    d = htdDisplayer.displayer(r"dane\\"+name.strip(), save=True)
    if(len(sys.argv) == 3):
        d.saveImage("obrazy\\" + sys.argv[2] + "\\" + name.strip() + ".jpg")
    else:
        d.saveImage()