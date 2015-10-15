import pygame
import sys

__author__ = 'michele'

FPS = 30
ALTEZZA = 700
LARGHEZZA = 960
DIMENSIONI_SCHERMO = LARGHEZZA, ALTEZZA
VELOCITA = 5
VELOCITA_SPARO = 15
NERO = 0, 0, 0


pygame.init()

schermo = pygame.display.set_mode(DIMENSIONI_SCHERMO)
orologio = pygame.time.Clock()
cannone_immagine = pygame.image.load("cannone.png")
cannone_rettangolo = cannone_immagine.get_rect()
cannone_rettangolo.centerx = LARGHEZZA / 2
cannone_rettangolo.bottom = ALTEZZA
sparo_immagine = pygame.image.load("sparo.png")
sparo_rettamgolo = sparo_immagine.get_rect()

pygame.display.set_caption('Space Invaders')

pygame.mixer.music.load("videogame2.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1, 0.0)

muovi_destra = False
muovi_sinistra = False
sparo_in_volo = False
spara = False

while True:
    orologio.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                muovi_destra = True
            if evento.key == pygame.K_LEFT:
                muovi_sinistra = True
            if evento.key == pygame.K_SPACE:
                if not sparo_in_volo:
                    spara = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                muovi_destra = False
            if evento.key == pygame.K_LEFT:
                muovi_sinistra = False

    if muovi_destra:
        cannone_rettangolo.centerx = cannone_rettangolo.centerx + VELOCITA
    if muovi_sinistra:
        cannone_rettangolo.centerx = cannone_rettangolo.centerx - VELOCITA
    if cannone_rettangolo.right > LARGHEZZA:
        cannone_rettangolo.right = LARGHEZZA
    if cannone_rettangolo.left < 0:
        cannone_rettangolo.left = 0

    if spara:
        sparo_rettamgolo.top = cannone_rettangolo.top
        sparo_rettamgolo.centerx = cannone_rettangolo.centerx
        sparo_in_volo = True
        spara = False
    if sparo_in_volo:
        sparo_rettamgolo.top = sparo_rettamgolo.top - VELOCITA_SPARO
    if sparo_rettamgolo.bottom < 0:
        sparo_in_volo = False

    schermo.fill(NERO)
    schermo.blit(cannone_immagine, cannone_rettangolo)
    if sparo_in_volo:
        schermo.blit(sparo_immagine, sparo_rettamgolo)
    pygame.display.flip()
