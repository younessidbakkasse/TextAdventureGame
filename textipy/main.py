""" This game is made by Youness ID BAKKASSE; https://github.com/younessidbakkasse/
    its a school project to initiat with Python programming 
  more informations and licence please check README file attached to the folder. 
"""
from textipy import game, scenario_en

if __name__ == "__main__":
    game.scenes.update(scenario_en)
    game.run()