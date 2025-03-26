import pygame  #importing necessary libraries, classes, and constants
from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Player(CircleShape):  #creating player subclass of CircleShape
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):  #method to define player visual
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):  #method to draw player visual
        pygame.draw.polygon(screen, "white", self.triangle(), 2)