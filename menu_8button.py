#!/usr/bin/env python
import sys, os, time, subprocess, commands, pygame
from pygame.locals import *
from subprocess import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

# Initialize pygame modules individually (to avoid ALSA errors) and hide mouse

pygame.font.init()
pygame.display.init()

pygame.mouse.set_visible(1)
border = 1

#colors     R    G    B
white   = (255, 255, 255)
red     = (255,   0,   0)
green   = (  0, 255,   0)
blue    = (  0,   0, 255)
black   = (  0,   0,   0)
cyan    = ( 50, 255, 255)
magenta = (255,   0, 255)
yellow  = (255, 255,   0)
orange  = (255, 127,   0)


class Button:
    def __init__(self,x,y,w,h,text="Button", colour=green,handler=None):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.handler = handler
        self.text = text
        self.colour=colour
        self.render()
    
    def render(self):
        font=pygame.font.Font(None,42)
        label=font.render(str(self.text), 1, (self.colour))
        screen.blit(label,(self.x,self.y))
        pygame.draw.rect(screen, blue, (self.x-border,self.y-border,self.w,self.h),3)

    def center(self):
        return ((self.x + self.w/2),(self.y + self.h/2))
    
    def hit_test(self,x,y):
        if self.x <= x <= (self.x+self.w) and self.y <= y <= (self.y + self.h):
            print "Button pressed: " + self.text + "!"
            if self.handler != None:
                self.handler()
            return True
        else:
            return False



# Set up the base menu you can customize your menu with the colors above
btn_config = [
    {"label":"Button 1","handler":"echo 'Button 1'", "colour":[255,0,0]},
    {"label":"Button 2","handler":"echo 'Button 2'", "colour":[255,0,0]},
    {"label":"Button 3","handler":"echo 'Button 3'", "colour":[255,0,0]},
    {"label":"Button 4","handler":"echo 'Button 4'", "colour":[255,0,0]},
    {"label":"Button 5","handler":"echo 'Button 5'", "colour":[255,0,0]},
    {"label":"Button 6","handler":"echo 'Button 6'", "colour":[255,0,0]},
    {"label":"Button 7","handler":"echo 'Button 7'", "colour":[255,0,0]},
    {"label":"Button 8","handler":"echo 'Button 8'", "colour":[255,0,0]},
]
config = {
    "width":320,
    "height":240,
    "buttons":btn_config
}

try:
    with open("menu_config.json","r") as f:
        config = json.load(f)
except:
    print "Error loading config"
        
#set size of the screen
width = config["width"]
height = config["height"]
size = (width, height)
screen = pygame.display.set_mode(size)

# Background Color
screen.fill(black)

# Outer Border
pygame.draw.rect(screen, blue, (0,0,width,height),10)
pad = width/16
button_width = (width - pad - 4*border)/2
button_height = (height - pad - 4*border)/4
nRows = 4
nCols = 2


buttons = []
def dummy_function(n):
    print "Button %d pushed"%(n)
n = 0


for row in range(0,nRows):
    for col in range(0,nCols):            
        btn = config["buttons"][n]
        b = Button(pad*(col+1)+button_width*col,pad*(row+1)+button_height*row,button_width, button_height,btn["label"],btn["colour"],lambda: os.system(btn["handler"]) )
        buttons.append(b)
        n=n+1

# define function that checks for touch location
def on_touch():
    # get the position that was touched
    touchx,touchy = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    for b in buttons:
        b.hit_test(touchx,touchy)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print "screen pressed" #for debugging purposes
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            print pos #for checking
            on_touch()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    pygame.display.update()
