import pygame  #importing pygame library
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):  #creating the CircleShape class as a pygame sprite
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision(self, object):  #method to check for collisions between CircleShape objects
        return self.position.distance_to(object.position) < (self.radius + object.radius)
    
    def wrap(self):  #method to wrap objects around the display border
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0