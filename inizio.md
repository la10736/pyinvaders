# Sfondo, musica e la nostra astronave

Eccoci davanti al foglo bianco, vediamo di rimepirlo. Vogliamo fare una bella finestra che resta aperta fino a quando 
non la chiudiamo con il nostro cannone fermo in basso al centro e una musica di sottofondo.

## Una bella finestra nera

Per prima cosa creiamo semplicemente il campo di gioco che consiste in una finestra nera larga 640 pixels (punti) e
alta 480.

```python
import pygame

altezza = 480
larghezza = 640

dimensioni_scehrmo = larghezza, altezza
nero = 0, 0, 0
pygame.init()

schermo = pygame.display.set_mode(dimensioni_scehrmo)
schermo.fill(nero)
pygame.display.flip()
```

Ora provimo a farlo partire e vediamo cosa succede.... Ecco una bella finestra vuota e nera:

![Finestra vuota e nera](vuoto.png)

... che si chiude subito :(

Poco male dato che è ora di scoprire cosè il **ciclo main di pygame**.

## Il ciclo main di `pygame`

Quando si esegue un gioco con `pygame` é come se ci fosse un direttore di orchestra che detta il tempo: *tutte le 
volte che il direttore di orchestra muove la bacchetta, bisogna eseguire i propri compiti e aspettare il prossimo 
movimento*.

Per costruire questo direttore di orchestra bisogna chiedere a `pygame` un *oroglogio* che ci aiuterà ad aspettare con
precisione il prossimo colpo di bacchetta.

```python
orologio = pygame.time.Clock()
while True:
    # Chiediamo all'orologio di aspettare fino al prossimo colpo di 
    # bacchetta e di fare 20 colpi di bacchetta al secondo
    orologio.tick(20)
    Il lavoro da fare prima di aspettare il prossimo tocco
```

Questi colpi si chiamano **frame** (fotogrammi), come in un film noi disegnamo tante foto da mostrare una dopo l'altra
con un ritmo di 20 al secondo. Quindi in ogni **frame** dobbiamo ridisegnare il nostro schermo:

```python
orologio = pygame.time.Clock()
while True:
    orologio.tick(20)
    schermo.fill(nero)
    pygame.display.flip()
```    

Ed ecco che la nostra finestra non si chiude più... ma proprio più :). Provate con il quadrato rosso in basso a sinistra
che dovrebbe uccidere il programma.

## Comunicare con un programma pygame

Per capire cosa sta facendo il giocatore, i programmi `pygame` devono *ascoltare e reagire a quello che succede*. Quello
che succede sono pressione di tasti, movimenti del mouse, click ... richieste di chiusura della finestra. Siamo noi che
dobbiamo istruire il nostro gioco a fa¶e la cosa giusta quando succede qualcosa.

Quindi ora diremo che quando qualcuno vuole chiudere il programma bisogna uscire. Per fare questo bisogna analizzare 
tutti gli eventi che arrivano e se troviamo una richiesta di uscita uscire:

Quindi, prima di disegnare ogni frame scriviamo

```python
for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
        import sys
        sys.exit()
```

Cioè per ogni **evento** che è successo si verifica se l'evento è una richiesta di uscita `pygame.QUIT`

Quindi adesso il vostro gioco si chiude quando cercate di chiudere la finestra.

## Disegnamo il cannone

Per disegnare il cannone bisogna leggere l'immagine del cannone, costruire un rettangolo grande come l'immagine e
tutte le volte che vorremo disegnare il cannone posizioniamo il rettangolo sullo scermo e diciamo allo scrmo di
riempire il rettangolo con quella immagine. Troppe parole: facciamo spazio al codice:

```python
cannone_immagine = pygame.image.load("cannone.png")
cannone_rettamgolo = cannone_immagine.get_rect()
cannone_rettamgolo.centerx = larghezza / 2
cannone_rettamgolo.bottom = altezza

...
   # Prima di riempire il display
   schermo.blit(cannone_immagine, cannone_rettamgolo)

```

