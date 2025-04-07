import pygame  #importing necessary library, the CircleShape class from circleshape.py, and all magic numbers from constants
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):  #creating Shot subclass of CircleShape
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.forward = pygame.Vector2(0, 1).rotate(0)
        self.distance_travelled = 0

    def draw(self, screen):  #method to draw an individual shot
        pygame.draw.circle(screen, "white", self.position, self.radius, 0)

    def update(self, dt):  #method to update shot position and limit shot travel distance
        self.position += self.velocity * dt
        self.distance_travelled += PLAYER_SHOOT_SPEED * dt
        if self.distance_travelled > max(SCREEN_WIDTH, SCREEN_HEIGHT):
            self.collide()

    def collide(self):  #method to kill asteroid and check for shot explosion
        self.kill()
        if self.radius > SHOT_RADIUS:
            self.explode()

    def explode(self):  #method to create an explosion of smaller shots
        for i in range(0, 8):
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = self.forward.rotate(i * 45) * PLAYER_SHOOT_SPEED / 3