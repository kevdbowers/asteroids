import pygame  #importing necessary library and CircleShape class from circleshape.py
from circleshape import CircleShape

class Asteroid(CircleShape):  #creating Asteroid subclass of CircleShape
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.center = (x, y)
        self.radius = radius

    def draw(self, screen):  #method to draw an individual asteroid
        pygame.draw.circle(screen, "white", self.center, self.radius, 2)

    def update(self, dt):  #method to move an asteroid once created
        self.center += (self.velocity * dt)