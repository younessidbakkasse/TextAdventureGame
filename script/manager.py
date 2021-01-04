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

            # Creating main game scenes ########################################
            'Pregame' : StoryScene('Pregame', [['Start playing', 'Beach', 'normal']], "Hi there and welcome. Dead Island is story game, your actions impact the story flow. Decide carefully, check your inventory from time to time, equip best weapons because it's scary what's waiting you out there."),
            'Beach' : StoryScene('Beach', [['Explore the beach', 'Nothing', 'normal']], 'Washed ashore, you have only vague recollections of what happened. The past seems unimportant now. Shivering, you watch the bodies float among the debris. No ships can be seen on the horizon.'),
            'Nothing' : StoryScene('Nothing', [['Examine the object', 'Coin', 'normal']], 'There is nothing but sand and gravel. Or so it may seem. You feel a painful sensation in your left foot, causing you to take a step backwards. Glimmering in the sun, a sharp object is revealed.'),
            'Coin' : StoryScene('Coin', [['Continue exploring', 'Footprints', 'loot-golden coin']], "At first, you are unable to make sense of it. You pick it to get a closer look. It's a golden coin. Something about the unusual coin seems familiar."),
            'Footprints' : StoryScene('Footprints', [['Study the footprints', 'Person', 'normal'], ['Follow the footprints', 'Something', 'normal']], "You discover footprints in the sand, leading north. it's late in the afternoon. If there's another survivor out there, you should find this person before it gets dark."),
            # One step scene
            'Person' : StoryScene('Person', [['Follow the footprints', 'Something', 'normal']], 'They are somewhat small and delicate. You arrive at the concusion that they were made by a person below average height, walking barefoot.'),
            'Something' : StoryScene('Something', [['Leave it', 'Lagoon', 'normal'], ['Take the knife', 'Lagoon', 'loot-knife']], "Something near the water has caught your attention, prompting you to take a quick look. Closer scrutiny reveals a rusty knife. While hardly ideal, it's better than nothing."),
            # Lagoon
            'Lagoon' : StoryScene('Lagoon', [['Take a look around', 'First enemy', 'normal']], "Further north, the beach gives way to a flourishing wetland. You discover a lagoon, surrounded by red pines. At this point there are no more footprints."),
            # Fight scene
            'First enemy' : StoryScene('First enemy', [['Fight', 'First blood', 'fight-wild dog']], "Something is moving through the reeds on the other side. A wild dog emerges. Growling, it runs towards you across the shallows."),
            'First blood' : StoryScene('First blood', [['Cross the shallows', 'Shallows', 'normal']], "Whimpering, the wild dog collapses. Slowly, the carcass starts to drift into the lagoon."),
            # won the fight 
            'Shallows' : StoryScene('Shallows', [['Study the footprints', 'Match', 'normal'], ['Approach the shack', 'Shack', 'normal']], "Tucked away in lush vegetation, a small shack lies on the outskirts of a deep forest.  You discover a fresh set of footprints on a dirt path nearby, leading into the northern forest."),
            'Match' : StoryScene('Match', [['Follow the footprints', 'Women', 'normal'], ['Approach the shack', 'Shack', 'normal']], "They match the footprints from the beach, as far as you can tell."),
            'Women' : StoryScene('Women', [['Keep going...', 'Forest', 'normal']], "Crossing a bridge over a stream, you realise that you are bieng watched. Armed with spears, two women observe you from a distance. They are dressed in green cloaks and blue tunics."),
            'Forest' : StoryScene('Forest', [['Approach the camp', 'Camp', 'normal']], "Seemingly without end, the winding path takes you deep into the forest. The pines are now enveloped by the shimmering light of the golden dusk. Smoke is rising from a campfire in the distance."),
            'Camp' : StoryScene('Camp', [['Search the camp', 'Hat', 'loot-wizard hat'], ['Follow the footprints', 'Blood', 'normal']], "There is blood all over the place. A wounded man lies on his back near the campfire. He's dressed in green cloak, just like the other forest-dwellers."),
            'Hat' : StoryScene('Hat', [['Check the other camp', 'Blood', 'normal']], "You just found a wizards hat, and you are wondering, how it could help you to survive in this bloody island."),
            'Blood' : StoryScene('Blood', [['Keep moving', 'Owl', 'normal']], "The bloodstained footprints lead to another path throught the forest. Forging ahead, you are faced with increasingly rugged terrain. Forced to constantly walk uphill, you lose yourself on the northern highlands."),
            'Owl' : StoryScene('Owl', [['Explore the forest hills', 'Bodies', 'normal']], "Your eyes adjust to the merciful darkness of spring. the full moon provides further assistance . The owls remind you that one is never truly alone in the forest."),
            'Bodies' : StoryScene('Bodies', [['Keep going fast', 'Someone', 'normal']], "A trail of dead bodies guides your ascent. You thinks that who ever did this must be a human."),
            'Someone' : StoryScene('Someone', [['Talk to the man', 'Witch', 'normal']], "You enter a moonlit grove on top of the hill. Exuberant cherry blossoms form a perfect circle around the meadow. the grass is darkened by the entrails of numerous corpses. A man stands alone in the center."),
            'Witch' : StoryScene('Witch', [['Dodge his attack ', 'Victory', 'fight-witch']], "You asked about the dead bodies. The man turned his face, with an agressive accent, trying to hit you with his enchanted wand. You just realised that he is a witch."),
            'Victory' : StoryScene('Victory', [['Go back to the shack', 'Shack', 'normal'], ['Search the witch', 'Shack', 'loot-blue potion']], "The witch is dead trying to tell his last words. He was talking about a key to get out of the island."),

            # the shack
            'Shack' : StoryScene('Shack', [['Enter the shack', 'Inside0', 'normal']], "The front door has been left slightly ajar. Partialy broken, it may have been opened by force."),
            'Inside0' : StoryScene('Inside0', [['Take the food', 'Inside1', 'loot-bread'], ['Climb the ladder', 'Loft0', 'normal']], "Someone has been here quite recently. A pile of bread has been discarded on the worktable in front of you. Facing the northern forest, there's a small window next to ladder."),
            'Inside1' : StoryScene('Inside1', [['Climb the ladder', 'Loft0', 'normal']], "Someone has been here quite recently. A pile of braead has been discarded on the worktable in front of you. There's also a book on the table. Facing the northern forest, there's a small window next to ladder."),
            'Loft0' : StoryScene('Loft0', [['Grab the book', 'Loft1', 'loot-book'], ['Climb back down', 'Inside2', 'normal']], "There's a loft up here. covered by dust and cobwebs, an old book lies to a moldy mattress."),
            'Loft1' : StoryScene('Loft1', [['Climb back down', 'Inside2', 'normal']], "There's a loft up here. covered by dust and cobwebs, an old book lies to a moldy mattress."),
            'Inside2' : StoryScene('Inside2', [['Go outside', 'Outside', 'normal']], "This place reeks of mold and ancient dust."),
            'Outside' : StoryScene('Outside', [['Attack', 'Snake', 'fight-great snake'], ['Ignore the snake', 'Outside shack', 'normal']], "When you open the door, you notice a huge snake lurking outside. It keeps it's distance, perhaps anticipating your next move."),
            'Snake' : StoryScene('Snake', [['Move on', 'Outside shack', 'normal']], "You have slain the big snake. the reptile lies on the ground, bleeding and twitching."),
            'Outside shack' : StoryScene('Outside shack', [['Go behind the shack', 'Behind shack', 'normal'], ['Follow the footprints', 'Women', 'normal']], "You're standing in front of the abandoned shack near the forest. it's quiet out here, for now. A fresh set of footprints are visible in the forest path."),
            'Behind shack' : StoryScene('Behind shack', [['Go behind the shack', '', 'normal'], ['Follow the footprints', 'Women', 'normal']], "You're standing in front of the abandoned shack near the forest. it's quiet out here, for now. A fresh set of footprints are visible in the forest path."),
            }

    def run(self):
        self.scenes['Home'].run_scene()  

game = Game()