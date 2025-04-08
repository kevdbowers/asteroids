import pygame  #importing pygame library, CircleShape class from circleshape.py and all magic numbers from constants.py
from circleshape import CircleShape
from constants import *

class Shield(CircleShape):  #creating Shield subclass of CircleShape
    def __init__(self, x, y):
        super().__init__(x, y, SHIELD_RADIUS)
    
    def draw(self, screen):  #method to draw shield visual
        pygame.draw.circle(screen, "cyan4", self.position, self.radius, 4)