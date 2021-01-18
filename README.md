# Textipy : An Adventure Text Game Engine
An easy way to create rpg textual games using Python.

![Banner](/docs/home.png)


## Getting Started
1) Install Python 3.9 or newer. https://www.python.org/downloads/

2) Open cmd/terminal and type:

        pip install textipy

The commande will also install pygame 2.0.1


If you want to install the newest version from git which is compatible with python 3.5 and above and to easily edit the source according to your needs, it's recommended to clone the git
repo and install like this. Make sure you have git installed. https://git-scm.com/

        git clone https://github.com/younessidbakkasse/textipy
        pip install pygame

you will have to install pygame for this to work.

On some systems you might have to use pip3 instead of pip in order to use Python 3 and not the old Python 2.

3) Start your first game screen by importing the game object.


## Dependencies
  * pygame 1.9+

  
## Examples
``` python
from textipy import *           # this will import everything we need from the engine manager with just one line.

game.run()                       # opens a window and starts the game.
```


## How do I make a game?
This game engine is writing in 100% Python code. You can use any text editor you want, but personally I like to use Vscode.
1) Create an empty .py file called 'my_game.py' avoid names like game.py, manager.py, scene.py
2) Copy this text into your new file:
``` python
from textipy import *          


# always chose 'Pregame' as a name of the first scene
game.scenes['Pregame'] = StoryScene(
        name = 'Pregame',  #the name is required so that you can link scenes with each others.
        buttons = [['Start the game', 'second scene', 'normal']],  #the first element is the text on the button
        text = "The front door has been left slightly ajar. Partialy broken, it may have been opened by force." # the scene text
)

game.run()                       # opens a window and starts the game.
```

3) Type this in the terminal to start the game:

       python my_game.py
   If you use Vscode, I recommend installing the python extension to tun on your scripts with the press of a button.

4) you can now control the game there a gui button such as inventory or profile, you can exit the game using the menu
selection exit game.

5) to link two scenes you need to create a sceond scene exemple below, and add it's name to the button destination list parameter, so when you click the button you directly convert the second scene.

``` python
from textipy import *            # this will import everything we need from the engine manager with just one line.

game.scenes['Pregame'] = StoryScene(
        name = 'Pregame',  #the name is required so that you can link scenes with each others.
        buttons = [['Start the game', 'Second Scene', 'normal']],  #the first element is the text on the button
        text = "The front door has been left slightly ajar. Partialy broken, it may have been opened by force." # the scene text
)

game.scenes['Second Scene'] = StoryScene(
        name = 'Second Scene',  #the name is required so that you can link scenes with each others.
        buttons = [
                ['Fight the dragon', 'third scene', 'fight-wild dog'], #first button
                ['Run away now', 'third scene', 'normal'] # second button
        ],  
        # here third scene is not yet created
        text = "You just met a wild dog do you want to fight him or run away" # the scene text
)

game.run()                       # opens a window and starts the game.
```

6) If you want to use an already made scenario for your game use the 'scenario_en' like below:

``` python
from textipy import *            # this will import everything we need from the engine manager with just one line.

game.scenes.update(scenario_en)

game.run()                       # opens a window and starts the game.
```

## Bugs
Please note that this is a pre-release version and, like all pre-releases, it certainly has bugs we don’t know about. If you run into any problems, please report them at : std.youness@gmail.com


# Contributions
Any pull requests are welcomed! We will have the code checked carefully. Please contact me at : std.youness@gmail.com if you have any thoughts on how to make this a better project.