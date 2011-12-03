'''
Created on Dec 3, 2011

@author: nebril
'''
import loaderHTD
import math

class htdDiagnost:
    def __init__(self, filename):
        self.packages = loaderHTD.DataHTD(filename).packages
        
    def getLength(self):
        length = 0;
        for i in range(0, len(self.packages)-1):
            altitude = (self.packages[i][3] + self.packages[i+1][3])/2
            if(altitude == 0): continue
            coords = ((self.packages[i][1], self.packages[i][2]),(self.packages[i+1][1], self.packages[i+1][2]))
            length += self.length(coords)
        return length
    
    def getAngleAverage(self):
        angleSum = 0.0
        count = 0.0
        for i in range(0, len(self.packages)-2, 100):
            v1 = ((self.packages[i][1], self.packages[i][2]),(self.packages[i+1][1], self.packages[i+1][2]))
            v2 = ((self.packages[i+1][1], self.packages[i+1][2]),(self.packages[i+2][1], self.packages[i+2][2]))
            if(self.length(v1) == 0 or self.length(v2) == 0): continue
            angleSum += self.angle(v1, v2)
            count = count + 1
            
        return angleSum/count

    def getAzimuthChanges(self):
        """TODO"""
        print 'TODO'
    
    def lineToVector(self, l):
        v = []
        for i in range(0, len(l[0])):
            v.append(l[1][i] - l[0][i])
        return v
    
    def dotproduct(self, v1, v2):
        if(type(v1).__name__ != 'list'):
            v1 = self.lineToVector(v1)
            v2 = self.lineToVector(v2)
            
        return sum((a*b) for a, b in zip(v1, v2))
    
    def length(self, v):
        return math.sqrt(self.dotproduct(v, v))
    
    def angle(self, v1, v2):
        cosine = round(self.dotproduct(v1, v2) / (self.length(v1) * self.length(v2)), 12)
#        return 1
        return math.acos(cosine)
        