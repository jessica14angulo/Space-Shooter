
from game.ship import Ship
from constants import *
from game.laser import Laser


class Enemy(Ship):
    """Creates dictionary of enemies and asigns laser color image"""
    COLOR_MAP = {
        "red": (ENEMY_1, RED_LASER),
        "green": (ENEMY_2, GREEN_LASER),
        "blue": (ENEMY_3, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    """sets the movement of the enemy ships to the Y axis of the screen."""

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
