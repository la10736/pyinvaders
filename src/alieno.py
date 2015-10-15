import pygame
import sys

__author__ = 'michele'

FPS = 30
ALTEZZA = 700
LARGHEZZA = 960
DIMENSIONI_SCHERMO = LARGHEZZA, ALTEZZA
VELOCITA = 5
VELOCITA_SPARO = 15
VELOCITA_SPARO_ALIENO = 10
MUOVI_ALIENI_EVENTO = pygame.USEREVENT + 1
SPARO_ALIENO_EVENTO = pygame.USEREVENT + 2
FREQUENZA_SPARI_ALIENI_MILLISECONDI = 2300
MOVIMENTO_LATERALE_ALIENO = 30
DISTANZA_LATERALE_ALIENO = MOVIMENTO_LATERALE_ALIENO * 2
MOVIMENTO_GIU_ALIENO = 15
BASE_FREQUENZA_MOVIMENTO_ALIENI_MILLISECONDI = 1000

NERO = 0, 0, 0

movimento_alieno_dx_sx = MOVIMENTO_LATERALE_ALIENO

pygame.init()

schermo = pygame.display.set_mode(DIMENSIONI_SCHERMO)
orologio = pygame.time.Clock()
cannone_immagine = pygame.image.load("cannone.png")
cannone_rettangolo = cannone_immagine.get_rect()
cannone_rettangolo.centerx = LARGHEZZA / 2
cannone_rettangolo.bottom = ALTEZZA
sparo_immagine = pygame.image.load("sparo.png")
sparo_rettamgolo = sparo_immagine.get_rect()
alieno_1_immagine = pygame.image.load("alieno_1_1.png"), pygame.image.load("alieno_1_2.png")
alieno_1_rettangolo = alieno_1_immagine[0].get_rect()
alieno_1_pos_immagine = 0
alieno_1_rettangolo.center = LARGHEZZA/2, 30
muovi_alieno_giu = 0

pygame.display.set_caption('Space Invaders')

pygame.mixer.music.load("videogame2.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1, 0.0)

muovi_destra = False
muovi_sinistra = False
sparo_in_volo = False
spara = False

# Ricorda di muovere l'alieno ogni 500 millisendi (0.5 secondi)
pygame.time.set_timer(MUOVI_ALIENI_EVENTO, BASE_FREQUENZA_MOVIMENTO_ALIENI_MILLISECONDI)

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
        if evento.type == MUOVI_ALIENI_EVENTO:
            alieno_1_pos_immagine = alieno_1_pos_immagine + 1
            if alieno_1_pos_immagine > 1:
                alieno_1_pos_immagine = 0
            if muovi_alieno_giu == 0:
                if alieno_1_rettangolo.right + movimento_alieno_dx_sx > LARGHEZZA:
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
    schermo.blit(alieno_1_immagine[alieno_1_pos_immagine], alieno_1_rettangolo)
    pygame.display.flip()
