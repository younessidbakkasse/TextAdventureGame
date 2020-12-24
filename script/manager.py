from scene import Scene, StoryScene
from template import (
    home_template,
    menu_template,
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
            'inventory' : Scene('inventory', inventory_template),
            'credit' : Scene('credit', credit_template, scene_type='pause'),
            'how to play' : Scene('how to play', howtoplay_template, scene_type='pause'),
            'stats' : Scene('stats', stats_template, scene_type='pause'),
            'quests' : Scene('quests', quests_template, scene_type='pause'),
            'store' : Scene('store',store_template, scene_type='pause'),

            # Creating main game scenes
            'pregame' : StoryScene('Pregame', ['Start playing'], 'Hi there, this is a story game. are you sure you wanna play. its scary out there !'),
            'Start playing' : StoryScene('Beach', ['Explore the beach'], 'Washed ashore, you have only vague recollections of what happened. The past seems unimportant now. Shivering, you watch the bodies float among the debris. No ships can be seen on the horizon.'),
            'Explore the beach' : StoryScene('Nothing', ['Examine the object'], 'There is nothing but sand and gravel. Or so it may seem. You feel a painful sensation in your left foot, causing you to take a step backwards. Glimmering in the sun, a sharp object is revealed.'),
            'Examine the object' : StoryScene('Coin', ['Continue exploring'], "At first, you are unable to make sense of it. You pick it to get a closer look. it's a silver coin. Something about the unusual coin seems familiar."),
            'Continue exploring' : StoryScene('Footprints', ['Study the footprints', 'Follow the footprints'], "You discover footprints in the sand, leading north. it's late in the afternoon. If there's another survivor out there, you should find this person before it gets dark."),
        }

    def run(self):
        self.scenes['home'].run_scene()  

game = Game()

