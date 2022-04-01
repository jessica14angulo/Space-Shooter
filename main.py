import pygame
from constants import *
import random
from game.enemy import Enemy
from game.player import Player
from game.collide import Collide as collide
from game.health_pack import Healthpack
from pygame import mixer

# Initializes mixer from the pygame library.
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()


# Initializes font from the pygame library.
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

    """Set Variables"""

    # Stores the enemies and number of ships per wave.
    enemies = []
    wave_length = 12
    # All Velocities are set in Pixels, meaning that every time an object moves it moves in pixels by second.
    enemy_vel = 1
    player_vel = 8
    laser_vel = 8
    healthpack_vel = 2

    health_packs = []
    level_count_req = 2
    health_pack_req = 0

    player = Player(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WIN.blit(BG, (0, 0))

        """ Draws texts on the screen: Lives and Level, and sets the color of it in the RGB format 
        (Red,Green,Blue)"""

        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        for healthpack in health_packs:
            healthpack.draw(WIN)

        player.draw(WIN)

        if lost:
            over_fx = pygame.mixer.Sound("game/sounds/over.wav")
            over_fx.set_volume(0.25)
            over_fx.play()
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)  # sets the clock speed at 60 FPS
        redraw_window()

        if player.health <= 0:
            lives -= 1
            player.health = 100

        if lives <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        """Spawns enemies randomly from the Y axis outsie the top of the screen"""
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(
                    50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        if len(health_packs) == health_pack_req and level == level_count_req:
            healthpack = Healthpack(random.randrange(
                50, WIDTH-100), random.randrange(-1500, -100))
            level_count_req += 1
            health_packs.append(healthpack)

        """Loop runs the variables 60 times per second"""
        for event in pygame.event.get():  # Checks for event
            if event.type == pygame.QUIT:  # If user clicks on x of the window, quits the game
                quit()

        """Keyboard Service"""
        # calls for the key dictionary of pygame
        keys = pygame.key.get_pressed()

        """Assign Keys and the velocity of the object"""
        if keys[pygame.K_LEFT] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        """WIDTH restricts movement outside of the width of the screen"""
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        """HEIGHT restricts movement out of the height of the screen"""
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide.collide(enemy, player):
                player.health -= 10
                explotion_fx = pygame.mixer.Sound("game/sounds/explotion.wav")
                explotion_fx.set_volume(0.25)
                explotion_fx.play()
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                explotion_fx = pygame.mixer.Sound("game/sounds/explotion.wav")
                explotion_fx.set_volume(0.25)
                explotion_fx.play()
                enemies.remove(enemy)

        for healthpack in health_packs:
            healthpack.move(healthpack_vel)

            if collide.collide(healthpack, player):
                player.health += 10
                ting_fx = pygame.mixer.Sound("game/sounds/ting.wav")
                ting_fx.set_volume(0.25)
                ting_fx.play()
                health_packs.remove(healthpack)
            elif healthpack.y + healthpack.get_height() > HEIGHT:
                health_packs.remove(healthpack)

        player.move_lasers(-laser_vel, enemies)


def main_menu():
    title_font = pygame.font.SysFont("Montserrat", 50)
    run = True
    while run:
        WIN.blit(BG, (0, 0))
        title_label = title_font.render(
            "Press the mouse to begin...", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        start_fx = pygame.mixer.Sound("game/sounds/start.wav")
        start_fx.set_volume(0.10)
        start_fx.play()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


if __name__ == "__main__":
    main_menu()
