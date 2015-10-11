# Conteggio punti e alieni che sparano

Ci occupiamo adesso di contare i punti, far sparare gli alieni e accelerare il movimento degli alieni ogni volta che li 
distruggiamo tutti che vengono ricostruiti.

## Contare i punti

Ogni tipo di alieno vale diversamente:

* Quelli più in alto valgono di più: ben 40 punti
* Quelli in mezzo 20 punti
* Quelli in basso 10 punti

Questi punti sembrano un attributo degli alieni e quindi un nuovo campo nel dizzionario di ogni alieno. Come per le
immagini immagazziniamo questa informazione suddividendola per riga. Questa volta possiamo scrivere il dizzionario
direttamente dato che i campi sono semplici:

```python
punti_alieni = {0: 40, 1: 20, 2: 20, 3: 10, 4: 10}
```

Ora tutte le volte che creiamo un alieno dobbiamo indicare anche quanti punti vale con 

```python
nuovo_alieno["punti"] = punti_alieni[riga]
```

Adesso iniziamo impostando `punti = 0` alla partenza e ogni volta che un alieno viene colpito sommiamo i punti che vale
proprio sotto a `alieni.remove(alieno)`

```python
punti = 0
...
punti = punti + alieno["punti"]
```

Ora per verificare se tutto funziona ogni volta che aumentiamo i punti scriviamo:

```python
print("PUNTI :" + str(punti))
```

Adesso, dopo aver disegnato gli alieni e prima di ridisegnare lo schermo con `pygame.display.flip()` disegniamo i punti 
in alto a sinistra:

```python
    font = pygame.font.SysFont(None, 48)
    testo_punti = font.render(str(punti), 1, bianco)
    punti_rettangolo = testo_punti.get_rect()
    punti_rettangolo.topleft = 30, 5
    schermo.blit(testo_punti, punti_rettangolo)
```

e togliamo la vecchia stampa dei punti che non serve più.

## Gli spari degli alieni

Gli spari degli alieni partono a caso. Quindi gli spari possono essere tanti (una lista come per gli alieni) esono 
fatti di due immagini (come gli alieni). A differenza degli alieni tra i diversi spari cambia solo il rettangolo e 
quindi mettiamo solo quello nella lista.

Per provare gli spari invece di farli generare a caso usiamo un bottone: la lettera **A**.
 
Andiamo con ordine. Ci servono:

1. `VELOCITA_SPARO_ALIENO = 10` che mettiamo sopra
2. Fare la lista di spari, caricare le immagini dello sparo e fissare il numero dell'immagine da mostrare
3. Far partire lo sparo (aggiungere un rettangolo alla lista) quando si preme il tasto **A** e posizionarlo su un alieno
4. A ogni frame alternare le immagini da disegnare
5. A ogni frame muovere tutti gli spari e verificare quelli da rimuovere o che colpiscono il cannone
6. Disegnare gli spari

### 2 Fare la lista di spari, caricare le immagini dello sparo e fissare il numero dell'immagine da mostrare

Prima del ciclo main di `pygame`

```python
spari = []
immagini_sparo_alieno = pygame.image.load("sparo_alieno_1.png"), pygame.image.load("sparo_alieno_2.png")
sparo_alieno_pos = 0
```

### 3 Far partire lo sparo quando si preme il tasto **A** e posizionarlo

Aggiungere tra gli eventi

```python
if evento.type == pygame.KEYDOWN and evento.key == ord("a"):
    rettangolo_nuovo_sparo_alieno = immagini_sparo_alieno[0].get_rect()
    alieno_che_spara = random.choice(alieni)
    rettangolo_nuovo_sparo_alieno.midbottom = alieno_che_spara["rettangolo"].midbottom
    spari.append(rettangolo_nuovo_sparo_alieno)
```

... all'inizio del programma

```python
import random
```

### 4 Alternare le immagini da disegnare
    
Prima di iniziare a disegnare

```python
sparo_alieno_pos = sparo_alieno_pos + 1
if sparo_alieno_pos > 1:
    sparo_alieno_pos = 0
```

### 5 muovere tutti gli spari e verificare quelli da rimuovere

Prima di iniziare a disegnare

```python
for sparo_alieno in spari:
    if sparo_alieno.top > altezza:
        spari.remove(sparo_alieno)
    if sparo_alieno.colliderect(cannone_rettangolo):
        spari.remove(sparo_alieno)
        print("CANNONE COLPITO")
    sparo_alieno.bottom = sparo_alieno.bottom + VELOCITA_SPARO_ALIENO
```

### 6 Disegnare gli spari

Prima di iniziare a disegnare

```python
for sparo_alieno in spari:
    schermo.blit(immagini_sparo_alieno[sparo_alieno_pos], sparo_alieno)
```


Ora cambiamo lo sparo creato con il bottone **A** con un evento casuale. Per fare questo creiamo un nuovo evento come 
abbiamo fatto per il movimento degli alieni solo che cambiamo l'intervallo ogni volta con un numero casuale:

```python
SPARO_ALIENO_EVENTO = pygame.USEREVENT + 2
FREQUENZA_SPARI_ALIENI_MILLISECONDI = 2300
...
pygame.time.set_timer(SPARO_ALIENO_EVENTO, random.randint(1, FREQUENZA_SPARI_ALIENI_MILLISECONDI))
...
if evento.type == SPARO_ALIENO_EVENTO:
    ...
    pygame.time.set_timer(SPARO_ALIENO_EVENTO, random.randint(1, FREQUENZA_SPARI_ALIENI_MILLISECONDI))
```

Dove il primo pezzo va allinizio del programma, il secondo dove impostavamo il timer del movimento, 
`if evento.type == SPARO_ALIENO_EVENTO` sostituisce la verifica del tasto **A** e il nuovo timer dopo aver aggiunto
lo sparo.

## Accelerare gli alieni

Per accelerare gli alieni è sufficiente diminuire il tempo con il quale viene creato l'evento di movimento:

```python
BASE_FREQUENZA_MOVIMENTO_ALIENI_MILLISECONDI = 1000
...
frequenza_movimento_alieni = BASE_FREQUENZA_MOVIMENTO_ALIENI_MILLISECONDI
...
frequenza_movimento_alieni = int(frequenza_movimento_alieni / 4) * 3
pygame.time.set_timer(MUOVI_ALIENI_EVENTO, frequenza_movimento_alieni)
```

La prima riga all'inizio, la seconda prima del ciclo main di `pygame` e l'ultimo blocco tutte le volte che ricostruiamo 
gli alieni.

## Dove siamo adesso

![Anche loro Sparano](sparano.png)

Ci siamo [quasi](src/punti_spari.py). Facciamo scoppiare il cannone quando è colpito e limitiamo i cannoni.

* Prossimo: [Solo 3 cannoni](3_cannoni.md)
* Precedente: [L'invasione](invasione.md)