import pygame
import sys
import os

__author__ = 'michele'


risorse = os.path.join("..", "risorse")
altezza = 500
larghezza = 800
VELOCITA = 5
VELOCITA_SPARO = 10
MUOVI_ALIENI_EVENTO = pygame.USEREVENT + 1
MOVIMENTO_LATERALE_ALIENO = 25
MOVIMENTO_GIU_ALIENO = 15

dimensioni_scehrmo = larghezza, altezza
nero = 0, 0, 0
movimento_alieno_dx_sx = MOVIMENTO_LATERALE_ALIENO

pygame.init()

schermo = pygame.display.set_mode(dimensioni_scehrmo)
orologio = pygame.time.Clock()
cannone_immagine = pygame.image.load("cannone.png")
cannone_rettamgolo = cannone_immagine.get_rect()
cannone_rettamgolo.centerx = larghezza / 2
cannone_rettamgolo.bottom = altezza
sparo_immagine = pygame.image.load("sparo.png")
sparo_rettamgolo = sparo_immagine.get_rect()
alieno_1_immagine = pygame.image.load("alieno_1_1.png"), pygame.image.load("alieno_1_2.png")
alieno_1_rettangolo = alieno_1_immagine[0].get_rect()
alieno_1_pos_immagine = 0
alieno_1_rettangolo.center = larghezza/2, 30
muovi_alieno_giu = 0

pygame.display.set_caption('Space Invaders')

pygame.mixer.music.load("quake.mp3")
pygame.mixer.music.play(-1, 0.0)

muovi_destra = False
muovi_sinistra = False
sparo_in_volo = False

# Ricorda di muovere l'alieno ogni 500 millisendi (0.5 secondi)
pygame.time.set_timer(MUOVI_ALIENI_EVENTO, 500)

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
        if evento.type == MUOVI_ALIENI_EVENTO:
            alieno_1_pos_immagine = alieno_1_pos_immagine + 1
            if alieno_1_pos_immagine > 1:
                alieno_1_pos_immagine = 0
            if muovi_alieno_giu == 0:
                if alieno_1_rettangolo.right + movimento_alieno_dx_sx > larghezza:
                    movimento_alieno_dx_sx = -MOVIMENTO_LATERALE_ALIENO
                    muovi_alieno_giu = 2
                if alieno_1_rettangolo.left + movimento_alieno_dx_sx < 0:
                    movimento_alieno_dx_sx = MOVIMENTO_LATERALE_ALIENO
                    muovi_alieno_giu = 2
            if muovi_alieno_giu > 0:
                alieno_1_rettangolo.centery = alieno_1_rettangolo.centery + MOVIMENTO_GIU_ALIENO
                muovi_alieno_giu = muovi_alieno_giu - 1
            else:
                alieno_1_rettangolo.centerx = alieno_1_rettangolo.centerx + movimento_alieno_dx_sx

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
    schermo.blit(alieno_1_immagine[alieno_1_pos_immagine], alieno_1_rettangolo)
    pygame.display.flip()
