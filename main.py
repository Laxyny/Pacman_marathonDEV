import pygame
from game import Game
from variables import *
import math
pygame.init()

# Générer fenêtre du jeu
WIDTH = 1280
HEIGHT = 720
color = (0, 0, 255)
PI = math.pi
pygame.display.set_caption("PacMan_MarrathonDEV")
screen = pygame.display.set_mode([WIDTH, HEIGHT])
player_x = 625
player_y = 357
direction = 0
#Droite Gauche Haut Bas
turns_allowed = [False, False, False, False]
direction_command = 0
player_speed = 2

running = True

level = boards

# Charger notre jeu
game = Game()

def draw_board():
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(
                    screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            if level[i][j] == 2:
                pygame.draw.circle(
                    screen, 'yellow', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(screen, color,
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 -
                                                                 (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'red', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)

def check_position(centerx, centery):
    turns = [False, False, False, False]
    num1 = (HEIGHT-50) //32
    num2 = (WIDTH//30)
    num3 = 15

    if centerx //30 < 29:
        if direction == 0:
            if level[centery//num1][(centerx - num3) // num2] < 3:
                turns[1] = True
        if direction == 1:
            if level[centery//num1][(centerx + num3) // num2] < 3:
                turns[0] = True
        if direction == 2:
            if level[(centery + num3)//num1][centerx // num2] < 3:
                turns[3] = True
        if direction == 3:
            if level[(centery - num3)//num1][centerx  // num2] < 3:
                turns[2] = True
        
        if direction == 2 or direction == 3:
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num3)//num1][centerx // num2] < 3:
                    turns[3] = True
                if level[(centery - num3)//num1][centerx // num2] < 3:
                    turns[2] = True

            if 12 <= centery % num1 <= 18:
                if level[centery//num1][(centerx - num2) // num2] < 3:
                    turns[1] = True
                if level[centery//num1][(centerx + num2) // num2] < 3:
                    turns[0] = True

        if direction == 0 or direction == 1:
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num1)//num1][centerx // num2] < 3:
                    turns[3] = True
                if level[(centery - num1)//num1][centerx // num2] < 3:
                    turns[2] = True

            if 12 <= centery % num1 <= 18:
                if level[centery//num1][(centerx - num3) // num2] < 3:
                    turns[1] = True
                if level[centery//num1][(centerx + num2) // num2] < 3:
                    turns[0] = True

    else:
        turns[0] = True
        turns[1] = True

    return turns

def move_player(player_x, player_y):
    #D, G, H, B
    if direction == 0 and turns_allowed[0]:
        player_x += player_speed
    elif direction == 1 and turns_allowed[1]:
        player_x -= player_speed
    if direction == 2 and turns_allowed[2]:
        player_y -= player_speed
    elif direction == 3 and turns_allowed[3]:
        player_y += player_speed
    return player_x, player_y

# Boucle exécutée tant que running = True
while running:

    # Appliquer arrière plan du jeu
    screen.fill('black')
    draw_board()
    center_x = player_x + 15
    center_y = player_y + 14
    pygame.draw.circle(screen, 'white', (center_x, center_y), 15)
    
    turns_allowed = check_position(center_x, center_y)
    player_x, player_y = move_player(player_x, player_y)

    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # Si le joueur ferme la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = direction
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = direction
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = direction
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = direction

        if direction_command == 0 and turns_allowed[0]:
            direction = 0
        if direction_command == 1 and turns_allowed[1]:
            direction = 1
        if direction_command == 2 and turns_allowed[2]:
            direction = 2
        if direction_command == 3 and turns_allowed[3]:
            direction = 3

        for i in range(4):
            if direction_command == i and turns_allowed[i]:
                direction = i
            
        if player_x > 900:
            player_x = -47
        elif player_x < -50:
            player_x = 897

    # Mettre à jour l'écran
    pygame.display.flip()

