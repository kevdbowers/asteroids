import pygame  #importing pygame library, Circleshape class from circleshape.py, and all magic numbers from constants
from circleshape import CircleShape
from constants import *

class Powerup(CircleShape):  #creating Powerup subclass of Circleshape
    def __init__(self, x, y, item_type, item_color, item_text):
        super().__init__(x, y, ITEM_RADIUS)
        self.name = item_type
        self.color = item_color
        self.text = item_text

    def draw(self, screen):  #method to draw item visual
        pygame.draw.circle(screen, self.color, self.position, self.radius)
        font = pygame.font.Font(None, ITEM_FONT_SIZE)
        letter_text = font.render(f"{self.text}", True, "white")
        letter_box = letter_text.get_rect()
        letter_box.center = self.position
        screen.blit(letter_text, letter_box)

    def update(self, dt):  #method to update item object
        self.position += self.velocity * dt