import pygame  #importing necessary library, the CircleShape class from circleshape.py, and all magic numbers from constants
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):  #creating Shot subclass of CircleShape
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):  #method to draw an individual shot
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):  #method to update shot position
        self.position += (self.velocity * dt)