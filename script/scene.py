import sys, pygame
import template
from gui import Gui
# Eng : global variables
# Fr : 
DISPLAY_HEIGHT = 500
DISPLAY_WIDTH = 400

class Scene:
    """ Eng : This the Scene Class its a blueprint for every scene for exemple the starting scene
    has its own loop, its own get event loop, its own template or elements and using this Class 
    we can create as many scenes as we want """

    """ Fr: """

    # Eng : making list to store scenes upon creation 
    # Fr : 
    previous_scene = None

    def __init__(self, scene_name, template_closure):
        """ Eng: Constructor method runs every time I create a new scene or page. """
        """ Fr: Constructor method runs every time I create a new scene or page. """
        self.template = template_closure
        self.scene_name = scene_name
        self.running = True 

        """ Eng : every scene has it's own button (besides the gui_buttons) in order to navigate
        the game story """
        """ Fr : every scene has it's own button (besides the gui_buttons) in order to navigate
        the game story """
        self.buttons = {}

        # Eng : mouse coords
        # Fr : mouse coords
        self.mx, self.my = 0, 0

    def run_scene(self):
        """ Eng : scene's main loop : basicly each scene has its own loop """
        """ Fr : scene's main loop : basicly each scene has its own loop """
        while self.running:  
            template.gui.render_background()
            self.render_template()
            self.get_events()
            pygame.display.flip()
            Gui.clock.tick(60)
    
    def close_scene(self):
        """ Eng : """
        """ Fr : """
        self.running = False

    def render_template(self):
        """ Eng : """
        """ Fr : """
        self.template()

    def get_events(self):
        """ Eng : This function collects Mouse clicks (events) from the user """
        """ Fr : """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # Eng : to exit the game
                # Fr : 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button: 
                    self.transition(game.ux_scenes, game.story_scenes)
    
    def transition(self, ux_scenes, story_scenes):
        """ Eng : One hell of an importante method it checks if mouse points to a text or 
        button (rect) and also allows scene transitions from self to another depending 
        on the button's name"""
        """ Fr : """
        for button_name, button in self.buttons.items():
            self.mx, self.my = pygame.mouse.get_pos()   
            if button != None and button.collidepoint((self.mx, self.my)):
                for scene_key, scene in ux_scenes.items():
                    if scene_key == button_name:
                        Scene.previous_scene = self.scene_name
                        # This may cause bugs in futur if it didn't ur a lucky mothafucka
                        self.buttons.popitem()
                        scene.run_scene()
                    # when we click exit game menu option 
                    elif button_name == 'game':
                        story_scenes[0][0].run_scene()
                    elif button_name == 'exit':
                        pygame.quit()
                        sys.exit()
        
        # check for story scene that have keys '01' as exemple
        for button_name, button in self.buttons.items():
            self.mx, self.my = pygame.mouse.get_pos()   
            if button != None and button.collidepoint((self.mx, self.my)):
                for scene_key, scene in enumerate(story_scenes):
                    if scene_key == button_name:
                        scene.run_scene()
                    
        # this is to check for gui buttons
        for button_name, button in template.gui.gui_buttons.items():
            self.mx, self.my = pygame.mouse.get_pos()   
            if button != None and button.collidepoint((self.mx, self.my)):
                for scene_key, scene in ux_scenes.items():
                    if scene_key == button_name:
                        Scene.previous_scene = self.scene_name
                        # This may cause bugs in futur if it didn't ur a lucky mothafucka
                        scene.run_scene()

class Game:
    def __init__(self):
        # constructing user expercience scenes 
        self.ux_scenes = {
            'home' : Scene('home', template.home),
            'menu' : Scene('menu', template.menu),
            'before game' : Scene('before game', template.before_game),
            'inventory' : Scene('inventory', template.inventory),
            'credit' : Scene('credit', template.credit),
            'how to play' : Scene('how to play', template.howtoplay),
            'stats' : Scene('stats', template.stats),
            'quests' : Scene('quests', template.quests),
            'store' : Scene('store', template.store)
        }

        # constructing mean game scenes 
        self.story_scenes = [[Scene(str(y) + "-" + str(x), template.game) for y in range(10)] for x in range(10)]
        self.i, self.j = 0, 0

    def run(self):
        self.ux_scenes['home'].run_scene()  


game = Game()
game.run()










