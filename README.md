# asteroids

Asteroids is a project designed to create a playable version of the 1979 video game of the same name.  This project was created using Python 3.

This project requires pygame version 2.6.1 and contains:
    a main.py file which is used to run the program
    an asteroid.py file defining the Asteroid sprite
    an asteroidfield.py file defining a field the size of the screen that creates Asteroid sprites and Powerup sprites
    a background.py file used to load and display the background image used in the game, this requires a LOCAL FILEPATH to an image
    a circleshape.py file defining the CircleShape sprite
    a constants.py file containing a list of magic numbers
    an explosion.py file defining the Explosion sprite, this sprite is a visual effect that requires a LOCAL FILEPATH to a series of nine consecutive numbered images
    an overlay.py file defining the methods to generate an overlay 
    a player.py file defining the Player sprite
    a powerup.py file defining the Powerup sprite
    a shot.py file defining the Shot Sprite  
    a requirements.txt file which shows the required libraries to be installed

To run this program enter the following in the command line: python3 main.py
Once running the game controls are as follows:
    "w" = move forward
    "d" = move backward
    "a" = rotate counter-clockwise
    "d" = rotate clockwise
    "spacebar" = shoot
    "q" = use a bomb
    "e" = use a shield