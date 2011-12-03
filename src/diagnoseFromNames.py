'''
Created on Dec 3, 2011

@author: nebril
'''
import htdDiagnost
import sys
import getopt
import numpy as np

optlist, args = getopt.getopt(sys.argv[1:], "f:v")

names = ""
verbose = False
for o, a in optlist:
    if(o == "-v"):
        verbose = True
    elif( o == '-f'):
        names = open(a)
    else:
        assert False, "unhandled option"

if(names == ""):
    assert False, "names not set"
lengths = []
angles = []

#d = htdDiagnost.htdDiagnost(r"dane\\"+names.readline().strip())
#for p in d.packages:
#    print [p[4], p[5]]


for name in names.readlines():
    d = htdDiagnost.htdDiagnost(r"dane\\"+name.strip())
    length = d.getLength()
    angle = d.getAngleAverage()
    lengths.append(length)
    angles.append(angle)
    if(verbose):
        print name
        print "length: " + str(length)
        print "angle average: " + str(angle)
        
print "curve length statistics:"
print "\taverage: " + str(np.average(lengths))
print "\tmedian: " + str(np.median(lengths))
print "\tstandard deviation: " + str(np.std(lengths))
print "\tvariance: " + str(np.var(lengths))

print "average angle statistics:"
print "\taverage: " + str(np.average(angles))
print "\tmedian: " + str(np.median(angles))
print "\tstandard deviation: " + str(np.std(angles))
print "\tvariance: " + str(np.var(angles))
