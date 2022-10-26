'''
A duck shooter game following the Udemy course
"An introduction to game development in python"
'''


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import sys
import os
import random
import pygame


# -----------------------------------------------------------------------------
# Pygame - Init
# -----------------------------------------------------------------------------
pygame.init()


# -----------------------------------------------------------------------------
# Display Dimensions and FPS
# -----------------------------------------------------------------------------
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# FPS
clock = pygame.time.Clock()


# -----------------------------------------------------------------------------
# Images
# -----------------------------------------------------------------------------
wood_bg = pygame.image.load(os.path.join("duck_shooter/assets", "Wood_BG.png"))
land_bg = pygame.image.load(os.path.join("duck_shooter/assets", "Land_BG.png"))
water_bg = pygame.image.load(
    os.path.join("duck_shooter/assets", "Water_BG.png"))
cloud1 = pygame.image.load(os.path.join("duck_shooter/assets", "Cloud1.png"))
cloud2 = pygame.image.load(os.path.join("duck_shooter/assets", "Cloud2.png"))
crosshair = pygame.image.load(
    os.path.join("duck_shooter/assets", "crosshair.png"))
crosshair_rect = crosshair.get_rect(center=(640, 360))
duck_surface = pygame.image.load(
    os.path.join("duck_shooter/assets", "duck.png"))

# Text
GAME_FONT = pygame.font.Font(None, 60)
TEXT_SURFACE = GAME_FONT.render('You Win!', True, (255, 255, 255))
TEXT_RECT = TEXT_SURFACE.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

# Land Variables
LAND_POSITION_Y = 560
LAND_SPEED = 1

# Water Variables
WATER_POSITION_Y = 640
WATER_SPEED = 1.5


# Duck Variables
DUCK_LIST = []
for duck in range(20):
    duck_position_x = random.randrange(50, 1200)
    duck_position_y = random.randrange(120, 600)
    duck_rect = duck_surface.get_rect(
        center=(duck_position_x, duck_position_y))
    DUCK_LIST.append(duck_rect)

# -----------------------------------------------------------------------------
# Pygame Game Loop
# -----------------------------------------------------------------------------
while True:
    for event in pygame.event.get():
        pygame.mouse.set_visible(False)
        # Close the window and kill the program when the X button is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Mouse movement control for the crosshair
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center=event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, duck_rect in enumerate(DUCK_LIST):
                if crosshair_rect.colliderect(duck_rect):
                    del DUCK_LIST[index]

    # Land animation and positioning
    screen.blit(wood_bg, (0, 0))
    LAND_POSITION_Y -= LAND_SPEED
    if LAND_POSITION_Y <= 520 or LAND_POSITION_Y >= 600:
        LAND_SPEED *= -1
    screen.blit(land_bg, (0, LAND_POSITION_Y))

    # Water animation and positioning
    WATER_POSITION_Y += WATER_SPEED
    if WATER_POSITION_Y <= 620 or WATER_POSITION_Y >= 680:
        WATER_SPEED *= -1
    screen.blit(water_bg, (0, WATER_POSITION_Y))

    # Duck positioning
    for duck_rect in DUCK_LIST:
        screen.blit(duck_surface, duck_rect)

    # You Won positioning
    if len(DUCK_LIST) <= 0:
        screen.blit(TEXT_SURFACE, TEXT_RECT)

    # Crosshair positioning
    screen.blit(crosshair, crosshair_rect)

    # Cloud positioning
    screen.blit(cloud1, (100, 50))
    screen.blit(cloud2, (170, 80))

    # Scenes will update on the display scene
    pygame.display.update()
    clock.tick(120)
