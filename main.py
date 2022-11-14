import pygame
pygame.init()

#Générer fenêtre du jeu
pygame.display.set_caption("PacMan_MarrathonDEV")
pygame.display.set_mode((1080, 720))

running = True

#Boucle exécutée tant que running = True
while running:
    
    #Si le joueur ferme la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")