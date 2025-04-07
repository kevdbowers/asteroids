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
        self.weapon_type = None
        self.weapon_timer = 0

        self.forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

    def triangle(self):  #method to define player visual
        a = self.position + self.forward * self.radius
        b = self.position - self.forward * self.radius - self.right
        c = self.position - self.forward * self.radius + self.right
        return [a, b, c]
    
    def draw(self, screen):  #method to draw player visual
        pygame.draw.polygon(screen, "azure4", self.triangle(), 0)

    def rotate(self, dt):  #method to rotate player visual
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):  #method to update player location/direction/action based on user input
        self.forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
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
            if self.weapon_type == None:
                self.shoot(self.position)
            if self.weapon_type == "triple_shot":
                self.triple_shot()
            if self.weapon_type == "scatter_shot":
                self.scatter_shot()
            if self.weapon_type == "exploding_shot":
                self.exploding_shot()
        
        if self.invuln_timer > 0:
            self.invuln_timer -= 1        

    def move(self, dt):  #method to adjust player position and acceleration
        if self.acceleration > 1:
            self.acceleration = 1
        if self.acceleration < -0.5:
            self.acceleration = -0.5

        self.position += self.forward * PLAYER_SPEED * self.acceleration * dt

        if self.acceleration >= 0.01:
            self.acceleration -= 0.01
        if self.acceleration <= -0.01:
            self.acceleration += 0.01
        if -0.01 < self.acceleration < 0.01:
            self.acceleration = 0

    def shoot(self, position, rotation=0, shot_radius=SHOT_RADIUS):  #method to create shots from the player
        if self.shot_timer > 0:
            return

        shot_origin_x = position.x + self.forward.x * self.radius
        shot_origin_y = position.y + self.forward.y * self.radius
        shot = Shot(shot_origin_x, shot_origin_y, shot_radius)
        shot.velocity = self.forward.rotate(rotation) * PLAYER_SHOOT_SPEED

        if self.weapon_type == None:
            self.shot_timer = PLAYER_SHOOT_COOLDOWN

    def triple_shot(self):  #method to fire a triple shot
        if self.shot_timer > 0:
            return

        left_position = self.position - self.forward * self.radius - self.right * 1.5 
        right_position = self.position - self.forward * self.radius + self.right * 1.5
        self.shoot(self.position)
        self.shoot(left_position)
        self.shoot(right_position)
        self.shot_timer = PLAYER_SHOOT_COOLDOWN * (3/2)

    def scatter_shot(self):  #method to fire a scatter shot
        if self.shot_timer > 0:
            return

        self.shoot(self.position)
        self.shoot(self.position, 15)
        self.shoot(self.position, -15)
        self.shoot(self.position, 30)
        self.shoot(self.position, -30)

        self.shot_timer = PLAYER_SHOOT_COOLDOWN * (5/2)

    def exploding_shot(self):  #method to fire an exploding shot
        if self.shot_timer > 0:
            return
        
        self.shoot(self.position, 0, SHOT_RADIUS * 3)

        self.shot_timer = PLAYER_SHOOT_COOLDOWN * (8/2)

    def respawn(self):  #method to respawn the player if they are destroyed
        if self.invuln_timer > 0:
            return

        self.invuln_timer += PLAYER_INVULN_TIMER
        self.lives -= 1
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.velocity = pygame.Vector2(0, 0)