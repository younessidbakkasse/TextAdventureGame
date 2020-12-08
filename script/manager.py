from scene import Scene, StoryScene
from template import (
    home_template,
    menu_template,
    before_game_template,
    inventory_template,
    credit_template,
    howtoplay_template,
    stats_template,
    store_template, 
    quests_template,
)   


class Game:
    def __init__(self):
        # constructing user expercience scenes 
        self.scenes = {
            'home' : Scene('home', home_template),
            'menu' : Scene('menu', menu_template),
            'before game' : Scene('before game', before_game_template),
            'inventory' : Scene('inventory', inventory_template),
            'credit' : Scene('credit', credit_template),
            'how to play' : Scene('how to play', howtoplay_template),
            'stats' : Scene('stats', stats_template),
            'quests' : Scene('quests', quests_template),
            'store' : Scene('store', store_template),

            'game' : StoryScene('game', ['play', 'go back'], ['you are about to meet him']),
            'play' : StoryScene('play', ['read map', 'kill the dragon'], ['you just fall in forest', 'but you found out'])
        }

    def run(self):
        self.scenes['home'].run_scene()  

game = Game()

