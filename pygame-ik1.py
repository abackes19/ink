import pygame

pygame.init()
pygame.font.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (50,0,200)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill(white)

clock = pygame.time.Clock()

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green

mouse = pygame.mouse.get_pos()
pygame.draw.line(gameDisplay, blue, (display_width/2,display_height/2), (mouse),5)

while True:
    mouse = pygame.mouse.get_pos()
    pygame.draw.line(gameDisplay, blue, (display_width/2,display_height/2), (mouse),5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    print(event)
    pygame.display.update()
    gameDisplay.fill(white)


pygame.quit()
quit()
