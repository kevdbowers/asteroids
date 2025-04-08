import pygame  #importing necessary libraries, classes, and all magic numbers from constants
import random
from asteroid import Asteroid
from powerup import Powerup
from constants import *


class AsteroidField(pygame.sprite.Sprite):  #creating the AsteroidField class as a pygame Sprite
    edges = [  #defining the border of the AsteroidField based on screen and asteroid max size
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.asteroid_spawn_timer = 0.0
        self.item_spawn_timer = 0.0
        self.item_counter = 0

    def spawn_asteroid(self, radius, position, velocity):  #method to create a new asteroid
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def spawn_item(self, position, velocity, kind):  #method to create a new item
        if 0 <= kind <= 1:
            item_type = "triple_shot"
            item_color = "indigo"
            item_text = "Ts"
        elif 2 <= kind <= 3:
            item_type = "scatter_shot"
            item_color = "green4"
            item_text = "Ss"
        elif 4 <= kind <= 5:
            item_type = "exploding_shot"
            item_color = "darkorange2"
            item_text = "Es"
        elif kind == 6:
            item_type = "bomb"
            item_color = "red"
            item_text = "B"
        elif kind == 7:
            item_type = "shield"
            item_color = "cyan3"
            item_text = "S"
        else:
            return
        
        self.item_counter += 1
        powerup = Powerup(position.x, position.y, item_type, item_color, item_text)
        powerup.velocity = velocity

    def update(self, dt):  #method to update the AsteroidField with new asteroids and move them
        self.asteroid_spawn_timer += dt
        self.item_spawn_timer += dt

        if self.asteroid_spawn_timer > ASTEROID_SPAWN_RATE:
            self.asteroid_spawn_timer = 0

            #spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn_asteroid(ASTEROID_MIN_RADIUS * kind, position, velocity)

        if (self.item_spawn_timer > ITEM_SPAWN_RATE and self.item_counter < 2) or (self.item_spawn_timer > ITEM_SPAWN_RATE * 2 and self.item_counter < 3):
            self.item_spawn_timer = 0

            #spawn a new item at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(80, 200)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(0, 9)
            self.spawn_item(position, velocity, kind)