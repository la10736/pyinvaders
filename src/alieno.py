import pygame
import sys
import os

__author__ = 'michele'


risorse = os.path.join("..", "risorse")
fattore = 4
base_altezza = 120
base_larghezza = 160
VELOCITA = 5
VELOCITA_SPARO = 10

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
sparo_immagine = pygame.image.load("sparo.png")
sparo_rettamgolo = sparo_immagine.get_rect()
alieno_1_immagine_1 = pygame.image.load("alieno_1_1.png")
alieno_1_immagine_2 = pygame.image.load("alieno_1_2.png")
alieno_rettangolo = alieno_1_immagine_1.get_rect()

pygame.display.set_caption('Space Invaders')

pygame.mixer.music.load("quake.mp3")
pygame.mixer.music.play(-1, 0.0)

muovi_destra = False
muovi_sinistra = False
sparo_in_volo = False

while True:
    orologio.tick(20)
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
                    sparo_rettamgolo.top = cannone_rettamgolo.top
                    sparo_rettamgolo.centerx = cannone_rettamgolo.centerx
                    sparo_in_volo = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                muovi_destra = False
            if evento.key == pygame.K_LEFT:
                muovi_sinistra = False

    if muovi_destra:
        cannone_rettamgolo.centerx = cannone_rettamgolo.centerx + VELOCITA
    if muovi_sinistra:
        cannone_rettamgolo.centerx = cannone_rettamgolo.centerx - VELOCITA
    if cannone_rettamgolo.right > larghezza:
        cannone_rettamgolo.right = larghezza
    if cannone_rettamgolo.left < 0:
        cannone_rettamgolo.left = 0

    if sparo_in_volo:
        sparo_rettamgolo.top = sparo_rettamgolo.top - VELOCITA_SPARO
    if sparo_rettamgolo.bottom < 0:
        sparo_in_volo = False

    schermo.fill(nero)
    schermo.blit(cannone_immagine, cannone_rettamgolo)
    if sparo_in_volo:
        schermo.blit(sparo_immagine, sparo_rettamgolo)
    pygame.display.flip()
