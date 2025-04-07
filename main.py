import sys  #importing necessary libraries, classes, and all magic numbers from constants.py
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"  #hiding pygame prompt on progam load, must be done before we import pygame
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from powerup import Powerup
from overlay import *
from explosion import Explosion
from background import *

def main():  #primary function designed to run asteroids
    pygame.init()  #initializing all imported pygame modules

    #creating and assigning groups to manage objects
    updatable = pygame.sprite.Group()
    wrapable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable, wrapable)
    Asteroid.containers = (asteroids, updatable, drawable, wrapable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable, wrapable)
    Explosion.containers = (updatable, drawable)
    Powerup.containers = (powerups, updatable, drawable, wrapable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #creating game window
    pygame.display.set_caption("Asteroids")
    font = pygame.font.Font(None, SCOREBOARD_FONT_SIZE)  #creating a font object for overlays
   
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  #creating player model
    asteroid_field = AsteroidField()  #creating the object that generates and controls asteroids
    point_counter = 0  #keeps track of score

    fps = pygame.time.Clock()  #creating in-game clock to restrict framerate
    dt = 0

    print("Starting Asteroids!")

    while True:  #running asteroids
        for event in pygame.event.get():  #enabling close button in window
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)  #updating objects
        for object in wrapable:
            object.wrap()

        for asteroid in asteroids:  #checking for player collision
            if player.collision(asteroid):
                if player.invuln_timer == 0:
                    explosion = Explosion(player.position.x, player.position.y, player.radius * 1.5)
                    if player.lives == 0:
                        print(f"Final score: {point_counter}")
                        print("Game over!")
                        sys.exit()
                player.respawn()
            
            for shot in shots:  #checking for shot collision and updating score
                if shot.collision(asteroid):
                    shot.collide()
                    explosion = Explosion(asteroid.position.x, asteroid.position.y, asteroid.radius)
                    point_counter += asteroid.split()

        for powerup in powerups:  #checking for powerup pickups
            if player.collision(powerup):
                player.pickup(powerup)
                asteroid_field.item_counter -= 1
                    
        #redrawing game display
        get_background(screen)

        for object in drawable:
            object.draw(screen)

        display_score(screen, font, point_counter)
        display_lives(screen, font, player.lives)
        display_bombs(screen, font, player.bomb_count)
        display_shield(screen, font, player.have_shield)
        display_weapon_timer(screen, font, player.weapon_type, player.weapon_timer)

        pygame.display.flip()  #refreshing game window
        
        dt = (fps.tick(60) / 1000)  #delaying game loop by 1/60th of a second


if __name__ == "__main__":  #call to main that runs asteroids when this file is run directly
    main()