import pygame
from game.laser import Laser
from constants import *


class Boss:

    BOSS_MAP = {
        "boss_red": (BOSS_IMAGE, RED_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.boss_img, self.laser_img = self.BOSS_MAP[color]
        self.mask = pygame.mask.from_surface(self.boss_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def draw(self, window):
        window.blit(self.boss_img, (self.x, self.y))

    def get_width(self):
        return self.boss_img.get_width()

    def get_height(self):
        return self.boss_img.get_height()
