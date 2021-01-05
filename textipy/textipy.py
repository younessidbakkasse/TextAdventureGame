from scene import Scene, StoryScene, Gui
from template import (
    home_template,
    menu_template,
    inventory_template,
    credit_template,
    howtoplay_template,
    stats_template,
    store_template, 
    quests_template,
    fight_template,
    gameover_template,
)   

class Game:
    def __init__(self):
        # Constructing GUI scenes 
        self.scenes = {
            # Paused scenes ##################################################
            'Home' : Scene('home', home_template),
            'Menu' : Scene('menu', menu_template),
            'Inventory' : Scene('inventory', inventory_template),
            'Credit' : Scene('credit', credit_template),
            'Help' : Scene('how to play', howtoplay_template),
            'Stats' : Scene('stats', stats_template),
            'Quests' : Scene('quests', quests_template),
            'Store' : Scene('store',store_template),
            'Fight' : Scene('fight', fight_template),
            'Game Over' : Scene('game over', gameover_template),
        }

    def run(self):
        self.scenes['Home'].run_scene()  

game = Game()
