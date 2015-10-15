# Space Invaders

## A chi è rivolto il tutorial?

Questo tutorial è rivolto a chi ha già provato a scrivere qualcosa in *Python* e si vuole cimentare con la costruzione
di un **gioco vero**. Bisogna saper maneggiare le cose base in Python come

* Assegnamenti
* Cicli
* Condizioni
* Eseguire Funzioni

Useremo:

* `pygame` per muovere i personaggi, suanare musica e fare effetti sonori
* liste per tenere in memoria un numero variabile di personaggi
* dizzionari per mantenere alcune cose più ordinate

## Lo scopo del Gioco

**Uccidere tutti gli alieni prima che tocchino terra.**

Gli alieni si mettono in formazione quando inizia la partita e piano piano si muovono facendo una serpentina a destra 
e sinistra scendendo ogni volta che toccano il bordo. Noi Abbiamo un cannone che si trova sul fondo a 
difendere la terra dall'invasione e spara dei missili che quando raggiungono gli alieni li distruggono. Ogni tanto 
qualche alieno lancia una bomba: se queste bombe colpiscono il cannone lo distruggono.

* Se gli alieni toccano terra o l'astronave vincono loro
* Se gli alieni finiscono si ricostruiscono tutti e ricominciano l'invasione un po più veloce
* Sono disponibili solo 3 cannoni, poi il gioco finisce
* Ogni alieno colpito vale 10, 20 o 40 punti a seconda del tipo di alieno

## La Strada

Questo è il percorso che faremo per arrivare al gioco finale

1. [pygame Apriamo la finestra disegnando un cannone e suonando la musica](inizio.md)
2. [Muoviamo il cannone con le frecce e spariamo caon la barra](muovi.md)
3. [Alieno animato che si sposta](alieno.md)
4. [Colpisci l'alieno e preparati all'invasione con due alieni](alieno_colpito.md)
5. [L'invasione](invasione.md)
6. [Conteggio punti e alieni che sparano](punti_spari.md)
7. [Solo 3 cannoni](3_cannoni.md)

* Prossimo: [Sfondo, musica e il nostro cannone](inizio.md) 