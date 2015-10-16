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
sudo apt-get install python-dev python3-dev
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

# pygame su Mac

Riferimento originale http://brysonpayne.com/2015/01/10/setting-up-pygame-on-a-mac/


I have compiled a replicable, dependable, almost understandable set of steps to install Pygame for Python 3 that has 
worked across four generations of Mac OS X. Pieces of these steps appear in two or three other how-to’s on the web, but 
this full process has been carefully tested across Mac OS X 10.6-10.9, and I’m posting the steps here to solicit 
feedback from Pygame-curious Mac users out there.

I had run into a tough situation – I wrote a book this past year using Python as the language, and in the last three 
chapters, I showed readers how to build playable, interactive games using Pygame. The problem is that Pygame is 
challenging to get working on Python 3 on a Mac – and a lot of my readers are Mac users.

Mac users have essentially the following three options if they want to use Pygame:

1. You can install an older version of Python, like Python 2.7, along with Pygame 1.9.2 for Mac OS X in a new location 
on your Mac for Pygame programming.
2. If you have access to a Windows PC, you may find it easier to install the Windows version of Python and Pygame…
3. Or, you can follow the steps listed below to install Pygame for Python 3.4 on your Mac – if you’re doing this at 
school or at work, you will probably need IT support.

## How to install Pygame for Python 3 on Mac OS X successfully, every time:

1. *Install Xcode*: In Finder, open Applications, App Store. Search for Xcode and click Get to install the **Xcode** 
developer tools. You’ll need these developer tools to run some of the command-line instructions in a Terminal window 
below.
2. *Install XQuartz*: Go to http://xquartz.macosforge.org and download the current version of XQuartz (2.7.7 as of this 
writing). Open your Downloads folder, double-click on the XQuartz-2.7.7.dmg file, then double-click on the XQuartz.pkg 
package file and follow the instructions to complete the installation.
3. *Open a Terminal (command-line) window*: Go to Applications, Utilities, and double-click Terminal. Your command-line 
Terminal window will open. All the following commands must be typed exactly as they appear in the Terminal window, one 
line at a time.
4. *Install Homebrew*: At the Terminal command line prompt, type the following as a single full line (you may want to 
expand your Terminal window wider to allow it to fit, but it’s okay if it wraps around):
```
ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”
```
then, hit return. Homebrew is a free program that helps you install Python, Pygame, and other programs on a Mac.
5. *Prepare Homebrew for use*: At the Terminal prompt, type each of the following three commands exactly as shown – the 
second two may take a few moments to run and will show several screens of information, but keep following the steps one 
line at a time.
```
echo export PATH=’/usr/local/bin:$PATH’ >> ~/.bash_profile
brew update
brew doctor
```
6. *Install Python 3 for Pygame*: At the Terminal prompt, type:
```
brew install python3
```
This will install a separate Python 3 specifically for Pygame use – this is required for all the following steps to work.
7. *Install Mercurial*: Still at the Terminal prompt, type:
```
brew install mercurial
```
Mercurial is a free source control management system that this installation of Pygame requires on a Mac.
8. *Install Pygame dependencies*: Pygame requires several other helper programs, called dependencies, so that it can 
show animations, play sounds, and create game graphics. Type the following three lines at the Terminal command prompt, 
hitting return after each line
```
brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
brew tap homebrew/headonly
brew install smpeg
```
(**NOTE 18JUL2015**: Updated to reflect changes to the smpeg library; if you have any trouble here, try 
`brew install –HEAD smpeg` instead, with two dashes/hyphens before the HEAD option).
Each command will take a few moments to run and display screens full of information; keep going, you’re almost done…
9. *Install Pygame*: Type the following line at the Terminal prompt and hit return:
```
sudo pip3 install hg+http://bitbucket.org/pygame/pygame
```

You may have to enter an administrator password (your password, or ask an IT administrator for help at school, work, or 
the library), and the installation may take a few minutes.
As mentioned in step 6 above, this process creates a second full Python environment (under /usr/local/Cellar) on your 
Mac. You’ll want easy access to your Pygame-enabled Python…

## Create a desktop shortcut to your new Pygame IDLE editor:

The new Pygame and Python 3 that you just installed creates a separate IDLE editor app that you’ll use especially for 
Pygame-enabled apps. (Note: You can use this new IDLE for all your Python development, if you wish.)

1. Go to Finder > Go > Go to Folder…
2. In the Go to the folder: window prompt, type /usr/local/Cellar/python3 and click Go.
3. Double-click to open the folder inside – it will be named with a version number (3.4.2_1 as of this writing), but 
the version is unimportant, just open the folder.
4. Inside this folder, you will find the IDLE 3 app. Hold down the control key and click on the IDLE 3 icon. Pressing 
control+clicking on the icon will open a popup menu; select the Make Alias option from that menu.
5. A new alias, or shortcut icon, will appear, with a name like IDLE 3 alias. Click on the file name to edit it, and 
rename the alias pygame IDLE or something similar, to help you remember that this IDLE has Pygame installed.
6. Drag the pygame IDLE icon to your Desktop. This will allow you to access the correct IDLE for Pygame programming 
right from your Desktop.
7. Double-click the pygame IDLE icon. The Pygame-enabled IDLE editor window will open. Type import pygame and hit 
return. IDLE should respond with a >>> prompt and no errors.

** You’re ready to program Pygame apps on your Mac!**

If you’re tough enough to make it through all these steps, and you’re enjoying Pygame on your Mac, please leave a comment and let me know (also leave any corrections/issues) – I hope these instructions will help others have as much Pygame fun as my sons and I have enjoyed these past few years. Cheers!

