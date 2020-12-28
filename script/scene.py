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
        "grey" : (40, 40, 60),
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
            self.gui_buttons["music on"] = Button('button_music_on', DISPLAY_WIDTH - 45, 50, 'music on')
        else:
            self.gui_buttons["music off"] = Button('button_music_off', DISPLAY_WIDTH - 45, 50, 'music off')
        self.gui_buttons["how to play"] = Button('button_help', DISPLAY_WIDTH - 110, 50, 'how to play')

        # Eng : buttons on the left side
        # Fr :
        self.gui_buttons["store"] = Button("button_cart", 110, 50, 'store')
        if pause: 
            self.gui_buttons["start"] = Button("button_start", 45, 50, None)
        else:
            self.gui_buttons["menu"] = Button("button_pause", 45, 50, "menu")

        # Eng : buttons on the right down corner 
        # Fr :
        self.gui_buttons["inventory"] = Button("button_inventory", DISPLAY_WIDTH - 45, DISPLAY_HEIGHT - 50, 'inventory')
        self.gui_buttons["stats"] = Button("button_character", DISPLAY_WIDTH - 110, DISPLAY_HEIGHT - 50, 'stats')

        # Eng : quest's button on the left down corner
        # Fr :
        self.gui_buttons["quests"] = Button("button_quests", 85, DISPLAY_HEIGHT - 50, 'quests')
        self.render_text("Quests", 85, DISPLAY_HEIGHT - 50, Gui.colors['white'], size=20, Regular=True)

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
        """ Eng :  """
        """ Fr : """
        pygame.draw.rect(Gui.display, color, pygame.Rect(int(x), int(y), width, height))

    def render_circle(self, x, y, radius, color):
        """ Eng :  """
        """ Fr : """
        pygame.draw.circle(Gui.display, color, (int(x), int(y)), radius)

    def render_gui(self, pause = False):
        """ Eng :  """
        """ Fr : """
        gui.render_logo(40, False)
        gui.render_ui_buttons(pause)
        
    
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
    previous_story_scene = None
    # Eng : game music 
    # Fr :
    sound = True
    
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
                    self.mx, self.my = pygame.mouse.get_pos()
                    self.transition()

    def transition(self):
        """ Eng : One hell of an importante method it checks if mouse points to a text or 
        button (rect) and also allows scene transitions from self to another depending 
        on the button's name"""
        """ Fr : """
        scene_key = self.get_current_scene_key()
        is_scene_type_game = isinstance(manager.game.scenes[scene_key], StoryScene)
        buttons = gui.gui_buttons | self.buttons
        if not is_scene_type_game:
            buttons = self.buttons
        for button in buttons.values():   
            if button.rect.collidepoint((self.mx, self.my)):
                if is_scene_type_game:
                    # Change sound button from on to off
                    if button.destination == 'music on':
                        Scene.sound = False
                        del gui.gui_buttons['music on']
                        break
                    elif button.destination == 'music off':
                        Scene.sound = True
                        del gui.gui_buttons['music off']
                        break
                    # check for loot buttons
                    if 'loot' in button.category:
                        player.add_item_inventory(button.loot)
                    elif 'navigate' in button.category:
                        button.onclick()

                elif button.destination == 'exit':
                        pygame.quit()
                        sys.exit()
                for scene in manager.game.scenes.values():
                    if scene.scene_name == button.destination:
                        if is_scene_type_game:
                            Scene.previous_story_scene = scene_key
                        Scene.previous_scene = self.scene_name
                        scene.run_scene()                                

    def get_current_scene_key(self):
        """ Eng : This function return current scene key in game manager dict """
        """ Fr : """
        for key, scene in manager.game.scenes.items():
            if scene.scene_name == self.scene_name:
                return key


class StoryScene(Scene):
    def __init__(self, scene_name, choices, story_text, template_closure = gui.render_gui):
        """ Eng : """
        """ Fr : """
        super().__init__(scene_name, template_closure)
        self.story_text = story_text
        self.choices = choices
        self.last_line = 0

    def render_story_text(self):
        """ Eng : """
        """ Fr : """
        for i, line in enumerate(self.process_story_text()):
            gui.render_text(line, int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 130 + i * 26), size = 20, Regular=True)
            self.last_line = int(DISPLAY_HEIGHT/2 - 120 + i * 26) + 80

    def render_previous_story(self):
        if self.scene_name != 'Pregame':
            for i, line in enumerate(manager.game.scenes[Scene.previous_story_scene].process_story_text()):
                gui.render_text(line, int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 180 + i * 15), size = 14, Regular=True, color=Gui.colors['grey'])
        
    def render_choices(self):
        """ Eng : """
        """ Fr : """
        for i, choice in enumerate(self.choices):
            if len(choice[0]) < 10:
                self.buttons['choice'+str(i)] = Button('button_small', int(DISPLAY_WIDTH/2), self.last_line + i * 6, choice[1], category=choice[2])
            elif len(choice[0]) < 20:
                self.buttons['choice'+str(i)] = Button('button_large', int(DISPLAY_WIDTH/2), self.last_line + i * 60, choice[1], category=choice[2])
            else:
                self.buttons['choice'+str(i)] = Button('button_really_large', int(DISPLAY_WIDTH/2), self.last_line + i * 60, choice[1], category=choice[2])
            gui.render_text(choice[0], int(DISPLAY_WIDTH/2), self.last_line + i * 60, Regular=True, size=20)
    
    def render_template(self):
        """ Eng : """
        """ Fr : """
        self.template()
        self.render_previous_story()
        self.render_story_text()
        self.render_choices()

    def process_story_text(self):
        """ Eng : """
        """ Fr : """
        processed_text, line = '', ''
        words = self.story_text.split()
        for i, word in enumerate(words):
            processed_text += word + ' '
            line += word + ' '
            if (i % 7 == 0 or i % 6 == 0 or i % 5 == 0) and len(line) > 26 and len(line) < 40:
                processed_text += '\n'
                line= ''
            elif(i % 9 == 0 or i % 4 == 0) and len(line) > 30:
                processed_text += '\n'
                line= ''
        return processed_text.splitlines()


class Button():
    def __init__(self, path, x, y, destination, category = 'normal'):
        self.path = path
        self.destination = destination
        self.category = category

        if self.category == 'text':
            self.rect = gui.render_text(path, x, y, size = 35, Regular=True)
        elif 'loot' in self.category:
            self.loot = self.category[5:]
            self.rect = gui.render_button(path, x, y)
        elif 'fight' in self.category:
            self.monster = self.category[6:]
            self.rect = gui.render_button(path, x, y)
        elif 'navigate' in self.category:
            self.onclick = None
            self.rect = gui.render_button(path, x, y)
        else:
            self.rect = gui.render_button(path, x, y)


        def navigate_right(self):
            pass

    
        