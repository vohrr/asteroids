import pygame
from constants import *

def main(): 
    print("Starting asteroids!")
    pygame.init()
    pygame.display.set_caption('Asteroids')
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True 
    
    # 3 common steps for the game loop:
    # check for player inputs
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = not run
        # draw the game to the screen

        screen.fill('black')
        # update the game world
        pygame.display.flip()
        dt += clock.tick(60)


if __name__ == "__main__":
    main()



