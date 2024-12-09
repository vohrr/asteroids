import pygame
from constants import *

def main(): 
    print("Starting asteroids!")
    pygame.init()
    pygame.display.set_caption('Asteroids')
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    
    # 3 common steps for the game loop:
    # check for player inputs
    while True:
        
        # draw the game to the screen

        screen.fill('black')
        # update the game world
        pygame.display.flip()


if __name__ == "__main__":
    main()



