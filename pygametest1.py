import pygame
import math

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
done = False

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (50,150,50)
blue = (50,0,200)

font = pygame.font.SysFont("comicsansms", 50)

display_width = 800
display_height = 600

originx = 400
originy = 300
d_one = 100 # the distance from shoulder to elbow
d_two = 100 # distance from elbow to wrist


pygame.mouse.set_pos(originx+d_two,originy-d_one)
xm, ym = pygame.mouse.get_pos()

y = originy - ym
x = xm - originx

text = font.render(str(xm), True, (blue))

sqd_one = d_one ** 2
sqd_two = d_two ** 2

d_three = math.sqrt((y**2) + (x**2)) # determining distance from shoulder to wrist ^
a_three = math.acos((sqd_one + sqd_two - ((y**2) + (x ** 2))) / (2 * d_one * d_two))
a_two = math.asin((d_two * math.sin(a_three) / d_three)) # angle between shoulder and wrist
a_four = math.atan2(y , x) # angle between 0 line and wrist
a_shoulder = (a_four + a_two) # shoulder angle?
a_elbow = a_three

xm = d_one * math.cos(a_shoulder) + originx
ym = originy - (d_one * math.sin(a_shoulder))


text2 = font.render(str(xm), True, (green))
text3 = font.render(str(math.cos(a_shoulder)), True, (green))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    gameDisplay.fill((255, 255, 255))
    gameDisplay.blit(text, (100, 300))
    gameDisplay.blit(text3, (100, 100))
    gameDisplay.blit(text2, (100, 200))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
