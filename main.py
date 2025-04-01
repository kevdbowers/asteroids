import sys  #importing necessary libraries, classes, and all magic numbers from constants.py
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():  #primary function designed to run asteroids
    pygame.init()  #initializing all imported pygame modules

    #creating and assigning groups to manage objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #creating game window
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  #creating player model
    asteroid_field = AsteroidField()  #creating the object that generates and controls asteroids

    fps = pygame.time.Clock()  #creating in-game clock to restrict framerate
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:  #running asteroids
        for event in pygame.event.get():  #enabling close button in window
            if event.type == pygame.QUIT:
                return

        #updating game screen visually 
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()  #refreshing game window

        dt = (fps.tick(60) / 1000)  #delaying game loop by 1/60th of a second


if __name__ == "__main__":  #call to main that runs asteroids when this file is run directly
    main()