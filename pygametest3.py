import pygame
from pygame.locals import *

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (137, 169, 244)

x = 50
x_change = 0


done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -1
                print(x)
            elif event.key == pygame.K_d:
                x_change = 1
                print(x)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_change = 0
        x += x_change



# Be IDLE friendly
pygame.quit()
