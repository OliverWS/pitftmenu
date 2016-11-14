import sys, pygame
from pygame.locals import *
import time
import subprocess
import os
from subprocess import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

# Initialize pygame and hide mouse
pygame.init()
pygame.mouse.set_visible(0)

class Button:
    def __init__(self,x,y,w,h,handler=None):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.handler = handler
        self.render()
    
    def render(self):
        font=pygame.font.Font(None,42)
        label=font.render(str(text), 1, (colour))
        screen.blit(label,(xpo,ypo))
        pygame.draw.rect(screen, blue, (xpo-border,ypo-border,width,height),3)

    def center(self):
        return ((self.x + self.w/2),(self.y + self.h/2))
    
    def hit_test(self,x,y):
        if self.x <= x <= (self.x+self.w) and self.y <= y <= (self.y + self.h):
            if self.handler != None:
                self.handler()
            return True
        else:
            return False


# define function for printing text in a specific place with a specific width and height with a specific colour and border
def make_button(text, xpo, ypo, height, width, colour,border=10,handler=None):
    font=pygame.font.Font(None,42)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))
    pygame.draw.rect(screen, blue, (xpo-border,ypo-border,width,height),3)
    return Rect(xpo,ypo,height,width)

# define function for printing text in a specific place with a specific colour
def make_label(text, xpo, ypo, fontsize, colour):
    font=pygame.font.Font(None,fontsize)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))

# Define each button press action
def button(number):
    print "You pressed button ",number

    if number == 1:
        time.sleep(5) #do something interesting here
        sys.exit()

    if number == 2:
        time.sleep(5) #do something interesting here
        sys.exit()

    if number == 3:
        time.sleep(5) #do something interesting here
        sys.exit()

    if number == 4:
        time.sleep(5) #do something interesting here
        sys.exit()

    if number == 5:
        time.sleep(5) #do something interesting here
        sys.exit()

    if number == 6:
        time.sleep(5) #do something interesting here
        sys.exit()

    if number == 7:
        time.sleep(5) #do something interesting here
        sys.exit()

    if number == 8:
        time.sleep(5) #do something interesting here
        sys.exit()

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

# Set up the base menu you can customize your menu with the colors above

#set size of the screen
size = width, height = 320, 240
border = 10
screen = pygame.display.set_mode(size)

# Background Color
screen.fill(black)

# Outer Border
pygame.draw.rect(screen, blue, (0,0,width,height),10)

button_width = (width - 4*border)/2
button_height = (height - 4*border)/4
pad = width/16
nRows = 4
nCols = 2

buttons = []
def dummy_function(n):
    print "Button %d pushed"%(n)
for row in range(0,nRows):
    for col in range(,nCols):
        b = Button(pad*(col+1)+button_width*col,pad*(row+1)+button_height*row,button_width, button_height, dummy_function)
        buttons.append(b)

# # Buttons and labels
# # First Row
# make_button("Menu Item 1", 30, 30, 55, 210, blue)
# make_button("Menu Item 2", 260, 30, 55, 210, blue)
# # Second Row
# make_button("Menu Item 3", 30, 105, 55, 210, blue)
# make_button("Menu item 4", 260, 105, 55, 210, blue)
# # Third Row
# make_button("Menu item 5", 30, 180, 55, 210, blue)
# make_button("Menu item 6", 260, 180, 55, 210, blue)
# # Fourth Row
# make_button("Menu item 7", 30, 255, 55, 210, blue)
# make_button("Menu item 8", 260, 255, 55, 210, blue)

# While loop to manage touch screen inputs


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
            pygame.draw.circle(screen, white, pos, 2, 0) #for debugging purposes - adds a small dot where the screen is pressed
            on_touch()

#ensure there is always a safe way to end the program if the touch screen fails

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    pygame.display.update()
