from entities import player
import manager
import sys, pygame, random

# Eng : global variables
# Fr : 
DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 450

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
    pygame.display.set_caption("Dead Island", "favicon")

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
        "dark blue" : (3, 15, 38),
        "white" : (253, 253, 253),
        "green": (18, 168, 113),
        "red" : (255, 0, 69),
        "yellow" : (250, 200, 50),
        "grey" : (20, 55, 45),
        "transparent" : (0, 44, 74, 150)
    }
    
    def __init__(self):
        self.gui_buttons = {}

    def render_ui_buttons(self, pause):
        """ Eng : renders the same user interface buttons acroos all the scenes and stores them on list"""
        """ Fr : """
        # Eng : buttons on the right side
        # Fr :
        if Scene.sound:
            self.gui_buttons["music on"] = self.render_button('button_music_on', DISPLAY_WIDTH - 45, 50)
        else:
            self.gui_buttons["music on"] = self.render_button('button_music_off', DISPLAY_WIDTH - 45, 50)
        self.gui_buttons["how to play"] = self.render_button("button_help", DISPLAY_WIDTH - 110, 50)

        # Eng : buttons on the left side
        # Fr :
        self.gui_buttons["store"] = self.render_button("button_cart", 110, 50)
        if pause: 
            self.render_button("button_start", 45, 50)
        else:
            self.gui_buttons["menu"] = self.render_button("button_pause", 45, 50)

        # Eng : buttons on the right down corner 
        # Fr :
        self.gui_buttons["inventory"] = self.render_button("button_inventory", DISPLAY_WIDTH - 45, DISPLAY_HEIGHT - 50)
        self.gui_buttons["stats"] = self.render_button("button_character", DISPLAY_WIDTH - 110, DISPLAY_HEIGHT - 50)

        # Eng : quest's button on the left down corner
        # Fr :
        self.gui_buttons["quests"] = self.render_button("button_quests", 85, DISPLAY_HEIGHT - 50)
        self.render_text("quests", 85, DISPLAY_HEIGHT - 50, Gui.colors['white'], size=18)

    def render_background(self):
        """ Eng : renders a dark green background with random white stars """
        """ Fr : """
        Gui.display.fill(Gui.colors["dark blue"])
        for star in self.stars:
            pygame.draw.rect(Gui.display, Gui.colors["white"], star)
    
    def render_transparent_background(self):
        """ Eng : renders a dark green transparent background """
        """ Fr : """
        s = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT), pygame.SRCALPHA)   
        s.fill(Gui.colors['transparent'])                       
        Gui.display.blit(s, (0,0))

    def render_frame(self, frame_type, frame_name):
        if frame_type == 'normal':
            # render frame
            self.render_image(f'./assets/frames/{frame_type}.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2))
            # render menu pause title
            self.render_text(frame_name, int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 110))
        if frame_type == 'big':
            # render frame
            self.render_image(f'./assets/frames/{frame_type}.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 20))
            # render menu pause title
            self.render_text(frame_name, int(DISPLAY_WIDTH/2), 160)
        if frame_type == 'huge':
            # render frame
            self.render_image(f'./assets/frames/{frame_type}.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 10))
            # render menu pause title
            self.render_text(frame_name, int(DISPLAY_WIDTH/2), 77)

    def render_logo(self, y, big_logo = True):
        """ Eng : renders the two versions of game logo : small & big """
        """ Fr : """
        if big_logo:
            self.render_text("DEAD", DISPLAY_WIDTH/2, y - 10, Gui.colors["dark green"], 115)
            self.render_text("ISLAND", DISPLAY_WIDTH/2, y + 70, Gui.colors["dark green"], 115)
            self.render_text("DEAD", DISPLAY_WIDTH/2, y, Gui.colors["white"], 110)
            self.render_text("ISLAND", DISPLAY_WIDTH/2, y + 80, Gui.colors["white"], 110)
        else:
            self.render_text("DEAD", DISPLAY_WIDTH/2, y - 4, Gui.colors["dark green"], 40)
            self.render_text("ISLAND", DISPLAY_WIDTH/2, y + 26, Gui.colors["dark green"], 40)
            self.render_text("DEAD", DISPLAY_WIDTH/2, y, Gui.colors["white"], 40)
            self.render_text("ISLAND", DISPLAY_WIDTH/2, y + 30, Gui.colors["white"], 40)

    def render_button(self, name, x, y):
        """ Eng : this function draw buttons from the asset/button file and checks hover effect """
        """ Fr : """
        path = f"./assets/buttons/buttons_normal/{name}.png"
        button = self.render_image(path, x, y + 3)
        mx, my = pygame.mouse.get_pos()
        if button.collidepoint(mx, my):
            path = f"./assets/buttons/buttons_pressed/{name}.png"
            button_pressed = self.render_image(path, x, y)
            return button_pressed
        return button
        

    def render_text(self, text, x, y, color = colors['white'], size = 16, Regular = False):
        """ Eng : Draws any text on the scene window and also returns a rectangle object wich have 
        coord attributes and collide methode """
        """ Fr : """
        game_font = pygame.font.Font("./assets/fonts/Minecraft.ttf", size)
        if Regular:
            game_font = pygame.font.Font("./assets/fonts/MinecraftRegular.otf", size)
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

    def render_gui(self, pause = False):
        gui.render_logo(40, False)
        gui.render_ui_buttons(pause)

    def render_char(self):
        pass
    
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

    # Eng : game music 
    # Fr :
    sound = True


    def __init__(self, scene_name, template_closure, scene_type = 'game'):
        """ Eng: Constructor method runs every time I create a new scene or page. """
        """ Fr: Constructor method runs every time I create a new scene or page. """
        self.template = template_closure
        self.scene_name = scene_name
        self.scene_type = scene_type
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
                    self.transition(manager.game.scenes)
    
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
                    elif button_name == 'exit':
                        pygame.quit()
                        sys.exit()
        
                    
        # this is to check for gui buttons
        for button_name, button in list(gui.gui_buttons.items()):
            self.mx, self.my = pygame.mouse.get_pos()   
            if button != None and button.collidepoint((self.mx, self.my)):
                if button_name == 'music on':
                    print('There should not be sound')
                    Scene.sound = False
                    gui.gui_buttons.pop('music on')
                elif button_name == 'music off':
                    print('There should be sound')
                    Scene.sound = True
                    gui.gui_buttons.pop('music off')
                for scene_key, scene in scenes.items():
                    if scene_key == button_name:
                        if self.scene_type == 'game':
                            Scene.previous_scene = self.scene_name
                            # This may cause bugs in futur if it didn't ur a lucky mothafucka
                            scene.run_scene()
        print(len(gui.gui_buttons))

class StoryScene(Scene):
    def __init__(self, scene_name, choices, story_text, template_closure = gui.render_gui):
        """ Eng : """
        """ Fr : """
        super().__init__(scene_name, template_closure)
        self.story_text = story_text
        self.choices = choices

    def render_story_text(self):
        """ Eng : """
        """ Fr : """
        for i, line in enumerate(self.story_text):
            gui.render_text(line, int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 80 - i * 20), size = 18)
        
    def render_choices(self):
        """ Eng : """
        """ Fr : """
        for i, choice in enumerate(self.choices):
            self.buttons[choice] = gui.render_button('button_xl', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + i * 45))
            gui.render_text(choice, int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + i * 45))
    
    def render_template(self):
        """ Eng : """
        """ Fr : """
        self.template()
        self.render_story_text()
        self.render_choices()





