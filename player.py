import pygame  #importing necessary libraries, classes, and constants
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):  #creating player subclass of CircleShape
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.lives = 3
        self.invuln_timer = PLAYER_INVULN_TIMER
        self.acceleration = 0

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
        self.shot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w] and not keys[pygame.K_s]:
            self.acceleration += 0.04
        if keys[pygame.K_s] and not keys[pygame.K_w]:
            self.acceleration -= 0.02

        self.move(dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        if self.invuln_timer > 0:
            self.invuln_timer -= 1        

    def move(self, dt):  #method to adjust player position and acceleration
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if self.acceleration > 1:
            self.acceleration = 1
        if self.acceleration < -0.5:
            self.acceleration = -0.5

        self.position += forward * PLAYER_SPEED * self.acceleration * dt

        if self.acceleration > 0:
            self.acceleration -= 0.01
        if self.acceleration < 0:
            self.acceleration += 0.01

    def shoot(self):  #method to create shots from the player
        if self.shot_timer > 0:
            return
        self.shot_timer = PLAYER_SHOOT_COOLDOWN

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x + forward.x * self.radius, self.position.y + forward.y * self.radius)
        shot.velocity = forward * PLAYER_SHOOT_SPEED

    def respawn(self):  #method to respawn the player if they are destroyed
        if self.invuln_timer > 0:
            return

        self.invuln_timer += PLAYER_INVULN_TIMER
        self.lives -= 1
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.velocity = pygame.Vector2(0, 0)