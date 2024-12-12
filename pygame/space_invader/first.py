# packages
import pygame



print("welcome to pygame!")

#  initialize the pygame
pygame.init()


# creating the screen 
screen  = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)



# game loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    # rgb = red green blue
screen.fill((255,0,0))