'''
Created on Dec 3, 2011

@author: nebril
'''
import loaderHTD
import Tkinter
import Image, ImageDraw

class displayer:
    width = 1200
    height = 800
    filename = ""
    save = False
    
    def __init__(self, filename, save):
        self.filename = filename
        htd = loaderHTD.DataHTD(filename)
        constans = 20
        self.save = save
        if(not save):
            self.root = Tkinter.Tk()
            self.root.geometry(str(self.width)+"x"+str(self.height))
            self.w = Tkinter.Canvas(self.root, width=self.width, height=self.height)
            self.w.pack()
        else:
            self.image = Image.new("RGB", (self.width, self.height), (255,255,255))
            self.draw = ImageDraw.Draw(self.image)
        
        for i in range(0, len(htd.packages)-1):
            altitude = (htd.packages[i][3] + htd.packages[i+1][3])/2
            if altitude == 0: continue
            rgb = self.getColor(altitude/1023.0)
            Hex = '#%02x%02x%02x' % rgb
            coords = ((htd.packages[i][1]/constans, htd.packages[i][2]/constans),(htd.packages[i+1][1]/constans, htd.packages[i+1][2]/constans))
            if(not save):
                self.w.create_line(coords[0][0], coords[0][1], coords[1][0], coords[1][1], fill=str(Hex))
            else:
                self.draw.line(coords, fill=str(Hex), width=1)
    def saveImage(self, filename=""):
        if(self.save):
            if(filename==""):
                self.image.save(self.filename+".jpg")
            else:
                self.image.save(filename)
    
    def display(self):
        if(not self.save):
            self.root.mainloop()
    
    def getColor(self, i):
        r = 0;
        g = 0;
        b = 0;
        if i > 1:
            i = i % 1
            
        if i <= 0.25:
            r = 0
            g = (i)*4
            b = 1
        elif i <= 0.5:
            r = 0
            g = 1
            b = 1 - (i-0.25)*4
        elif i <= 0.75:
            r = (i-0.5)*4
            g = 1
            b = 0
        elif i <= 1:
            r = 1;
            g = 1-(i-0.75)*4;
            b = 0;
            
        return (round(r*255),round(g*255),round(b*255));
