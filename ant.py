from tkinter import *
import random
import time

root = Tk()

width = 800
height = 800

canvas = Canvas(root, width=width, height=height)
canvas.pack()

gridWidth = 10

class Ant:
    def __init__(self, x ,y, dir):
        self.x = x
        self.y = y
        self.dir = dir              

    def Draw(self):
        canvas.create_rectangle(self.x, self.y, self.x + gridWidth,
                                self.y + gridWidth, width = 0, fill="red")

    def Move(self):
        if self.dir == 0:
            self.x += 1 * gridWidth
        elif self.dir == 1:
            self.y += 1 * gridWidth
        elif self.dir == 2:
            self.x -= 1 * gridWidth
        elif self.dir == 3:
            self.y -= 1 * gridWidth
        else: print("ERROR")

    def Collision(self, pads):
        for pad in pads:
            if self.x == pad.x and self.y == pad.y:
                if pad.color == "black":
                    self.ClockWise()
                    pad.color = "orange"
                    return pads
                if pad.color == "orange":
                    self.CounterWise()
                    pads.remove(pad)
                    return pads
                

        pads.append(Pad(self.x,self.y,gridWidth,gridWidth,"black"))
        self.CounterWise()
        return pads

    def ClockWise(self):
        self.dir += 1
        if self.dir > 3:
            self.dir = 0
    
    def CounterWise(self):
        self.dir -= 1
        if self.dir < 0:
            self.dir = 3

class Pad:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def Draw(self):
        canvas.create_rectangle(self.x, self.y, self.x + self.width,
                                self.y + self.height, width = 0, fill=self.color)
  
def Main(*args, **kwargs):
    multiplier = 5
    
    pads = []
    ant = Ant(width/2,height/2,3)
    while(True):
        #time.sleep(1)
        canvas.delete('all')
        for i in range(multiplier):
            pads = ant.Collision(pads)
            ant.Move()
        for i in pads:
            i.Draw()
        ant.Draw()
        canvas.update()


Main()
    

