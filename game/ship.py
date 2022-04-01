import pygame
from game.laser import Laser
from constants import *
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()


class Ship:

    COOLDOWN = 10  # The cooldown determines the time between laser shots
    # The higher the number, the slower your lasers are.
    """ Sets all the variables with the parameters that will be user for the Spaceships of the game"""

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        # I mages are not defined on these variables so that the code could be reused for possible updates, and also inherited in the Player class and Enemy class.
        self.ship_img = None
        self.laser_img = None

        self.lasers = []
        self.cool_down_counter = 0

    """Draw Ship images on the screen"""

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 2

            laser_fx = pygame.mixer.Sound(LASER_SOUND)
            laser_fx.set_volume(SOUNDS_VOLUME)
            laser_fx.play()

    """
    Getter methods to get the width and hight of the variable ship_img.
    The width and height is used in the re_draw window function which is
    nested in the main function, and in the keyService, also in the main
    function to restrict images from showing outside of the window width
    and height.
    """

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()
