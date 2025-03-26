import pygame  #importing necessary libraries, and all magic numbers from constants.py
from constants import *

def main():  #primary function designed to run asteroids
    pygame.init()  #initializing all imported pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #creating game window

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:  #running asteroids
        for event in pygame.event.get():  #enabling close button in window
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip  #refreshing game window


if __name__ == "__main__":  #call to main that runs asteroids when this file is run directly
    main()