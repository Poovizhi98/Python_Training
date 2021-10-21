# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 09:33:13 2019

@author: psabapathi
"""

import math
import tkinter as tk
import random
import pygame 
from tkinter import messagebox
class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        
    def move(self,dirnx,dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos=(self.pos[0]+self.dirnx,self.pos[1]+self.dirny)
        
    def draw(self, surface,eyes=False):
        distance = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface,self.color,(i*distance+1,j*distance+1, distance-2,distance-2))
        if eyes:
            center = distance //2
            radius = 3
            cm1 = (i*distance+center-radius,j*distance+8)
            cm2 = (i*distance+distance-radius*2, j*distance+8)
            pygame.draw.circle(surface,(0,0,0),cm1,radius)
            pygame.draw.circle(surface,(0,0,0),cm2,radius)      

class snake(object):
    body = []
    turns = {}
    def __init__(self,color,pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
        
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx ,self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx ,self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx ,self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx ,self.dirny]
        for i,c in enumerate(self.body):
              p = c.pos[:]
              if p in self.turns:
                  turn = self.turns[p]
                  c.move(turn[0],turn[1])
                  if i == len(self.body)-1:
                      self.turns.pop(p)
              else:
                  if c.dirnx == -1 and c.pos[0]<=0:
                      c.pos = (c.rows-1, c.pos[1]) #if no turn then goes to right side of the screen
                  elif c.dirnx == 1 and c.pos[0]>=c.rows-1:
                      c.pos = (0, c.pos[1])
                  elif c.dirny == 1 and c.pos[1]>=c.rows-1:
                      c.pos = (c.pos[0], 0)
                  elif c.dirny == -1 and c.pos[1]<=0:
                      c.pos = (c.pos[0], c.rows-1)
                  else:
                      c.move(c.dirnx,c.dirny)
                      
                      
    def reset(self,pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 1
        self.dirny = 0
        
    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))    
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1))) 
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
    def draw(self,surface):
        
        for i,c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True) # true for drawing eyes
            else:
                c.draw(surface)
    
def drawGrid(w,rows,surface):
    sizeBtwn = w // rows
    x,y=0,0
    for l in range(rows):
        x = x+sizeBtwn
        y = y+sizeBtwn
        pygame.draw.line(surface,(255,255,255),(x,0),(x,w))
        pygame.draw.line(surface,(255,255,255),(0,y),(w,y))
  
    #  to update the display
  #  We call this function once a frame from our game loop.
def redrawWindow(surface):
    global rows,width,s,snack
    
    surface.fill((0,0,0)) # Fills the screen with black
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width,rows,surface)  # Will draw our grid lines
    pygame.display.update()  # Updates the screen
    
def randomSnack(rows,item):
    positions = item.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y),positions)))>0:
            continue
        else:
            break
    return(x,y)
        
def message_box(subject,content):
    root = tk.Tk()
    root.attributes('-topmost',True)
    root.withdraw()
    messagebox.showinfo(subject,content)
    try:
        root.destroy()
    except:
        pass        
    
def main():
    global rows,width,s,snack
    width=500 # Width of our screen
    rows=20 # Amount of rows
    window=pygame.display.set_mode((width,width))  # Creates our screen object
    s=snake((255,0,0),(10,10))   # Creates a snake object which we will code later
    snack = cube(randomSnack(rows,s),color=(0,255,0))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        #pygame.time.delay(500)
        clock.tick(10)  # Will ensure the snake runs at 10 FPS
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows,s),color=(0,255,0))
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print('Score : ', len(s.body))
                message_box('You Lost!','Play Again')
                s.reset((10,10))
                break
        redrawWindow(window)

main()
