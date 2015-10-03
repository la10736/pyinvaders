import os
from pygame.rect import Rect

__author__ = 'michele'

import pygame
import sys

risorse = os.path.join("..", "risorse")
fattore = 3
base_altezza = 120
base_larghezza = 160

altezza = base_altezza * fattore
larghezza = base_larghezza * fattore
dimensioni_scehrmo = larghezza, altezza
nero = 0, 0, 0

pygame.init()

schermo = pygame.display.set_mode(dimensioni_scehrmo)
orologio = pygame.time.Clock()
immagine_cannone = pygame.image.load(os.path.join(risorse, "cannone.png"))
immagine_cannone = pygame.transform.rotozoom(immagine_cannone, 0, fattore)
cannone = immagine_cannone.get_rect()
""":type: pygame.rect.Rect"""
cannone.centerx = larghezza / 2
cannone.bottom = altezza

pygame.display.set_caption('Space Invaders')
pygame.mouse.set_visible(False)

# set up sounds
pygame.mixer.music.load(os.path.join(risorse, "quake.mp3"))


while True:
    pygame.mixer.music.play(-1, 0.0)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
    orologio.tick(20)
    schermo.fill(nero)
    schermo.blit(immagine_cannone, cannone)

    pygame.display.flip()
