from textipy import *          


# always chose 'Pregame' as a name of the first scene
game.scenes['Pregame'] = StoryScene(
        name='Pregame', 
        buttons=[['Start playing', 'Beach', 'normal']], 
        text="Hi there and welcome. Dead Island is story game, your actions impact the story flow. Decide carefully, check your inventory from time to time, equip best weapons because it's scary what's waiting you out there."
)

game.run() 