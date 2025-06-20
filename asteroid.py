import pygame
from constants import *
from player import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0,0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        random_angle = random.uniform(20, 50)

        direction1 = self.velocity.rotate(random_angle) * 1.2
        direction2 = self.velocity.rotate(-random_angle) * 1.2
        
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = direction1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = direction2
