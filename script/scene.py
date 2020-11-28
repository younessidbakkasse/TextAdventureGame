from entities import Entity
import pygame, random, sys

# Eng : global variables
# Fr : 
DISPLAY_HEIGHT = 500
DISPLAY_WIDTH = 400

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
    
    # Eng : constructed a dict object for gui common button
    # Fr :
    gui_buttons = dict()

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

    def render_ui_buttons(self):
        """ Eng : renders the same user interface buttons acroos all the scenes and stores them on list"""
        """ Fr : """

        # Eng : buttons on the right side
        # Fr :
        self.gui_buttons["scene1"] = self.render_button("button_music_on", DISPLAY_WIDTH - 40, 40)
        self.gui_buttons["scene2"] = self.render_button("button_help", DISPLAY_WIDTH - 90, 40)

        # Eng : buttons on the left side
        # Fr :
        self.gui_buttons["scene3"] = self.render_button("button_return", 40, 40)
        self.gui_buttons["scene4"] = self.render_button("button_pause", 90, 40)

        # Eng : buttons on the right down corner 
        # Fr :
        self.gui_buttons["scene5"] = self.render_button("button_inventory", DISPLAY_WIDTH - 40, DISPLAY_HEIGHT - 40)
        self.gui_buttons["scene6"] = self.render_button("button_character", DISPLAY_WIDTH - 90, DISPLAY_HEIGHT - 40)

        # Eng : quest's button on the left down corner
        # Fr :
        self.gui_buttons["scene7"] = self.render_button("button_large", 85, DISPLAY_HEIGHT - 40)
        self.render_text("quests", 85, DISPLAY_HEIGHT - 39, Gui.colors['white'])

    def render_background(self):
        """ Eng : renders a dark green background with random white stars """
        """ Fr : """
        Gui.display.fill(Gui.colors["dark green"])
        for star in self.stars:
            pygame.draw.rect(Gui.display, Gui.colors["white"], star)

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
        if button.collidepoint((mx, my)):
            path = f"./assets/buttons/buttons_pressed/{name}.png"
            button_pressed = self.render_image(path, x, y)
            return button_pressed

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

# create a gui
gui = Gui()







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
                    # self.transition(Scene.scenes)
                    pass
    
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




##########################
#CREATING FONCTIONS AS TEMPLATES
###########################

def story_template():
    def template():
        # render big centered logo
        gui.render_logo(30, False)
        # render UI buttons
        gui.render_ui_buttons()
        #story text
        gui.render_text('Chose a direction ?', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2- 80), size = 20)
        # render left direction buttons
        game.story_scenes[0][0].buttons['left'] = gui.render_button('button_large', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 30))
        gui.render_text('Left', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 30))

        # render left direction buttons
        game.story_scenes[0][0].buttons['right'] = gui.render_button('button_large', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 80))
        gui.render_text('Right', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 80))

    return template

def home_template():
    def template():
        # render big centered logo
        gui.render_logo(150, True)
        # start game button
        game.ux_scenes['home'].buttons["main_game"] = gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 160) 
    return template

def menu_template():
    def template():
        # render big centered logo
        gui.render_logo(150, True)
        # start game button
        game.ux_scenes['home'].buttons["main_game"] = gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 160) 
    return template

def fight_template():
    def template():
        # render big centered logo
        gui.render_logo(150, True)
        # start game button
        game.ux_scenes['home'].buttons["main_game"] = gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 160) 
    return template

def inventory_template():
    def template():
        # render big centered logo
        gui.render_logo(150, True)
        # start game button
        game.ux_scenes['home'].buttons["main_game"] = gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 160) 
    return template

def credit_template():
    def template():
        # render big centered logo
        gui.render_logo(150, True)
        # start game button
        game.ux_scenes['home'].buttons["main_game"] = gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 160) 
    return template

def howtoplay_template():
    def template():
        # render big centered logo
        gui.render_logo(150, True)
        # start game button
        game.ux_scenes['home'].buttons["main_game"] = gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 160) 
    return template

def stats_template():
    def template():
        # render big centered logo
        gui.render_logo(150, True)
        # start game button
        game.ux_scenes['home'].buttons["main_game"] = gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 160) 
    return template











class Game:
    def __init__(self):
        # constructing user expercience scenes 
        self.ux_scenes = {
            'home' : Scene('home', home_template()),
            'menu' : Scene('menu', menu_template()),
            'fight' : Scene('fight', fight_template()),
            'inventory' : Scene('inventory', inventory_template()),
            'credit' : Scene('credit', credit_template()),
            'how to play' : Scene('how to play', howtoplay_template()),
            'stats' : Scene('stats', stats_template())
        }

        # constructing mean game scenes 
        self.story_scenes = [[Scene(str(y) + "-" + str(x), story_template()) for y in range(1)] for x in range(1)]
        self.i, self.j = 0, 0

    def run(self):
        # self.ux_scenes['credit'].run_scene()
        self.story_scenes[0][0].run_scene()        

    def deploy_scenes(self):
        pass

game = Game()
game.run()

