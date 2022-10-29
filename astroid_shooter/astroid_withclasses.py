'''
Astroid Shooter game using pygame.
Following the Udemy course "Learn Python by Making Games"
This version is uing classes.
'''


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import sys
from random import randint, uniform
import pygame


# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
class Ship(pygame.sprite.Sprite):
    ''' Ship sprite class '''
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            'astroid_shooter/assets/ship.png'
            ).convert_alpha()
        self.rect = self.image.get_rect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            )
        self.can_shoot = True
        self.shoot_time = None

    def laser_timer(self):
        ''' Timer to only shoot the laser every 0.5 seconds '''
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.can_shoot = True

    def input_position(self):
        ''' Get's the position of the mouse '''
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def laser_shoot(self):
        ''' Tracks if and when the laser is shot '''
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
            Laser(self.rect.midtop, laser_group)

    def update(self):
        ''' Updates the frames for the Ship class '''
        self.laser_timer()
        self.laser_shoot()
        self.input_position()


class Laser(pygame.sprite.Sprite):
    ''' Laser sprite class '''
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            'astroid_shooter/assets/laser.png'
        ).convert_alpha()
        self.rect = self.image.get_rect(
            midbottom=pos
        )
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 600

    def update(self):
        ''' Updates the frames for the Laser class'''
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))


class Meteor(pygame.sprite.Sprite):
    ''' Meteor sprint class '''
    def __init__(self, pos, groups):
        super().__init__(groups)
        meteor_surf = pygame.image.load(
            'astroid_shooter/assets/meteor.png'
        ).convert_alpha()
        meteor_size = pygame.math.Vector2(
            meteor_surf.get_size()
            ) * uniform(0.5, 1.5)
        self.scaled_surf = pygame. transform.scale(meteor_surf, meteor_size)
        self.image = self.scaled_surf
        self.rect = self.image.get_rect(
            center=pos
        )
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 600)
        self.rotation = 0
        self.rotation_speed = randint(20, 50)

    def rotate(self):
        ''' Rotation logic for the meteor'''
        self.rotation += self.rotation_speed * dt
        rotated_surf = pygame.transform.rotozoom(
            self.scaled_surf, self.rotation, 1
            )
        self.image = rotated_surf
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        ''' Updates the frames for the Meteor class'''
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.rotate()


class Score:
    ''' Game score class '''
    def __init__(self):
        self.font = pygame.font.Font('astroid_shooter/assets/subatomic.ttf', 50)

    def display(self):
        ''' Displays the score '''
        score_text = f'Score: {pygame.time.get_ticks() // 1000}'
        text_surf = self.font.render(score_text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(
            midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80)
            )
        display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(display_surface,
                         (255, 255, 255),
                         text_rect.inflate(30, 30),
                         width=8,
                         border_radius=5
                         )

# -----------------------------------------------------------------------------
# Pygame - Initiate
# -----------------------------------------------------------------------------
# Initiate
pygame.init()

# Hide the mouse
pygame.mouse.set_visible(False)

# Window size
WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

# Display surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Window Label
pygame.display.set_caption('Meteor Shooter - With Classes')

# FPS
clock = pygame.time.Clock()


# -----------------------------------------------------------------------------
# Global Variables
# -----------------------------------------------------------------------------
# Background
background_surf = pygame.image.load(
    'astroid_shooter/assets/background.png').convert()

# Sprite groups
spaceship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()

# Sprite creation
ship = Ship(spaceship_group)


# Meteor timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 400)

# Score
score = Score()

# -----------------------------------------------------------------------------
# Pygame - Game Loop
# -----------------------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == meteor_timer:
            meteor_y_pos = randint(-150, -50)
            meteor_x_pos = randint(-100, WINDOW_WIDTH + 100)
            Meteor((meteor_x_pos, meteor_y_pos), groups=meteor_group)

    # Delta time
    dt = clock.tick() / 1000

    # Background
    display_surface.blit(background_surf, (0, 0))

    # Updates
    spaceship_group.update()
    laser_group.update()
    meteor_group.update()

    # Score
    score.display()

    # Graphics
    spaceship_group.draw(display_surface)
    laser_group.draw(display_surface)
    meteor_group.draw(display_surface)

    # Draw the frame
    pygame.display.update()
