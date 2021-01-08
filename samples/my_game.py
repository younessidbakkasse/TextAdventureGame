from textipy import *          


# always chose 'Pregame' as a name of the first scene
game.scenes['Pregame'] = StoryScene(
        name = 'Pregame',  #the name is required so that you can link scenes with each others.
        buttons = [['Start the game', 'second scene', 'normal']],  #the first element is the text on the button
        text = "The front door has been left slightly ajar. Partialy broken, it may have been opened by force." # the scene text
)

game.run() 