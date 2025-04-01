import pygame  #importing necessary libraries, CircleShape class from circleshape.py, and all magic numbers from constants.py
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):  #creating Asteroid subclass of CircleShape
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):  #method to draw an individual asteroid
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):  #method to move an asteroid once created
        self.position += (self.velocity * dt)

    def split(self):  #method to split asteroids above the minimum size into two smaller asteroids
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = self.velocity.rotate(random.uniform(20, 50))
        random_neg_angle = self.velocity.rotate(-random.uniform(20, 50))
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = random_angle * 1.2

        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = random_neg_angle * 1.2