import pygame  #importing pygame library

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

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, object):  #method to check for collisions between CircleShape objects
        return self.position.distance_to(object.position) < (self.radius + object.radius)