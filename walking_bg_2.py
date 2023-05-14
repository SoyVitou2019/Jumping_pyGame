import pygame as py
import glob


img_left = []
for imgs in glob.glob("./walking/*.png"):
    img_left.append(py.transform.flip(py.transform.scale(py.image.load(imgs),(140,140)),True,False))
img_right = []
for imgs in glob.glob("./walking/*.png"):
    img_right.append(py.transform.scale(py.image.load(imgs),(140,140)))

# constant variable
Width = 800
Height = 600
screen = py.display.set_mode((Width,Height))
title = py.display.set_caption("Walking Pro")

# create object player
class Player():
    def __init__(self, x, y,bg):
        self.x = x
        self.y = y
        self.walk_change = 0
       
        self.bg = bg
        self.gravity = 10
        self.height_jump_bool = False
    def walking(self,bg_x):
        self.walk_change+=1
        screen.blit(self.bg,(bg_x,0))
        screen.blit(img_right[self.walk_change],(self.x,self.y))
        self.walk_change +=1
        if self.walk_change >= len(img_right):
            self.walk_change = 0
            self.right = False
        py.display.update()
                
    def jump(self,bg_x):
        keys = py.key.get_pressed()
        if keys[py.K_UP]:
            self.height_jump_bool = True
            
        if self.height_jump_bool:
            if self.gravity >= -10:
                neg = 1
                if self.gravity < 0:
                    neg = -1
                self.y -= (self.gravity ** 2) * 0.5 * neg
                screen.blit(self.bg,(bg_x,0))
                screen.blit(img_right[self.walk_change],(self.x, self.y))
                py.display.update()
                self.gravity -= 1
            else:
                self.height_jump_bool = False
                self.gravity = 10
            
   
            
            
            
 


