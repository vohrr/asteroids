import pygame
from player import Player
from constants import *

def main(): 
    print("Starting asteroids!")
    pygame.init()
    pygame.display.set_caption('Asteroids')
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True 
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    # 3 common steps for the game loop:
    # check for player inputs
    while run:
        screen.fill('black')
        player.update(dt)
        player.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = not run
        # draw the game to the screen

        # update the game world
        pygame.display.flip()
        dt += clock.tick(60)


if __name__ == "__main__":
    main()



