'''
Astroid Shooter game using pygame.
Following the Udemy course "Learn Python by Making Games"
'''


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import sys
import pygame


# -----------------------------------------------------------------------------
# Pygame - Initiate
# -----------------------------------------------------------------------------
pygame.init()


# -----------------------------------------------------------------------------
# Global Variables
# -----------------------------------------------------------------------------
# Window Size
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Display Surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Window Label
pygame.display.set_caption('Meteor Shooter - No Classes')

# A test surface
test_surf = pygame.Surface((400, 100))


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
    display_surface.fill('red')
    test_surf.fill('blue')

    # Place a surface
    display_surface.blit(test_surf,
                         (WINDOW_WIDTH - test_surf.get_width(), 100))

    # Display the frame / updates to the display surface
    pygame.display.update()
