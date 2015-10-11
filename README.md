# Space Invaders

## A chi è rivolto il tutorial?

Questo tutorial è rivolto a chi ha già provato a scrivere qualcosa in *Python* e si vuole cimentare con la costruzione
di un **gioco vero**. Bisogna saper maneggiare le cose base in Python come

* Assegnamenti
* Cicli
* Condizioni
* Funzioni

Impareremo a usare le cose base di *pygame* per muovere personaggi, usare la musca e gli effetti sonori. Dovremo 
anche usare liste per tenere memoria di tutti i nemici e gli spari.

## Lo scopo del Gioco

**Uccidere tutti gli alieni prima che tocchino terra.**

Gli alieni si mettono in formazione quando inizia la partita e piano piano si muovono verso destra fino a quando almeno
uno tocca il bordo di destra a questo punto scendono di un passo e poi si muovono a sinistra fino a quando.non toccano
il bordo di destra scendendo ancora e ricominciando verso destra. Noi Abbiamo una astronave che si trova sul fondo a 
diferndere la terra e spara dei missili che quando raggiungono gli alieni li distruggono. A loro volta ogni tanto un
alieno lancia una bomba a sua volta e la nostra astronave è meglio che non venga colpita, altrimenti si distrugge.

Man mano che gli alieni diminuiscono accelerano il loro passo e sparano sempre più veloce. 

* Se gli alieni toccano terra o l'astronave vincono loro
* Se gli alieni finiscono si ricostruiscono tutti e ricominciano l'invasione un po più veloce
* Possiamo essere colpiti solo 3 volte in tutto e poi il gioco finisce
* Ogni alieno colpito vale 10, 20 o 40 punti a seconda del tipo di alieno

## La Strada

Questo è il percorso che faremo per arrivare al programma finale

1. [pygame Apriamo la finestra disegnando un cannone e suonando la musica](inizio.md)
2. [Muoviamo il cannone con le frecce e spariamo caon la barra](muovi.md)
3. [Alieno animato che si sposta](alieno.md)
4. [Colpisci l'alieno e preparati all'invasione con due alieni](alieno_colpito.md)
5. [L'invasione](invasione.md)
6. [Punti e alieni che sparano](punti_spari.md)

* Prossimo: [Sfondo, musica e il nostro cannone](inizio.md) 