import pygame
import sys
import os

__author__ = 'michele'


risorse = os.path.join("..", "risorse")
fattore = 4
base_altezza = 120
base_larghezza = 160

altezza = base_altezza * fattore
larghezza = base_larghezza * fattore
dimensioni_scehrmo = larghezza, altezza
nero = 0, 0, 0

pygame.init()

schermo = pygame.display.set_mode(dimensioni_scehrmo)
orologio = pygame.time.Clock()
cannone_immagine = pygame.image.load("cannone.png")
cannone_rettamgolo = cannone_immagine.get_rect()
cannone_rettamgolo.centerx = larghezza / 2
cannone_rettamgolo.bottom = altezza

pygame.display.set_caption('Space Invaders')

pygame.mixer.music.load("quake.mp3")
pygame.mixer.music.play(-1, 0.0)

while True:
    orologio.tick(20)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
    schermo.fill(nero)
    schermo.blit(cannone_immagine, cannone_rettamgolo)

    pygame.display.flip()
