import pygame  #importing pygame library, and all magic numbers from constants.py
from constants import *

def display_score(display, font, points):  #method to create to overlay the score
    score_text = font.render(f"Score: {points}", True, "black", "white")
    scoreboard = score_text.get_rect()
    scoreboard.center = (SCREEN_WIDTH * (7/8), SCREEN_HEIGHT - 16)
    display.blit(score_text, scoreboard)

def display_lives(display, font, num_lives):
    lives_text = font.render(f"Lives: {num_lives}", True, "black", "white")  #method to overlay the number of lives
    lives = lives_text.get_rect()
    lives.center = (SCREEN_WIDTH / 8, SCREEN_HEIGHT - 16)
    display.blit(lives_text, lives)

def display_bombs(display, font, num_bombs):  #method to overlay the number of bombs
    bombs_text = font.render(f"Bombs: {num_bombs}", True, "red", "white")
    bombs = bombs_text.get_rect()
    bombs.center = (SCREEN_WIDTH / 4, SCREEN_HEIGHT - 16)
    display.blit(bombs_text, bombs)

def display_shield(display, font, have_shield, shield_timer):  #method to overlay if shield is available
    if shield_timer == 0:
        if have_shield == False:
            message = "Unavailable"
        elif have_shield == True:
            message = "Available"
    else:
        message = int(shield_timer / 60)
    
    shield_text = font.render(f"Shield: {message}", True, "cyan3", "white")
    shield = shield_text.get_rect()
    shield.center = (SCREEN_WIDTH * (7/16), SCREEN_HEIGHT - 16)
    display.blit(shield_text, shield)

def display_weapon_timer(display, font, weapon_type, weapon_timer):  #method to display current weapon powerup if available
    if weapon_type == "triple_shot":
        weapon_color = "indigo"
    elif weapon_type == "scatter_shot":
        weapon_color = "green4"
    elif weapon_type == "exploding_shot":
        weapon_color = "darkorange2"
    
    if weapon_type == None:
        weapon_text = font.render(f"Powerup: None", True, "black", "white")
    else:
        weapon_text = font.render(f"Powerup: {int(weapon_timer / 60)}", True, weapon_color, "white")

    weapon = weapon_text.get_rect()
    weapon.center = (SCREEN_WIDTH * (21/32), SCREEN_HEIGHT - 16)
    display.blit(weapon_text, weapon)