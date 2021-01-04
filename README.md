# Adventure Text Game Engine
An easy way to create rpg text games using Python.

![Banner](/docs/home.png)


## Getting Started
1) Install Python 3.9 or newer. https://www.python.org/downloads/
2) Open cmd/terminal and install the newest version from git by typing:

        mkdir mygame
        cd mygame
        pip install git+https://github.com/younessidbakkasse/TextGameEngine 



If you want to easily edit the source, it's recommended to clone the git
repo and install as develop like this. Make sure you have git installed. https://git-scm.com/

        git clone https://github.com/younessidbakkasse/TextGameEngine

Also install pygame module using this command:

        pip install -r requirements.txt


On some systems you might have to use pip3 instead of pip in order to use Python 3 and not the old Python 2.


## Dependencies
  * pygame 1.9+
  
  
## Examples
``` python
from manager import *            # this will import everything we need from the engine manager with just one line.

game = Game()

game.scenes['First Scene'] = StoryScene(
        name = 'first scene',  #the name is required so that you can link scenes with each others.
        buttons = [['Start the game', 'second scene', 'normal']],  #the first element is the text on the button
        text = "The front door has been left slightly ajar. Partialy broken, it may have been opened by force." # the scene text
),

game.run()                       # opens a window and starts the game.
```


## How do I make a game?
This game engine is writing in 100% Python code. You can use any text editor you want, but personally I like to use Vscode.
1) Create an empty .py file called 'my_game.py' avoid names like game.py, manager.py, scene.py
2) Copy this text into your new file:
``` python
from manager import *            # this will import everything we need from the engine manager with just one line.

game = Game()

game.scenes['First Scene'] = StoryScene(
        name = 'first scene',  #the name is required so that you can link scenes with each others.
        buttons = [['Start the game', 'second scene', 'normal']],  #the first element is the text on the button
        text = "The front door has been left slightly ajar. Partialy broken, it may have been opened by force." # the scene text
),

game.run()                       # opens a window and starts the game.
```

3) Type this in the terminal to start the game:

       python my_game.py
   If you use Vscode, I recommend installing the python extension to tun on your scripts with the press of a button.

4) you can now control the game there a gui button such as inventory or profile, you can exit the game using the menu
selection exit game.

5) to link two scenes you need to create a sceond scene exemple below, and add it's name to the button destination list parameter, so when you click the button you directly convert the second scene.

``` python
from manager import *            # this will import everything we need from the engine manager with just one line.

game = Game()

game.scenes['First Scene'] = StoryScene(
        name = 'first scene',  #the name is required so that you can link scenes with each others.
        buttons = [['Start the game', 'second scene', 'normal']],  #the first element is the text on the button
        text = "The front door has been left slightly ajar. Partialy broken, it may have been opened by force." # the scene text
),

game.scenes['Second Scene'] = StoryScene(
        name = 'second scene',  #the name is required so that you can link scenes with each others.
        buttons = [
                ['Fight the dragon', 'third scene', 'fight-wild dog'], #first button
                ['Run away', 'third scene', 'normal'] # second button
        ],  
        # here third scene is not yet created
        text = "You just met a wild dog do you want to fight him or run away" # the scene text
),

game.run()                       # opens a window and starts the game.
```
