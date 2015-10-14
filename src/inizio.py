import pygame
import sys

__author__ = 'michele'


FPS = 30
ALTEZZA = 700
LARGHEZZA = 960
DIMENSIONI_SCHERMO = LARGHEZZA, ALTEZZA
NERO = 0, 0, 0

pygame.init()
schermo = pygame.display.set_mode(DIMENSIONI_SCHERMO)
orologio = pygame.time.Clock()
cannone_immagine = pygame.image.load("cannone.png")
cannone_rettamgolo = cannone_immagine.get_rect()
cannone_rettamgolo.centerx = LARGHEZZA / 2
cannone_rettamgolo.bottom = ALTEZZA

pygame.display.set_caption('Space Invaders')

pygame.mixer.music.load("videogame2.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1, 0.0)

while True:
    orologio.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
    schermo.fill(NERO)
    schermo.blit(cannone_immagine, cannone_rettamgolo)

    pygame.display.flip()
