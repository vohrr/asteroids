import pygame
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS, ASTEROID_KINDS 
from circleshape import CircleShape


class Asteroid(CircleShape):


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
         
