
from game.ship import Ship
from constants import *


class Player(Ship):
    # Initiantes all functions from the Ship class
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)

        """
        Polymorphism applied to the images of the spaceship and laser 
        from the variables inherited from the Ship class' functions and 
        changes them to what the Player's spaceship will need
        """
        self.ship_img = SPACE_SHIP
        self.laser_img = YELLOW_LASER

        """
        Applies mask to the images of the spaceship to handdle the empty
        space from the png image, allowing pixel perfect collision.
        """
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y +
                         self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() +
                         10, self.ship_img.get_width() * (self.health/self.max_health), 10))
