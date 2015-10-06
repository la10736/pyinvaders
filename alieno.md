# Un Alieno

Ora vogliamo inserire il primo alieno, animarlo e farlo muovere per lo schermo. Per fare questo dovremo

1. Caricare le immagini dell'alieno e costruire il rettangolo
2. Fissare una posizione di partenza del rettangolo e disegnarci l'immagine dell'alieno
3. A intervalli regolari cambiare l'immagine dell'amieno da disegnare
3. Cambiare la posizione dell'alieno quando serve per andare a destra o sinistra

# Caricare le immagini dell'alieno

Come potete vedere ci sono 3 tipi di alieni e per ogni alieno ci sono 2 immagini. I nomi delle immagini le trovate nella
directory del progetto e sono del tipo `alieno_?_?.png` dove nel primo punto interrogativo troviamo il numero 
dell' alieno e nel secondo il tipo di immagine (1 o 2). Per ora vogliamo usare solo alieno 1 eper caricare le due 
immagini e costruire il rettangolo possiamo usare:

```python
alieno_1_immagine_1 = pygame.image.load("alieno_1_1.png")
alieno_1_immagine_2 = pygame.image.load("alieno_1_2.png")
alieno_rettangolo = alieno_1_immagine_1.get_rect()
```

Il rettangolo si costruisce usando una delle due immagini (tanto sono grandi uguali).


Le cose iniziano a essere un po complicate e tutti questi numerini sono noisi... è ora di imparare qualcosa di nuovo!

Aprite la console e scrivete 

```python
>>> numeri = 1,2, 3, 7,10
>>> numeri
(1, 2, 3, 7, 10)
>>> numeri[2]
3
>>> numeri[4]
10
>>> numeri[0]
1
>>> for n in numeri:
...     print(n)
... 
1
2
3
7
10
```

Dentro a `numeri` abbiamo messo un tanti numeri diversi e abbiamo potuto prendere quello che ci serviva 
semplicemente scrivendo `numeri[posizione]` inoltre con il ciclo for possiamo girarli tutti semplicemente.

Quindi possiamo invece di usare due nomi per le immagini dell' alieno possiamo usare un nome solo che contiene entrambe
le immagini:

```python
alieno_1_immagine = pygame.image.load("alieno_1_1.png"), pygame.image.load("alieno_1_2.png")
alieno_rettangolo = alieno_1_immagine[0].get_rect()
```

