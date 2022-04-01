import pygame
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

#load sounds
start_fx = pygame.mixer.Sound("game/sounds/start.wav")
start_fx.set_volume(0.25)
start_fx.play()

laser_fx = pygame.mixer.Sound("game/sounds/laser.wav")
laser_fx.set_volume(0.25)
laser_fx.play()

explotion_fx = pygame.mixer.Sound("game/sounds/explotion.wav")
explotion_fx.set_volume(0.25)
explotion_fx.play()

over_fx = pygame.mixer.Sound("sounds/over.wav")
over_fx.set_volume(0.25)