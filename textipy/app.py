from textipy import *


game.scenes['First Scene'] = StoryScene(
    name = 'First Scene',  
    buttons = [
        ['Start the game', 'second scene', 'normal'],
    ], 
    text = "The front door has been left slightly ajar. Partialy broken, it may have been opened by force." 
)

game.run() 

