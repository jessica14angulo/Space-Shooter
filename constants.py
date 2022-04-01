import pygame
import os


# window/Screen dimensions
WIDTH, HEIGHT = 1000, 700
# Window: display, size, and caption
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Space Shooter")


"""Load images"""

# Enemy Images
ENEMY_1 = pygame.image.load(os.path.join("game", "assets", "space1.png"))
ENEMY_2 = pygame.image.load(os.path.join("game", "assets", "space2.png"))
ENEMY_3 = pygame.image.load(os.path.join("game", "assets", "space3.png"))
BOSS_IMAGE = pygame.image.load(os.path.join("game", "assets", "boss.png"))

# Player player
SPACE_SHIP = pygame.image.load(os.path.join("game", "assets", "space4.png"))

# health pack
HEALTH_PACK = pygame.image.load(
    os.path.join("game", "assets", "health_pack.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("game", "assets", "red_laser.png"))
GREEN_LASER = pygame.image.load(
    os.path.join("game", "assets", "green_laser.png"))
BLUE_LASER = pygame.image.load(
    os.path.join("game", "assets", "blue_laser.png"))
YELLOW_LASER = pygame.image.load(
    os.path.join("game", "assets", "yellow_laser.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join(
    "game", "assets", "space_background.png")), (WIDTH, HEIGHT))

# Sounds paths
START_SOUND = "game/sounds/start.wav"
LASER_SOUND = "game/sounds/laser.wav"
EXPLOTION_SOUND = "game/sounds/explotion.wav"
OVER_SOUND = "sounds/over.wav"
HEALTH_SOUND = "game/sounds/ting.wav"

SOUNDS_VOLUME = 0.25
START_VOLUME = 0.10
