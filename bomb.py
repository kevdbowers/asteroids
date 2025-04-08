import pygame
from circleshape import CircleShape
from constants import *

class Bomb(CircleShape):  #create Bomb subclass of CircleShape
    def __init__(self, x, y, radius=0):
        super().__init__(x, y, radius)

    def draw(self, screen):  #method to draw bomb visual
        pygame.draw.circle(screen, "red3", self.position, self.radius, 10)

    def update(self, dt):  #method to update bomb object
        if self.radius <= BOMB_RADIUS: 
            self.radius += BOMB_RADIUS * dt
        else:
            self.kill()