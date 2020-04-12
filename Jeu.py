import pygame
pygame.init()
from Chauve_souris import Chauve_souris


#Création de la fenêtre :
joueur = Joueur()
pygame.display.set_caption("test")
ecran = pygame.display.set_mode((1000, 800))


bg = pygame.image.load("fond.png")

#game = pygame.Game()
Chauve_souris = Chauve_souris()

perso = pygame.image.load("assets/Untitled1.png").convert_alpha()
position_perso = perso.get_rect()
pygame.key.set_repeat(400, 30)
fenetre.blit(perso,position_perso)
running = True

#Boucle Infinie
Chauve_souris.rect.x = Chauve_souris.rect.x + 100
Chauve_souris.rect.y = Chauve_souris.rect.y + 300

while running:
    ecran.blit(bg, (0, 0))
    ecran.blit(Chauve_souris.image,(Chauve_souris.rect.x, Chauve_souris.rect.y))
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("jeu fermé")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                position_perso = position_perso.move(0, 3)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                position_perso = position_perso.move(0, -3)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                position_perso = position_perso.move(3, 0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                position_perso = position_perso.move(-3, 0)


    #Mouvements Monstres

    Chauve_souris.mouvements()

    #Tests de colisions entre les monstres et les joueurs:

    Chauve_souris.attaque_chauve_souris()
