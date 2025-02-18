import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):

        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 180

    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        direction = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += direction * PLAYER_SPEED * dt
        
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 2) 

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1) 
        
        if keys[pygame.K_d]:
            self.rotate(1)

        if keys[pygame.K_w]:
            self.move(1)

        if keys[pygame.K_s]:
            self.move(-1)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


