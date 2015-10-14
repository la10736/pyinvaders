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
MOVIMENTO_LATERALE_ALIENO = 30
DISTANZA_LATERALE_ALIENO = MOVIMENTO_LATERALE_ALIENO * 2
MOVIMENTO_GIU_ALIENO = 15
DISTANZA_GIU_ALIENO = MOVIMENTO_GIU_ALIENO * 4
BASE_FREQUENZA_MOVIMENTO_ALIENI_MILLISECONDI = 1000

NERO = 0, 0, 0
BIANCO = 255, 255, 255


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
immagini_alieni = {}
immagini_alieni[0] = pygame.image.load("alieno_3_1.png"), pygame.image.load("alieno_3_2.png")
immagini_alieni[1] = pygame.image.load("alieno_2_1.png"), pygame.image.load("alieno_2_2.png")
immagini_alieni[2] = pygame.image.load("alieno_2_1.png"), pygame.image.load("alieno_2_2.png")
immagini_alieni[3] = pygame.image.load("alieno_1_1.png"), pygame.image.load("alieno_1_2.png")
immagini_alieni[4] = pygame.image.load("alieno_1_1.png"), pygame.image.load("alieno_1_2.png")
posizione_primo_x = LARGHEZZA/2 - DISTANZA_LATERALE_ALIENO * 5
posizione_primo_y = 30
muovi_alieno_giu = 0
movimento_alieno_dx_sx = MOVIMENTO_LATERALE_ALIENO

pygame.display.set_caption('Space Invaders')

pygame.mixer.music.load("videogame2.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1, 0.0)
bang = pygame.mixer.Sound('bang.wav')
bang.set_volume(0.2)

muovi_destra = False
muovi_sinistra = False
sparo_in_volo = False

# Ricorda di muovere l'alieno ogni 500 millisendi (0.5 secondi)
pygame.time.set_timer(MUOVI_ALIENI_EVENTO, BASE_FREQUENZA_MOVIMENTO_ALIENI_MILLISECONDI)
invaso = False

while not invaso:
    if not alieni:
        muovi_alieno_giu = 0
        movimento_alieno_dx_sx = MOVIMENTO_LATERALE_ALIENO
        for riga in range(5):
            for colonna in range(11):
                nuovo_alieno = {}
                nuovo_alieno["immagini"] = immagini_alieni[riga]
                nuovo_alieno["rettangolo"] = nuovo_alieno["immagini"][0].get_rect()
                nuovo_alieno["pos_immagine"] = 0
                nuovo_alieno["rettangolo"].centerx = posizione_primo_x + colonna * DISTANZA_LATERALE_ALIENO
                nuovo_alieno["rettangolo"].centery = posizione_primo_y + riga * DISTANZA_GIU_ALIENO
                alieni.append(nuovo_alieno)
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

    for alieno in alieni:
        if alieno["rettangolo"].bottom >= ALTEZZA or alieno["rettangolo"].colliderect(cannone_rettangolo):
            invaso = True

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

pygame.mixer.music.stop()
font = pygame.font.SysFont(None, 96)
testo = font.render('GAME OVER', 1, BIANCO)
testo_rettangolo = testo.get_rect()
testo_rettangolo.center = (LARGHEZZA/2, ALTEZZA/2)
schermo.blit(testo, testo_rettangolo)
pygame.display.flip()
while True:
    orologio.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
