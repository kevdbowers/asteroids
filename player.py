import pygame  #importing necessary libraries, classes, and constants
from circleshape import CircleShape
from shot import Shot
from constants import *

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

    def rotate(self, dt):  #method to rotate player visual
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):  #method to update player location/direction/action based on user input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):  #method to adjust player position
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):  #method to create shots from the player
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED