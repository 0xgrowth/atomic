import pygame
from pygame.locals import *
import random

# --- THIS CODE WAS WRITTEN BY 0xgrowth.
# --- SEND ME A DM ON TWITTER.
# --- AVAILABLE FOR COLLABORATIONS AND PAID JOBS

pygame.init()
size = (900, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Atomic Particles movement by 0xgrowth")

icon = pygame.image.load('ball.png')
pygame.display.set_icon(icon)


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
WHITE = (255, 255, 255)
# ---------------------------------------
# Functions for each color to be displayed as screen color.

def screen_color():
    screen.fill(BLACK)

# --------------------------

# colors = [red_display,blue_display,green_display,cyan_display,gray_display,black_display,yellow_display,magenta_display]

#ball one
ball = []
a_pos = []
b_pos = []
apos_change = []
bpos_change = []
num_of_ball = 10000

for i in range(num_of_ball) :
    bal = pygame.image.load('ball.png')
    small_ball = pygame.transform.scale(bal, (3,3))
    ball.append(small_ball)
    # horizontal(x) position of snowballs
    a_pos.append(random.randint(10, 895))

    # vertical(x) position of snowballs
    b_pos.append(random.randint(5, 698))

    # constants for ball speed 
    apos_change.append(2)
    bpos_change.append(2)

def ballImg(a,b,i) :
    screen.blit(ball[i], (a,b))

# fonts = pygame.font.get_fonts()
# for f in fonts:
#     print(f)
# ---------------
# running = True
# while running: 
# ---------------
# The above block of code also works

while True:
    screen_color()

    # --- snowball movements
    for i in range(num_of_ball) :
        a_pos[i] += apos_change[i]
        b_pos[i] += bpos_change[i]

    # --- bouncing effect with  screen boundaries
        if b_pos[i] >= 698 :
            bpos_change[i] = -2
        elif b_pos[i] <= 10 :
            bpos_change[i] = +2

        if a_pos[i] >= 895 :
            apos_change[i] = -2
        elif a_pos[i] <= 10 :  
            apos_change[i] = +2

    # ---  
 
    # --- calling the functions for atomic motion
        ballImg(a_pos[i],b_pos[i], i)
        ballImg_one(c_pos[i],d_pos[i], i)
    # ---

    # --- EVENT HANDLERS 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # ---

    pygame.display.update()        