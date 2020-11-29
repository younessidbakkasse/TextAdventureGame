from entities import Entity
from gui import Gui
import sys, pygame

# Eng : global variables
# Fr : 
DISPLAY_HEIGHT = 500
DISPLAY_WIDTH = 400

# create a gui
gui = Gui()

# create a player 
player = Entity()

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
            gui.render_background()
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
                    self.transition(game.ux_scenes)
    
    def transition(self, scenes):
        """ Eng : One hell of an importante method it checks if mouse points to a text or 
        button (rect) and also allows scene transitions from self to another depending 
        on the button's name"""
        """ Fr : """
        for button_name, button in self.buttons.items():
            self.mx, self.my = pygame.mouse.get_pos()   
            if button != None and button.collidepoint((self.mx, self.my)):
                for scene_key, scene in scenes.items():
                    if scene_key == button_name:
                        Scene.previous_scene = self.scene_name
                        # This may cause bugs in futur if it didn't ur a lucky mothafucka
                        self.buttons.popitem()
                        scene.run_scene()


        for button_name, button in gui.gui_buttons.items():
            self.mx, self.my = pygame.mouse.get_pos()   
            if button != None and button.collidepoint((self.mx, self.my)):
                for scene_key, scene in scenes.items():
                    if scene_key == button_name:
                        Scene.previous_scene = self.scene_name
                        # This may cause bugs in futur if it didn't ur a lucky mothafucka
                        scene.run_scene()


##########################
#CREATING FONCTIONS AS TEMPLATES
###########################
def layout(template):
    def render_gui():
        # render big centered logo
        gui.render_logo(30, False)
        # render UI buttons
        gui.render_ui_buttons()
        template()
    return render_gui

    

################################# Story Template #################################
@layout
def story_template():
    #story text
    gui.render_text('Hi there, this is a story game.', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2- 80), size = 18)
    gui.render_text('are you sure you wanna play its', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2- 58), size = 18)
    gui.render_text('scary out there !', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2- 36), size = 18)
    # render left direction buttons
    game.story_scenes[0][0].buttons['left'] = gui.render_button('button_large', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 30))
    gui.render_text('Play', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 30))


################################# Menu Template #################################
@layout
def menu_template():
    # render frame
    gui.render_image('./assets/frames/normal.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2))
    # render close button
    game.ux_scenes['menu'].buttons["fight"] = gui.render_button('button_close', 355, 155)
    # render menu pause title
    gui.render_text('Pause', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 80))
    # render menu options
    game.ux_scenes['menu'].buttons["new_game"] = gui.render_text('New Game', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 30), size = 30)
    game.ux_scenes['menu'].buttons["exit_game"] = gui.render_text('Exit Game', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 10), size = 30)
    game.ux_scenes['menu'].buttons["credit"] = gui.render_text('Credit', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 50), size = 30)
    

################################# Monster Fight Template #################################
@layout
def fight_template():
    pass

################################# Game Credit Template #################################
def credit_template():
    ## render frame
    gui.render_frame('big', 'credit')
    # render credit
    gui.render_text('Game design & production', int(DISPLAY_WIDTH/2), 160, size = 15)
    gui.render_text('Youness Id bakkasse', int(DISPLAY_WIDTH/2), 200, size = 25)
    gui.render_text('Sound effects', int(DISPLAY_WIDTH/2), 250, size = 15)
    gui.render_text('Soundhound.com', int(DISPLAY_WIDTH/2), 290, size = 25)


################################# Stats Template #################################
@layout
def stats_template():
    # render frame
    gui.render_frame('normal', 'stats')

    # render stats
    gui.render_text(f'Gold {int(player.gold)}', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 40))
    gui.render_text(f'Attack {int(player.attack)}', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 20))
    gui.render_text(f'Diffence {int(player.defence)}', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2))
    
    # render player's health bar
    gui.render_image('./assets/frames/bar.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 30))
    # render player's armor bar
    gui.render_image('./assets/frames/bar.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 65))

    # render icons
    gui.render_image('./assets/icons/heart.png', int(DISPLAY_WIDTH/2 - 65), int(DISPLAY_HEIGHT/2 + 30))
    gui.render_image('./assets/icons/level.png', int(DISPLAY_WIDTH/2 - 65), int(DISPLAY_HEIGHT/2 + 65))

    # render dynamique bar for both health and levels
    gui.render_rect(int(DISPLAY_WIDTH/2 - 50), int(DISPLAY_HEIGHT/2 + 20), int(125 * player.health/player.max_health), 20, Gui.colors['red'])
    gui.render_rect(int(DISPLAY_WIDTH/2 - 50), int(DISPLAY_HEIGHT/2 + 55), int(125 * player.current_xp/player.max_xp), 20, Gui.colors['yellow'])

    # render stats on bars
    gui.render_text(f'{int(player.health)}/{int(player.max_health)}', int(DISPLAY_WIDTH/2 + 10), int(DISPLAY_HEIGHT/2 + 32), size = 13)
    gui.render_text(f'Level {int(player.level)}', int(DISPLAY_WIDTH/2 + 10), int(DISPLAY_HEIGHT/2 + 67), size = 13)


################################# HomeTemplate #################################
def home_template():
    # render big centered logo
    gui.render_logo(150, True)
    # start game button
    game.ux_scenes['home'].buttons["fight"] = gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 160) 

################################# How to play Template #################################
def howtoplay_template():
    # render frame
    gui.render_frame('big', 'how to play')
    # render how to play content
    gui.render_text('Use your mouse to play', int(DISPLAY_WIDTH/2), 120, size = 15)


################################# Inventory Template #################################
def inventory_template():
    # render frame
    gui.render_frame('big', 'inventory')

    #render inventory boxes
    for i in range(3):
        for j in range(4):
            gui.render_image('./assets/frames/tall.png', int(80 * j + 80), int(150 + i * 120))

################################# Quests Template #################################
@layout
def quests_template():
    # render frame
    gui.render_frame('normal', 'quests')

    # render how to play content
    gui.render_text('current quest : Kill the boss', int(DISPLAY_WIDTH/2), 250)












class Game:
    def __init__(self):
        # constructing user expercience scenes 
        self.ux_scenes = {
            'home' : Scene('home', home_template),
            'menu' : Scene('menu', menu_template),
            'fight' : Scene('fight', story_template),
            'inventory' : Scene('inventory', inventory_template),
            'credit' : Scene('credit', credit_template),
            'how to play' : Scene('how to play', howtoplay_template),
            'stats' : Scene('stats', stats_template),
            'quests' : Scene('quests', quests_template)
        }

        # constructing mean game scenes 
        self.story_scenes = [[Scene(str(y) + "-" + str(x), story_template) for y in range(1)] for x in range(1)]
        self.i, self.j = 0, 0

    def run(self):
        self.ux_scenes['home'].run_scene()  

game = Game()
game.run()

