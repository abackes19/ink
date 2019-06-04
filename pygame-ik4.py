# using arrow keys! also multiple angles! sideview and topview
# notes: can use continuously, but use one key at a time in an orderly fashion

# able to change z coordinate, and see change on topview.
# z is a plane, w is a dummy plane
# Next is elbow joint


import pygame, math, fractions, time
from pygame.locals import *

pygame.init()


white = (255,255,255); black = (0,0,0)
red = (255,0,0); green = (39, 147, 52)
blue = (102, 136, 214); pink = (232, 13, 119)
grey = (203, 206, 214)

display_width = 1000
display_height = 450
screen = pygame.display.set_mode((display_width,display_height))
screen.fill(white)
clock = pygame.time.Clock()

step = 2
originx = 250
originy = 250
d_one = 124 # the distance from shoulder to elbow
d_two = 96 # distance from elbow to wrist
toriginz = 725
toriginw = 250

xm, ym = d_two, d_one
x, y = d_two, d_one
z = 0
w = d_two
xo = x
yo = y
x_change = 0
y_change = 0
z_change = 0
td_one = d_one + d_two

done = False
# ^^^ that all would be the setup



def ik(x, y, z): # here is where we do math

    sqd_one = d_one ** 2
    sqd_two = d_two ** 2

    d_three = math.sqrt((y**2) + (x**2))# determining distance from shoulder to wrist ^
    if d_three < d_one + d_two and d_three > d_one - d_two and y > -24:

        a_three = math.acos((sqd_one + sqd_two - ((y**2) + (x ** 2))) / (2 * d_one * d_two))
        a_two = math.asin((d_two * math.sin(a_three) / d_three)) # angle between shoulder and wrist
        a_four = math.atan2(y , x) # angle between 0 line and wrist
        a_shoulder = (a_four + a_two)  # shoulder angle?
        a_elbow = a_three


        a_swivel = math.atan2(round(z, 2), round(x, 2))
        xe = d_one * math.cos(a_shoulder)
        ye = (d_one * math.sin(a_shoulder))
        ze = (xe * math.tan(a_swivel))
        return xe, ye, ze
    else:
        return False

    pygame.display.flip()

def pos(x, y, z):
    x_change = 0
    y_change = 0
    z_change = 0

    if event.type == pygame.KEYDOWN:
        # what key are they pressing? move accordingly
        if event.key == pygame.K_ESCAPE:
            done=True
            return done
        elif event.key == pygame.K_a:
            x_change = -step
        elif event.key == pygame.K_d:
            x_change = step
        elif event.key == pygame.K_w:
            y_change = step
        elif event.key == pygame.K_s:
            y_change = -step
        elif event.key == pygame.K_q:
            z_change = step
        elif event.key == pygame.K_e:
            z_change = -step

    return x_change, y_change, z_change

while not done:
    clock.tick(60)
    # determine where want to be
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        else: # did something other than close
            x_change, y_change, z_change = pos(x,y,z) # figure out the change


    # move

    x += x_change
    y += y_change
    z += z_change

    if x_change and z_change == 0:
        w = math.sqrt((x**2) - (z**2))

    if x_change != 0:
        w = math.sqrt((x**2) - (z**2))
    elif z_change != 0:
        x = math.sqrt((w**2) + (z**2))


    if ik(x, y, z) != False:
        # determine elbow point
        xe, ye, ze = ik(x,y,z)
        xo = x + originx; yo = originy - y; zo = toriginz + z
        xe = xe + originx; ye = originy - ye; ze = toriginz + ze

        pxe = toriginw - (xe - originx)


        # draw line
        pygame.draw.lines(screen, blue, False, [[originx,originy], [xe, ye], [xo, yo]], 5) # sideview

        pygame.draw.line(screen, blue, (toriginz, toriginw), [(zo), (toriginw - w)], 5)
        pygame.draw.line(screen, green, (toriginz, toriginw), (ze, pxe), 5)
    else: # out of range so stay
        pygame.draw.lines(screen, pink, False, [[originx,originy], [xe, ye], [xo, yo]], 5)
#        pygame.draw.circle(screen, pink, (x + originx, originy - y), (5), 0)

# Be IDLE friendly
    pygame.display.update()
    screen.fill(grey)
    pygame.draw.circle(screen, white, (originx, originy), (d_one + d_two), 0)
    pygame.draw.circle(screen, grey, (originx, originy), (d_one - d_two), 0)
    # topview
    pygame.draw.circle(screen, white, (toriginz, toriginw), (d_one + d_two), 0)
    pygame.draw.circle(screen, grey, (toriginz, toriginw), (10), 0)
    pygame.draw.rect(screen, grey, [0, (originy + 24), display_width, display_width])

#please work rectangle
pygame.quit()
