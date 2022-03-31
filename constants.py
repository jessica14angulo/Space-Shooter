import pygame
import os


# window/Screen dimensions
WIDTH, HEIGHT = 1000, 700
# Window: display, size, and caption
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")


# Load images
ENEMY_1 = pygame.image.load(
    os.path.join("game", "assets", "space1.png"))
ENEMY_2 = pygame.image.load(
    os.path.join("assets", "space2.png"))
ENEMY_3 = pygame.image.load(
    os.path.join("assets", "space3.png"))

# Player player
SPACE_SHIP = pygame.image.load(os.path.join("game", "assets", "space4.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("game", "assets", "red_laser.png"))
GREEN_LASER = pygame.image.load(
    os.path.join("game", "assets", "green_laser.png"))
BLUE_LASER = pygame.image.load(
    os.path.join("game", "assets", "blue_laser.png"))
YELLOW_LASER = pygame.image.load(
    os.path.join("game", "assets", "yellow_laser.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(
    os.path.join("game", "assets", "background-black.png")), (WIDTH, HEIGHT))
