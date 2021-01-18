""" This is a game sample is made by Youness ID BAKKASSE; https://github.com/younessidbakkasse/
    the scenario_en is a dict full of already made text and buttons in english, you can use 
    the french version by remplacing 'scenario_en' 'to scenario_fr'.
"""
from textipy import game, scenario_en

if __name__ == "__main__":
    # Remove this line if you want to start your game from scratch
    game.scenes.update(scenario_en)
    # This is the only thing you need to starts your game    
    game.run()