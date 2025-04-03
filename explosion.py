import pygame  #importing pygame library, Circleshape class from circleshap.py, and all magic numbers from constants.py
from circleshape import CircleShape
from constants import *

class Explosion(CircleShape):  #creating Explosion subclass of CircleShape
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.images = []
        for num in range(1, 10):  #loading images create an explosion visual effect
            img = pygame.image.load(f"explosion_images/explosion{num}.png")  #filepath to the images used for explosion visual
            img = pygame.transform.scale(img, (radius * 3, radius * 3))
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.bottomright = (x, y)
        self.counter = 0

    def update(self, dt):  #method to update explosion visual
        self.counter += 1

        if self.counter >= EXPLOSION_SPEED and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.counter >= EXPLOSION_SPEED and self.index >= len(self.images) - 1:
            self.kill()

    def draw(self, screen):  #method to display explosion visual
        screen.blit(self.image, self.rect.center)