import pygame
from pygame.locals import *
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (137, 169, 244)

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill(white)
clock = pygame.time.Clock()


y = 300
x = 400
x_change = 0
y_change = 0

pygame.draw.circle(gameDisplay, blue, (x, y), (5), 0)


done = False

while not done:
    clock.tick(10)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -5
            elif event.key == pygame.K_d:
                x_change = 5
            elif event.key == pygame.K_w:
                y_change = -5
            elif event.key == pygame.K_s:
                y_change = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                y_change = 0
        x += x_change
        y += y_change
        gameDisplay.fill(white)
        pygame.draw.circle(gameDisplay, blue, (x, y), (5), 0)
        pygame.display.update()
    pygame.draw.rect(gameDisplay, blue, [0, (originy + 24), 100, display_width])



# Be IDLE friendly
pygame.quit()
