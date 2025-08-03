from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        draw_color = (255,255,255)
        draw_width = 2

        pygame.draw.circle(screen, draw_color, self.position, self.radius, draw_width)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)
        self.radius -= ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position[0], self.position[1], self.radius / 2)
        new_asteroid2 = Asteroid(self.position[0], self.position[1], self.radius / 2)
        new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, split_angle)*1.2
        new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -split_angle)*1.2
        