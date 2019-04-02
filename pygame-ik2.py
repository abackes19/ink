# using cursor!
import pygame
import math
import fractions
import time
pygame.init()
pygame.font.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (137, 169, 244)
purple = (232, 13, 119)
grey = (99,99,99)

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill(white)
font = pygame.font.SysFont("comicsansms", 50)
clock = pygame.time.Clock()

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green

originx = 400
originy = 300
d_one = 107 # the distance from shoulder to elbow
d_two = 84 # distance from elbow to wrist

pygame.mouse.set_pos(originx+d_two,originy-d_one)
xm, ym = pygame.mouse.get_pos()
pygame.draw.line(gameDisplay, blue, (originx, originy), (xm, ym),5)
text = font.render(str(xm), True, (blue))

pygame.draw.circle(gameDisplay, grey, (originx, originy), (d_one + d_two), 0)
pygame.draw.circle(gameDisplay, white, (originx, originy), (d_one - d_two), 0)



def ik(xm, ym):
    import math
    text = font.render("Yikes", True, (blue))
    y = originy - ym
    x = xm - originx

    sqd_one = d_one ** 2
    sqd_two = d_two ** 2

    d_three = math.sqrt((y**2) + (x**2)) # determining distance from shoulder to wrist ^
    if d_one - d_two < d_three < d_one + d_two:
        a_three = math.acos((sqd_one + sqd_two - ((y**2) + (x ** 2))) / (2 * d_one * d_two))
        a_two = math.asin((d_two * math.sin(a_three) / d_three)) # angle between shoulder and wrist
        a_four = math.atan2(y , x) # angle between 0 line and wrist
        a_shoulder = (a_four + a_two)  # shoulder angle?
        a_elbow = a_three

        xe = d_one * math.cos(a_shoulder) + originx
        ye = originy - (d_one * math.sin(a_shoulder))
        return xe, ye
    else:
        return False


    gameDisplay.blit(text, (100, 100))
    pygame.display.flip()

done = False


while not done:
    clock.tick(60)

    # determine where want to be
    x, y = pygame.mouse.get_pos()
    # can reach?
    if ik(x, y) != False:
        # determine elbow point
        xm, ym = pygame.mouse.get_pos()
        xe, ye = ik(xm,ym)
        # draw line
        pygame.draw.lines(gameDisplay, blue, False, [[originx,originy], [xe, ye], [xm, ym]], 5)
    else: # out of range so stay
        pygame.draw.lines(gameDisplay, purple, False, [[originx,originy], [xe, ye], [xm, ym]], 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # update and redraw background
    pygame.display.update()
    gameDisplay.fill(grey)
    pygame.draw.circle(gameDisplay, white, (originx, originy), (d_one + d_two), 0)
    pygame.draw.circle(gameDisplay, grey, (originx, originy), (d_one - d_two), 0)


pygame.quit()
