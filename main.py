import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player
from shot import Shot
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
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable,drawable,asteroids)
    
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,drawable, updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
   
    asteroid_field = AsteroidField()

    # 3 common steps for the game loop:
    # check for player inputs
    while run:
        dt = clock.tick(60) / 1000

        for sprite in updatable:
            sprite.update(dt)

        screen.fill('black')
        
        for asteroid in asteroids:
            if(asteroid.check_collision(player)):
                print("Player collided! Game Over")
                run = not run
            for shot in shots:
                if(asteroid.check_collision(shot)):
                    asteroid.split()
                    shot.kill()

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



