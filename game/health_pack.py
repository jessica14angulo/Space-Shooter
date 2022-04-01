import pygame
from game.laser import Laser
from constants import *


class Healthpack:
    

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health_pack_img = HEALTH_PACK
        self.mask = pygame.mask.from_surface(self.health_pack_img)
        
        
    def move(self, vel):
        self.y += vel   

    def draw(self, window):
        window.blit(self.health_pack_img, (self.x, self.y))
        


    def get_width(self):
        return self.health_pack_img.get_width()

    def get_height(self):
        return self.health_pack_img.get_height()
