import pygame
from constants import *

pygame.font.init()

# Window: display, size, and caption
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")


def main():
    run = True
    FPS = 60  # FPS Stands for Frames Per Second, The higher the number the faster the game will run
    level = 0
    # determines the amount of ships that reach the end of the screen Y.
    lives = 5

    # Uses font library to set it text at 25px at Monteserrat regular
    main_font = pygame.font.SysFont("Montserrat", 25)
    lost_font = pygame.font.SysFont("Montserrat", 25)


if __name__ == "__main__":
    main()
