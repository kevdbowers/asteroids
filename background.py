import pygame  #importing pygame library and all magic numbers from constants.py
from constants import *

def get_background(screen):  #method to load, scale, and display the background
    background = pygame.image.load("background_images/background1.jpg")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    rect = background.get_rect()
    screen.blit(background, rect)