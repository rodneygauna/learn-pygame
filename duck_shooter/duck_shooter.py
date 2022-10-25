'''
A duck shooter game following the Udemy course "An introduction to game development in python"
'''


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import pygame, sys, os


# -----------------------------------------------------------------------------
# Pygame - Init
# -----------------------------------------------------------------------------
pygame.init()


# -----------------------------------------------------------------------------
# Global Variables
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

land_position_y = 560
land_speed = 1

water_position_y = 640
water_speed = 1.5


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center=event.pos)
            pygame.mouse.set_visible(False)

    screen.blit(wood_bg, (0, 0))
    land_position_y -= land_speed

    if land_position_y <= 520 or land_position_y >= 600:
        land_speed *= -1
    screen.blit(land_bg, (0, land_position_y))

    water_position_y += water_speed
    if water_position_y <= 620 or water_position_y >= 680:
        water_speed *= -1
    screen.blit(water_bg, (0, water_position_y))

    screen.blit(crosshair, crosshair_rect)
    screen.blit(cloud1, (100, 50))
    screen.blit(cloud2, (170, 80))

    pygame.display.update()
    clock.tick(120)
