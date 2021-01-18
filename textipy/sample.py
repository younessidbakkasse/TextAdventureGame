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
        text = "You just met a wild dog do you want to fight him or run away",# the scene text
)

game.run() 