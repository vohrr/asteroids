import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
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
    
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
   
    asteroidField = AsteroidField()

    # 3 common steps for the game loop:
    # check for player inputs
    while run:
        dt = clock.tick(60) / 1000

        for sprite in updatable:
            sprite.update(dt)
       
        screen.fill('black')

        for sprite in drawable:
            sprite.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = not run
        # draw the game to the screen

        # update the game world
        pygame.display.flip()
        


if __name__ == "__main__":
    main()



