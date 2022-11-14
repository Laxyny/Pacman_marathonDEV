import pygame
from player import Player

#Créer une seconde classe
class Game:
    def __init__(self):
        #Générer joueur
        self.player = Player(self)
        self.pressed = {}

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)