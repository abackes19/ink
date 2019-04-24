# using arrow keys!
# notes: can use continuously, but use one key at a time in an orderly fashion

import RoboPiLib3 as RPL
import setup3
import pygame, math, fractions, time
from pygame.locals import *


pygame.init()


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (39, 147, 52)
blue = (102, 136, 214)
pink = (232, 13, 119)
grey = (203, 206, 214)

display_width = 500
display_height = 500
gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill(white)
clock = pygame.time.Clock()

step = 4
originx = 250
originy = 250
d_one = 90 # the distance from shoulder to elbow
d_two = 95 # distance from elbow to wrist

pygame.draw.circle(gameDisplay, grey, (originx, originy), (d_one + d_two), 0)
pygame.draw.circle(gameDisplay, white, (originx, originy), (d_one - d_two), 0)
xm, ym = originx+d_two, originy-d_one
pygame.draw.line(gameDisplay, blue, (originx, originy), (xm, ym),5)
pygame.display.update()

x, y = originx+d_two, originy-d_one
xo = x
yo = y
x_change = 0
y_change = 0

s_pin = 1
e_pin = 0
input_shoulder = 2400
input_elbow = 1400
a_shoulder = 90
a_elbow = 90


# ^^^ that all would be the setup

done = False
clock = pygame.time.Clock()


def ik(xm, ym): # here is where we do math
    y = originy - ym
    x = xm - originx

    sqd_one = d_one ** 2
    sqd_two = d_two ** 2

    d_three = math.sqrt((y**2) + (x**2)) # determining distance from shoulder to wrist ^
    if d_one - d_two < d_three < d_one + d_two and y > -24:
        a_three = math.acos((sqd_one + sqd_two - ((y**2) + (x ** 2))) / (2 * d_one * d_two))
        a_two = math.asin((d_two * math.sin(a_three) / d_three)) # angle between shoulder and wrist
        a_four = math.atan2(y , x) # angle between 0 line and wrist
        a_shoulder = (a_four + a_two)  # shoulder angle?
        a_elbow = a_three

        xe = d_one * math.cos(a_shoulder) + originx
        ye = originy - (d_one * math.sin(a_shoulder))
        return xe, ye
        return a_shoulder, a_elbow
    else:
        return False

    pygame.display.flip()


def pos(x, y):
    x_change = 0
    y_change = 0

    if event.type == pygame.KEYDOWN:
        # what key are they pressing? move accordingly
        if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
            done=True
            return done
        elif event.key == pygame.K_a:
            x_change = -step
        elif event.key == pygame.K_d:
            x_change = step
        elif event.key == pygame.K_w:
            y_change = -step
        elif event.key == pygame.K_s:
            y_change = step

    return x_change, y_change

def arm(a_shoulder, a_elbow):
    a_elbow = a_elbow * 180 / math.pi # make to degrees
    a_shoulder = a_shoulder * 180 / math.pi # make to degrees
    input_elbow = int(a_elbow * (2000/180)  + 400);
    input_shoulder = int(a_shoulder * (2000/180) + 400) #angle and motor value calculations
    return input_elbow, input_shoulder


RPL.servoWrite(s_pin, input_shoulder); RPL.servoWrite(e_pin, input_elbow)

while not done:
    clock.tick(60)
    # determine where want to be
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        else: # did something other than close
            x_change, y_change = pos(x,y) # figure out the change
    # move
    x += x_change
    y += y_change
    print(input_shoulder)
    if ik(x, y) != False:
        # determine elbow point
        xe, ye = ik(x,y)
        arm(a_shoulder, a_elbow)
        xo = x; yo = y
        # draw line
        pygame.draw.lines(gameDisplay, blue, False, [[originx,originy], [xe, ye], [xo, yo]], 5)
        RPL.servoWrite(s_pin, input_shoulder); RPL.servoWrite(e_pin, input_elbow) # inputs determined by arm()

    else: # out of range so stay
        pygame.draw.lines(gameDisplay, pink, False, [[originx,originy], [xe, ye], [xo, yo]], 5)
        pygame.draw.circle(gameDisplay, pink, (x, y), (5), 0)


    pygame.display.update()
    gameDisplay.fill(grey)
    pygame.draw.circle(gameDisplay, white, (originx, originy), (d_one + d_two), 0)
    pygame.draw.circle(gameDisplay, grey, (originx, originy), (d_one - d_two), 0)
    pygame.draw.rect(gameDisplay, grey, [0, (originy + 24), display_width, display_width])





####
pygame.quit()
