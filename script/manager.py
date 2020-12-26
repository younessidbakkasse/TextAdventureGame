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
            'Home' : Scene('home', home_template),
            'Menu' : Scene('menu', menu_template, scene_type='pause'),
            'Inventory' : Scene('inventory', inventory_template),
            'Credit' : Scene('credit', credit_template, scene_type='pause'),
            'Help' : Scene('how to play', howtoplay_template, scene_type='pause'),
            'Stats' : Scene('stats', stats_template, scene_type='pause'),
            'Quests' : Scene('quests', quests_template, scene_type='pause'),
            'Store' : Scene('store',store_template, scene_type='pause'),

            # Creating main game scenes
            'Prologue' : StoryScene('Pregame', ['Start playing'], 'Hi there, this is a story game. are you sure you wanna play. its scary out there !'),
            'Beach' : StoryScene('Start playing', ['Explore the beach'], 'Washed ashore, you have only vague recollections of what happened. The past seems unimportant now. Shivering, you watch the bodies float among the debris. No ships can be seen on the horizon.'),
            'Nothing' : StoryScene('Explore the beach', ['Examine the object'], 'There is nothing but sand and gravel. Or so it may seem. You feel a painful sensation in your left foot, causing you to take a step backwards. Glimmering in the sun, a sharp object is revealed.'),
            'Coin' : StoryScene('Examine the object', ['Continue exploring'], "At first, you are unable to make sense of it. You pick it to get a closer look. it's a silver coin. Something about the unusual coin seems familiar."),
            'Footprints' : StoryScene('Continue exploring', ['Study the footprints', 'Follow the footprints'], "You discover footprints in the sand, leading north. it's late in the afternoon. If there's another survivor out there, you should find this person before it gets dark."),

            # one step scene
            'Person' : StoryScene('Study the footprints', ['Follow the footprints'], 'They are somewhat small and delicate. You arrive at the concusion that they were made by a person below average height, walking barefoot.'),
            'Something' : StoryScene('Follow the footprints', ['Leave it', 'Take the knife'], "Something near the water has caught your attention, prompting you to take a quick look. Closer scrutiny reveals a rusty knife. While hardly ideal, it's better than nothing."),
            'Habon de la kaka' : StoryScene('Take the knife', ['mahmoudt', 'walid'], "je  mange le coucous a midi avec Majid"),
        }

    def run(self):
        self.scenes['Home'].run_scene()  

game = Game()

