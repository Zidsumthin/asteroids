from circleshape import *
from constants import *
import pygame

class Shots(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        draw_color = (255,255,255)
        draw_width = 2

        pygame.draw.circle(screen, draw_color, self.position, self.radius, draw_width)

    def update(self, dt):
        self.position += (self.velocity * dt)