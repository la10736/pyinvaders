# Usare `pygame` su PyCharm

Anche installando `pygame` usando l'interprete standard di pycharm non si riesce a caricare il modulo (da console 
funziona). Inoltre nelle opzioni dei virtualenv non si trova. La soluzione è installare dai sorgenti in un 
vitrtualenv nuovo, i passi sono i seguenti (testati su ubuntu 15.4)

1. Scaricare le dipendenze di `pygame`
2. Installare `virtualenv`
3. Costruire un nuovo virtualenv
4. Installare `pygame` dai sorgenti

```
sudo apt-get build-dep python-pygame
sudo apt-get install python-dev
mkdir -p ~/.virtualenvs/pygame
sudo apt-get install python-virtualenv
virtualenv --no-site-packages --distribute -p /usr/bin/python3.4 ~/.virtualenvs/pygame
. ~/.virtualenvs/pygame/bin/activate
pip install hg+http://bitbucket.org/pygame/pygame
```

Per testare lanciare python (viene eseguto quello del virtualenv come indicato dal prompt)
```
(pygame)michele@michele-asus:~$ python
```

e importate `pygame` con `import pygame`

Per chiudere il virtulenv usate `deactivate` (ovviamente dopo che siete usciti da python).

```
(pygame)michele@michele-asus:~$ deactivate
```

Ora su pycharm non vi resta che selezionare il nuovo virtualenv sia peril progetto che per l'interprete: 

* *File* -> *Settings...* -> *Project: ...* -> *Project Interpreter*

Ingranaggio in alto a destra, segno + poi *Add Local*. Navigate fino a `<home>/.virtualenvs/pygame/bin/python` 

Ora nella tendina scegliete 

* *<ver> virtualenv at ~/.virtualenvs/pygame`

Analogamente fate questo nella tendina di

* *Build, Execution and Deployment* -> *Console* -> *Python Console*
