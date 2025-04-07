import pygame  #importing necessary libraries, CircleShape class from circleshape.py, and all magic numbers from constants.py
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):  #creating Asteroid subclass of CircleShape
    def __init__(self, x, y, radius, point_value = 1):
        super().__init__(x, y, radius)
        self.point_value = point_value
        self.has_split = False

    def draw(self, screen):  #method to draw an individual asteroid
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):  #method to move an asteroid once created
        self.position += (self.velocity * dt)

    def wrap(self):  #overriding parent wrap method with asteroidfield class dimensions
        if self.position.x < -ASTEROID_MAX_RADIUS:
            self.position.x = ASTEROID_MAX_RADIUS + SCREEN_WIDTH
        if self.position.x > ASTEROID_MAX_RADIUS + SCREEN_WIDTH:
            self.position.x = -ASTEROID_MAX_RADIUS
        if self.position.y < -ASTEROID_MAX_RADIUS:
            self.position.y = ASTEROID_MAX_RADIUS + SCREEN_HEIGHT
        if self.position.y > ASTEROID_MAX_RADIUS + SCREEN_HEIGHT:
            self.position.y = -ASTEROID_MAX_RADIUS

    def split(self):  #method to split asteroids above the minimum size into two smaller asteroids
        if self.has_split == True:
            return 0
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return self.point_value
        
        new_point_value = self.point_value * 2
        random_angle = self.velocity.rotate(random.uniform(20, 50))
        random_neg_angle = self.velocity.rotate(-random.uniform(20, 50))
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius, new_point_value)
        asteroid_one.velocity = random_angle * ASTEROID_SPLIT_ACCELERATOR

        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius, new_point_value)
        asteroid_two.velocity = random_neg_angle * ASTEROID_SPLIT_ACCELERATOR

        self.has_split = True

        return self.point_value