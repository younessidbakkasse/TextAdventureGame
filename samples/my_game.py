from textipy import *


# exemple demo to create one game scene with one button
game.scenes['Pregame'] = StoryScene(
    # always name your first scene pregame
    name = 'Pregame',  
    buttons = [
        ['Start the game', 'second scene', 'normal'],
    ], 
    text = "The front door has been left slightly ajar. Partialy broken, it may have been opened by force." 
)

game.run() 

