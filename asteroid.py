import pygame
import random
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS, ASTEROID_KINDS 
from circleshape import CircleShape

class Asteroid(CircleShape):


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # a large asteroid splits into 2 medium asteroids
        # a medium asteroid splits into 2 small asteroids
        if(self.radius > ASTEROID_MIN_RADIUS):
            new_radius = (self.radius / ASTEROID_MIN_RADIUS - 1) * ASTEROID_MIN_RADIUS
            split_angle = random.uniform(20, 50)
            split_1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            split_1.velocity = self.velocity.rotate(split_angle) * 1.2
            split_2.velocity = self.velocity.rotate(-split_angle) * 1.2
        #destroy the current asteroid
        self.kill()
