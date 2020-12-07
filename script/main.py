from entities import Entity
import sys, pygame, random

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
        for button_name, button in gui.gui_buttons.items():
            self.mx, self.my = pygame.mouse.get_pos()   
            if button != None and button.collidepoint((self.mx, self.my)):
                for scene_key, scene in ux_scenes.items():
                    if scene_key == button_name:
                        Scene.previous_scene = self.scene_name
                        # This may cause bugs in futur if it didn't ur a lucky mothafucka
                        scene.run_scene()
        
        

        
            


class Gui:
    """ Eng : this class takes care of everything that has to do with rendering content and gui
    elements such as buttons, hover effect, text.."""

    """ Fr : this class takes care of everything that has to do with rendering content and gui
    elements such as buttons, hover effect, text.."""

    # Eng : initialising the pygame display and module it's a must
    # Fr : 
    pygame.init()
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()

    # Eng : display set up
    # FR :
    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    pygame.display.set_caption("Wood Runner", "favicon")

    # Eng : set up game favicon
    # Fr : 
    favicon = pygame.image.load("./assets/icons/favicon.png")
    pygame.display.set_icon(favicon)

    # Eng : the following loop generates random white squares
    # Fr :
    stars = [pygame.Rect(random.randint(0, DISPLAY_WIDTH), random.randint(0, DISPLAY_HEIGHT), 3, 3) for i in range(35)]
    # Eng : game color palette
    # Fr :
    colors = {
        "dark green" : (14, 43, 35),
        "dark blue" : (2, 17, 29),
        "white" : (251, 251, 251),
        "green": (18, 168, 113),
        "red" : (255, 0, 69),
        "yellow" : (250, 200, 50)
    }
    def __init__(self):
        self.gui_buttons = {}

    def render_ui_buttons(self, pause = False):
        """ Eng : renders the same user interface buttons acroos all the scenes and stores them on list"""
        """ Fr : """

        # Eng : buttons on the right side
        # Fr :
        self.gui_buttons["music"] = self.render_button('button_music_on', DISPLAY_WIDTH - 40, 40)
        self.gui_buttons["how to play"] = self.render_button("button_help", DISPLAY_WIDTH - 90, 40)

        # Eng : buttons on the left side
        # Fr :
        self.gui_buttons["store"] = self.render_button("button_cart", 90, 40)
        if not pause:
            self.gui_buttons["menu"] = self.render_button("button_pause", 40, 40)
        else:
            # todo : there is a bug here
            self.gui_buttons.pop('menu', 'key not found')
            self.gui_buttons['pause'] = self.render_button("button_start", 40, 40)

        # Eng : buttons on the right down corner 
        # Fr :
        self.gui_buttons["inventory"] = self.render_button("button_inventory", DISPLAY_WIDTH - 40, DISPLAY_HEIGHT - 40)
        self.gui_buttons["stats"] = self.render_button("button_character", DISPLAY_WIDTH - 90, DISPLAY_HEIGHT - 40)

        # Eng : quest's button on the left down corner
        # Fr :
        self.gui_buttons["quests"] = self.render_button("button_large", 85, DISPLAY_HEIGHT - 40)
        self.render_text("quests", 85, DISPLAY_HEIGHT - 39, Gui.colors['white'])

    def render_background(self):
        """ Eng : renders a dark green background with random white stars """
        """ Fr : """
        Gui.display.fill(Gui.colors["dark green"])
        for star in self.stars:
            pygame.draw.rect(Gui.display, Gui.colors["white"], star)

    def render_frame(self, frame_type, frame_name):
        # render frame
        self.render_image(f'./assets/frames/{frame_type}.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2))
        if frame_type == 'normal':
            # render close button
            self.gui_buttons[Scene.previous_scene] = self.render_button('button_close', 355, 155)
            # render menu pause title
            self.render_text(frame_name, int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 80))
        if frame_type == 'big':
            # render close button
            self.gui_buttons[Scene.previous_scene] = self.render_button('button_close', 355, 45)
            # render menu pause title
            self.render_text(frame_name, int(DISPLAY_WIDTH/2), 60)

    def render_logo(self, y, big_logo = True):
        """ Eng : renders the two versions of game logo : small & big """
        """ Fr : """
        if big_logo:
            self.render_text("woods", DISPLAY_WIDTH/2 + 7, y + 7, Gui.colors["dark blue"], 80)
            self.render_text("runner", DISPLAY_WIDTH/2 + 7, y + 67, Gui.colors["dark blue"], 80)
            self.render_text("woods", DISPLAY_WIDTH/2, y, Gui.colors["white"], 80)
            self.render_text("runner", DISPLAY_WIDTH/2, y + 60, Gui.colors["white"], 80)
        else:
            self.render_text("woods", DISPLAY_WIDTH/2 + 4, y + 4, Gui.colors["dark blue"], 30)
            self.render_text("runner", DISPLAY_WIDTH/2 + 4, y + 26, Gui.colors["dark blue"], 30)
            self.render_text("woods", DISPLAY_WIDTH/2, y, Gui.colors["white"], 30)
            self.render_text("runner", DISPLAY_WIDTH/2, y + 22, Gui.colors["white"], 30)

    def render_button(self, name, x, y):
        """ Eng : this function draw buttons from the asset/button file and checks hover effect """
        """ Fr : """
        path = f"./assets/buttons/buttons_normal/{name}.png"
        button = self.render_image(path, x, y)
        mx, my = pygame.mouse.get_pos()
        if button.collidepoint(mx, my):
            path = f"./assets/buttons/buttons_pressed/{name}.png"
            button_pressed = self.render_image(path, x, y)
            return button_pressed
        return button
        

    def render_text(self, text, x, y, color = colors['white'], size = 16):
        """ Eng : Draws any text on the scene window and also returns a rectangle object wich have 
        coord attributes and collide methode """
        """ Fr : """
        game_font = pygame.font.Font("./assets/fonts/Minecraft.ttf", size)
        text_surface = game_font.render(text, False, color)
        text_rect = text_surface.get_rect(center = (int(x), int(y)))
        Gui.display.blit(text_surface, text_rect)
        return text_rect

    def render_image(self, path, x, y):
        """ Eng : Renders images and icons on the screen and returns a rect object """
        """ Fr : """
        image = pygame.image.load(path).convert_alpha()
        image_rect = image.get_rect(center = (int(x), int(y)))
        Gui.display.blit(image, image_rect)
        return image_rect

    def render_rect(self, x, y, width, height, color):
        pygame.draw.rect(Gui.display, color, pygame.Rect(int(x), int(y), width, height))


