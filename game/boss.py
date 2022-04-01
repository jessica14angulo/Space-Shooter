import pygame
from game.ship import Ship
from game.laser import Laser
from constants import *


class Boss(Ship):

    BOSS_MAP = {
        "boss_red": (BOSS_IMAGE, RED_LASER)
    }

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.boss_img, self.laser_img = self.BOSS_MAP
        self.mask = pygame.mask.from_surface(self.boss_img)

    def move(self, vel):
        self.y += vel

    def draw(self, window):
        window.blit(self.boss_img, (self.x, self.y))

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    # def get_width(self):
    #     return self.boss_img.get_width()

    # def get_height(self):
    #     return self.boss_img.get_height()
