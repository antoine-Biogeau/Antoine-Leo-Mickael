import pygame

class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vie = 100
        self.degats = 10
        self.vie_max = 100

