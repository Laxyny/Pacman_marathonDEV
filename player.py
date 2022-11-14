import pygame

#Classe joueur
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        WIDTH = 1280
        HEIGHT = 720
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.health = 1 #Vie joueur
        self.max_health = 1 #Vie max joueur
        self.attack = 1 #Attaque joueur
        self.velocity = 5 #Vitesse déplacement joueur en px
        image2 = pygame.image.load('assets/images/player_pacman.png')
        image = pygame.transform.scale(image2, (28,28))
        screen.blit(image, (28,28))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 625
        self.rect.y = 357
    
    def move_right(self):
        self.rect.x += self.velocity / 5

    def move_left(self):
        self.rect.x -= self.velocity / 5

    def move_up(self):
        self.rect.y -= self.velocity / 5

    def move_down(self):
        self.rect.y += self.velocity / 5