# create a gui
gui = Gui()
# create a player 
player = Entity()

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

def layout_paused(template):
    def render_gui():
        # render big centered logo
        gui.render_logo(30, False)
        # render UI buttons
        gui.render_ui_buttons(pause=True)
        template()
    return render_gui

    

################################# Story Template #################################
@layout
def before_game_template():
    #story text
    gui.render_text('Hi there, this is a story game.', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2- 80), size = 18)
    gui.render_text('are you sure you wanna play its', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2- 58), size = 18)
    gui.render_text('scary out there !', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2- 36), size = 18)
    # render left direction buttons
    game.ux_scenes['before game'].buttons['game'] = gui.render_button('button_large', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 30))
    gui.render_text('Play', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 30))


################################# Menu Template #################################
@layout_paused
def menu_template():
    # render frame 
    gui.render_frame('normal', 'pause')
    # render menu options
    game.ux_scenes['menu'].buttons["home"] = gui.render_text('New Game', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 30), size = 30)
    game.ux_scenes['menu'].buttons["exit"] = gui.render_text('Exit Game', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 10), size = 30)
    game.ux_scenes['menu'].buttons["credit"] = gui.render_text('Credit', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 50), size = 30)
    

################################# Monster Fight Template #################################
@layout
def fight_template():
    # render frame
    gui.render_frame('normal', 'fight')

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
@layout_paused
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
    game.ux_scenes['home'].buttons["before game"] = gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 160) 

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
@layout_paused
def quests_template():
    # render frame
    gui.render_frame('normal', 'quests')
    # render how to play content
    gui.render_text('current quest: Kill the boss', int(DISPLAY_WIDTH/2), 250)

################################# Quests Template #################################
def store_template():
    # render frame
    gui.render_frame('big', 'store')
    # render how to play content
    gui.render_text('this is the store', int(DISPLAY_WIDTH/2), 250)


################################# Game Story Template  (important) #################################
@layout
def game_template():
    pass












class Game:
    def __init__(self):
        # constructing user expercience scenes 
        self.ux_scenes = {
            'home' : Scene('home', home_template),
            'menu' : Scene('menu', menu_template),
            'before game' : Scene('before game', before_game_template),
            'inventory' : Scene('inventory', inventory_template),
            'credit' : Scene('credit', credit_template),
            'how to play' : Scene('how to play', howtoplay_template),
            'stats' : Scene('stats', stats_template),
            'quests' : Scene('quests', quests_template),
            'store' : Scene('store', store_template)
        }

        # constructing mean game scenes 
        self.story_scenes = [[Scene(str(y) + "-" + str(x), game_template) for y in range(10)] for x in range(10)]
        self.i, self.j = 0, 0

    def run(self):
        self.ux_scenes['home'].run_scene()  


game = Game()
game.run()
