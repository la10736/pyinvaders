import pygame
import sys

__author__ = 'michele'

FPS = 30
ALTEZZA = 580
LARGHEZZA = 960
DIMENSIONI_SCHERMO = LARGHEZZA, ALTEZZA
VELOCITA = 5
VELOCITA_SPARO = 15
MUOVI_ALIENI_EVENTO = pygame.USEREVENT + 1
MOVIMENTO_LATERALE_ALIENO = 30
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
alieni = []
nuovo_alieno = {}
nuovo_alieno["immagini"] = pygame.image.load("alieno_1_1.png"), pygame.image.load("alieno_1_2.png")
nuovo_alieno["rettangolo"] = nuovo_alieno["immagini"][0].get_rect()
nuovo_alieno["pos_immagine"] = 0
nuovo_alieno["rettangolo"].center = LARGHEZZA/2, 30
alieni.append(nuovo_alieno)
nuovo_alieno = {}
nuovo_alieno["immagini"] = pygame.image.load("alieno_1_1.png"), pygame.image.load("alieno_1_2.png")
nuovo_alieno["rettangolo"] = nuovo_alieno["immagini"][0].get_rect()
nuovo_alieno["pos_immagine"] = 0
nuovo_alieno["rettangolo"].center = LARGHEZZA/2 + 60, 30
alieni.append(nuovo_alieno)

muovi_alieno_giu = 0

pygame.display.set_caption('Space Invaders')

pygame.mixer.music.load("videogame2.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1, 0.0)
bang = pygame.mixer.Sound('bang.wav')
bang.set_volume(1)

muovi_destra = False
muovi_sinistra = False
sparo_in_volo = False

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
                    sparo_rettamgolo.top = cannone_rettangolo.top
                    sparo_rettamgolo.centerx = cannone_rettangolo.centerx
                    sparo_in_volo = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                muovi_destra = False
            if evento.key == pygame.K_LEFT:
                muovi_sinistra = False
        if evento.type == MUOVI_ALIENI_EVENTO:
            for alieno in alieni:
                alieno["pos_immagine"] = alieno["pos_immagine"] + 1
                if alieno["pos_immagine"] > 1:
                    alieno["pos_immagine"] = 0
                if muovi_alieno_giu == 0:
                    if alieno["rettangolo"].right + movimento_alieno_dx_sx > LARGHEZZA:
                        movimento_alieno_dx_sx = -MOVIMENTO_LATERALE_ALIENO
                        muovi_alieno_giu = 2
                    if alieno["rettangolo"].left + movimento_alieno_dx_sx < 0:
                        movimento_alieno_dx_sx = MOVIMENTO_LATERALE_ALIENO
                        muovi_alieno_giu = 2
            if muovi_alieno_giu > 0:
                for alieno in alieni:
                    alieno["rettangolo"].centery = alieno["rettangolo"].centery + MOVIMENTO_GIU_ALIENO
                muovi_alieno_giu = muovi_alieno_giu - 1
            else:
                for alieno in alieni:
                    alieno["rettangolo"].centerx = alieno["rettangolo"].centerx + movimento_alieno_dx_sx

    if muovi_destra:
        cannone_rettangolo.centerx = cannone_rettangolo.centerx + VELOCITA
    if muovi_sinistra:
        cannone_rettangolo.centerx = cannone_rettangolo.centerx - VELOCITA
    if cannone_rettangolo.right > LARGHEZZA:
        cannone_rettangolo.right = LARGHEZZA
    if cannone_rettangolo.left < 0:
        cannone_rettangolo.left = 0

    if sparo_in_volo:
        sparo_rettamgolo.top = sparo_rettamgolo.top - VELOCITA_SPARO
        if sparo_rettamgolo.bottom < 0:
            sparo_in_volo = False
        for alieno in alieni:
            if alieno["rettangolo"].colliderect(sparo_rettamgolo):
                sparo_in_volo = False
                bang.play()
                alieni.remove(alieno)

    schermo.fill(NERO)
    schermo.blit(cannone_immagine, cannone_rettangolo)
    if sparo_in_volo:
        schermo.blit(sparo_immagine, sparo_rettamgolo)
    for alieno in alieni:
        schermo.blit(alieno["immagini"][alieno["pos_immagine"]], alieno["rettangolo"])
    pygame.display.flip()
