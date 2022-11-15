from ghosts import Ghost
import pygame
import copy
from variables import boards

class GBox:
    score = 0
    powerup = False
    power_counter = 0
    eaten_ghost = [False, False, False, False]
    #def __init__():

    def check_collisions2(scor, power, power_count, eaten_ghosts):
        player_x = 450
        player_y = 663
        WIDTH = 900
        HEIGHT = 950
        level = copy.deepcopy(boards)
        center_x = player_x + 23
        center_y = player_y + 24
        num1 = (HEIGHT - 50) // 32
        num2 = WIDTH // 30
        if 0 < player_x < 870:
            if level[center_y // num1][center_x // num2] == 1:
                level[center_y // num1][center_x // num2] = 0
                scor += 10
            if level[center_y // num1][center_x // num2] == 2:
                level[center_y // num1][center_x // num2] = 0
                scor += 50
                power = True
                power_count = 0
                eaten_ghosts = [False, False, False, False]
        return scor, power, power_count, eaten_ghosts

    def ifmov():
        player_x = 450
        player_y = 663
        ghost_speeds = [2, 2, 2, 2]
        blinky_x = 56
        blinky_y = 58
        blinky_direction = 0
        inky_x = 440
        inky_y = 388
        inky_direction = 2
        pinky_x = 440
        pinky_y = 438
        pinky_direction = 2
        clyde_x = 440
        clyde_y = 438
        clyde_direction = 2
        blinky_box = False
        inky_box = False
        clyde_box = False
        pinky_box = False
        blinky_img = pygame.transform.scale(pygame.image.load(
            f'assets/images/ghost_images/red.png'), (45, 45))
        pinky_img = pygame.transform.scale(pygame.image.load(
            f'assets/images/ghost_images/pink.png'), (45, 45))
        inky_img = pygame.transform.scale(pygame.image.load(
            f'assets/images/ghost_images/blue.png'), (45, 45))
        clyde_img = pygame.transform.scale(pygame.image.load(
            f'assets/images/ghost_images/orange.png'), (45, 45))
        spooked_img = pygame.transform.scale(pygame.image.load(
            f'assets/images/ghost_images/powerup.png'), (45, 45))
        dead_img = pygame.transform.scale(pygame.image.load(
            f'assets/images/ghost_images/dead.png'), (45, 45))
        blinky_dead = False
        inky_dead = False
        clyde_dead = False
        pinky_dead = False
        targets = [(player_x, player_y), (player_x, player_y), (player_x, player_y), (player_x, player_y)]
        blinky = Ghost(blinky_x, blinky_y, targets[0], ghost_speeds[0], blinky_img, blinky_direction, blinky_dead,
                       blinky_box, 0)
        inky = Ghost(inky_x, inky_y, targets[1], ghost_speeds[1], inky_img, inky_direction, inky_dead,
                        inky_box, 1)
        pinky = Ghost(pinky_x, pinky_y, targets[2], ghost_speeds[2], pinky_img, pinky_direction, pinky_dead,
                        pinky_box, 2)
        clyde = Ghost(clyde_x, clyde_y, targets[3], ghost_speeds[3], clyde_img, clyde_direction, clyde_dead,)
        if not blinky_dead and not blinky.in_box:
            blinky_x, blinky_y, blinky_direction = blinky.move_blinky()
        else:
            blinky_x, blinky_y, blinky_direction = blinky.move_clyde()
        if not pinky_dead and not pinky.in_box:
            pinky_x, pinky_y, pinky_direction = pinky.move_pinky()
        else:
            pinky_x, pinky_y, pinky_direction = pinky.move_clyde()
        if not inky_dead and not inky.in_box:
            inky_x, inky_y, inky_direction = inky.move_inky()
        else:
            inky_x, inky_y, inky_direction = inky.move_clyde()
        clyde_x, clyde_y, clyde_direction = clyde.move_clyde()
    score, powerup, power_counter, eaten_ghost = check_collisions2(score, powerup, power_counter, eaten_ghost)