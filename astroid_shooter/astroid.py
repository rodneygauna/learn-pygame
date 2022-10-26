'''
Astroid Shooter game using pygame.
Following the Udemy course "Learn Python by Making Games"
'''


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import sys
import os
import pygame


# -----------------------------------------------------------------------------
# Pygame - Initiate
# -----------------------------------------------------------------------------
# Initiate
pygame.init()

# Window Size
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Display Surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Window Label
pygame.display.set_caption('Meteor Shooter - No Classes')


# -----------------------------------------------------------------------------
# Global Variables
# -----------------------------------------------------------------------------
# Import Images
SHIP_SURF = pygame.image.load(
    os.path.join("astroid_shooter/assets", "ship.png")).convert_alpha()
BG_SURF = pygame.image.load(
    os.path.join("astroid_shooter/assets", "background.png")).convert()

# Import Text
font = pygame.font.Font(
    os.path.join("astroid_shooter/assets", "subatomic.ttf"), 50)
TEXT_SURF = font.render("Space", True, (255, 255, 255))


# -----------------------------------------------------------------------------
# Pygame
# -----------------------------------------------------------------------------
while True:
    # Input - Events (mouse click, mouse movement, button press, etc.)
    for event in pygame.event.get():
        # If the window is exited, close the window and exit the code
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Updates
    display_surface.fill((0, 0, 0))
    display_surface.blit(BG_SURF, (0, 0))
    display_surface.blit(SHIP_SURF, (300, 500))
    display_surface.blit(TEXT_SURF, (500, 200))

    # Display the frame / updates to the display surface
    pygame.display.update()
