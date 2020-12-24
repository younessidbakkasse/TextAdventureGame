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
        # constructing GUI scenes 
        self.scenes = {
            'home' : Scene('home', home_template),
            'menu' : Scene('menu', menu_template, scene_type='pause'),
            'before game' : Scene('before game', before_game_template),
            'inventory' : Scene('inventory', inventory_template),
            'credit' : Scene('credit', credit_template, scene_type='pause'),
            'how to play' : Scene('how to play', howtoplay_template, scene_type='pause'),
            'stats' : Scene('stats', stats_template, scene_type='pause'),
            'quests' : Scene('quests', quests_template, scene_type='pause'),
            'store' : Scene('store',store_template, scene_type='pause'),

            # Creating main game scenes
            'game' : StoryScene('game', ['play', 'go back'], ['you are about to meet him']),
            'play' : StoryScene('play', ['read map', 'kill the dragon'], ['you just fall in forest', 'but you found out'])
        }

    def run(self):
        self.scenes['home'].run_scene()  

game = Game()

