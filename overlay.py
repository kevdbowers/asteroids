import pygame  #importing pygame library and all magic numbers from constants.py
from constants import *

def display_score(display, font, points):  #method to create to overlay the score
    score_text = font.render(f"Score: {points}", True, "Black", "White")
    scoreboard = score_text.get_rect()
    scoreboard.center = (SCREEN_WIDTH * (7/8), SCREEN_HEIGHT - 16)
    display.blit(score_text, scoreboard)

def display_lives(display, font, lives):
    lives_text = font.render(f"Lives: {lives}", True, "Black", "White")  #method to overlay the number of lives
    lives = lives_text.get_rect()
    lives.center = (SCREEN_WIDTH / 8, SCREEN_HEIGHT - 16)
    display.blit(lives_text, lives)