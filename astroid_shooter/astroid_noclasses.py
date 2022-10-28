'''
Astroid Shooter game using pygame.
Following the Udemy course "Learn Python by Making Games"
'''


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import os
import sys
from random import randint, uniform
import pygame


# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def laser_update(laser_list, speed=300):
    ''' Controls the speed of the laser '''
    for rect in laser_list:
        rect.top -= speed * dt
        if rect.bottom < 0:
            laser_list.remove(rect)


def meteor_update(meteor_list, speed=300):
    ''' Controls the speed and direction of the meteors'''
    for meteor_tuple in meteor_list:
        direction = meteor_tuple[1]
        rect = meteor_tuple[0]
        rect.center += direction * speed * dt
        if rect.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor_tuple)


def display_score():
    ''' Controls the score for the game'''
    score_text = f'Score: {pygame.time.get_ticks() // 1000}'
    text_surf = font.render(score_text, True, (255, 255, 255))
    text_rect = text_surf.get_rect(
        midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface,
                     (255, 255, 255),
                     text_rect.inflate(30, 30),
                     width=8,
                     border_radius=5)


def laser_timer(can_shoot, duration=500):
    ''' Timer to only shoot the laser ever 0.5 seconds '''
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - SHOOT_TIME > duration:
            can_shoot = True
    return can_shoot


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

# FPS
clock = pygame.time.Clock()


# -----------------------------------------------------------------------------
# Global Variables
# -----------------------------------------------------------------------------
# Ship Imports
SHIP_SURF = pygame.image.load(
    os.path.join("astroid_shooter/assets", "ship.png")).convert_alpha()
SHIP_RECT = SHIP_SURF.get_rect(
    center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# Background Import
BG_SURF = pygame.image.load(
    os.path.join("astroid_shooter/assets", "background.png")).convert()

# Laser Import
LASER_SURF = pygame.image.load(
    os.path.join("astroid_shooter/assets", "laser.png")).convert_alpha()
LASER_LIST = []

# Laser Timer
CAN_SHOOT = True
SHOOT_TIME = None

# Text Import
font = pygame.font.Font(
    os.path.join("astroid_shooter/assets", "subatomic.ttf"), 50)
TEXT_SURF = font.render("Space", True, (255, 255, 255))

# Meteor Import
METEOR_SURF = pygame.image.load(
    os.path.join("astroid_shooter/assets", "meteor.png")).convert_alpha()
METEOR_LIST = []

# Meteor Timer
METEOR_TIMER = pygame.event.custom_type()
pygame.time.set_timer(METEOR_TIMER, 500)

# Sound Import
LASER_SOUND = pygame.mixer.Sound(
    os.path.join("astroid_shooter/assets", "laser.ogg"))
EXPLOSION_SOUND = pygame.mixer.Sound(
    os.path.join("astroid_shooter/assets", "explosion.wav"))
BACKGROUND_MUSIC = pygame.mixer.Sound(
    os.path.join("astroid_shooter/assets", "music.wav"))

# Play the background music continuously
BACKGROUND_MUSIC.play(loops=-1)

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
        # If the player presses down on the mouse button, fire a laser
        if event.type == pygame.MOUSEBUTTONDOWN and CAN_SHOOT:
            # Displays the laser and adds to the list
            laser_rect = LASER_SURF.get_rect(midbottom=SHIP_RECT.midtop)
            LASER_LIST.append(laser_rect)
            # Once the laser fires, updates the variables
            CAN_SHOOT = False
            SHOOT_TIME = pygame.time.get_ticks()
            # Play the laser sound
            # LASER_SOUND.play()
        # Loops the meteor timer
        if event.type == METEOR_TIMER:
            # Creates a random position
            x_pos = randint(-100, WINDOW_WIDTH + 100)
            y_pos = randint(-100, 50)
            # Creates a meteor
            rect = METEOR_SURF.get_rect(center=(x_pos, y_pos))
            # Creates a random direction
            direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
            # Adds a meteor to the list
            METEOR_LIST.append((rect, direction))

    # Framerate limit
    dt = clock.tick(120) / 1000

    # Mouse Input
    SHIP_RECT.center = pygame.mouse.get_pos()

    # Laser Update List
    laser_update(LASER_LIST)
    meteor_update(METEOR_LIST)
    CAN_SHOOT = laser_timer(CAN_SHOOT)

    # Check for meteor and ship overlap
    for meteor_tuple in METEOR_LIST:
        meteor_rect = meteor_tuple[0]
        if SHIP_RECT.colliderect(meteor_rect):
            EXPLOSION_SOUND.play()
            pygame.quit()
            sys.exit()

    # Check if laser and meteor overlap
    for laser_rect in LASER_LIST:
        for meteor_tuple in METEOR_LIST:
            if laser_rect.colliderect(meteor_tuple[0]):
                METEOR_LIST.remove(meteor_tuple)
                LASER_LIST.remove(laser_rect)
                EXPLOSION_SOUND.play()

    # Draw background
    display_surface.fill((0, 0, 0))
    display_surface.blit(BG_SURF, (0, 0))

    # Display the Score
    display_score()

    # Draw Lasers
    for rect in LASER_LIST:
        display_surface.blit(LASER_SURF, rect)

    # Draw Meteors
    for meteor_tuple in METEOR_LIST:
        display_surface.blit(METEOR_SURF, meteor_tuple[0])

    # Draw the ship and rect
    display_surface.blit(SHIP_SURF, SHIP_RECT)

    # Display the frame / updates to the display surface
    pygame.display.update()
