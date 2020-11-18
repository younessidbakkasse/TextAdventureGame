""" This game is made by Youness ID BAKKASSE; https://github.com/younessidbakkasse/
its a school project to initiat with Python programming 
for more informations and licence please check README file attached to the folder."""

# Importing modules: pygame is a module that allows us to draw on screen
import pygame, sys, random

# Colors
colors = {
    "dark green" : (14, 43, 35),
    "dark blue" : (2, 17, 29),
    "white" : (251, 251, 251),
    "green": (18, 168, 113),
    "red" : (255, 0, 69),
    "yellow" : (250, 200, 50)
}

DISPLAY_HEIGHT = 500
DISPLAY_WIDTH = 400

class Scene:
    # Set up the game display
    pygame.init()
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()

    def __init__(self, scene_name):
        """ Constructor method runs when I creat an object using the Scene class """
        self.running = True 
        self.scene_name = scene_name
        self.buttons = {}
        self.mx, self.my = 0, 0

    def render_template(self):
        pass

    def run_scene(self):
        """ scene's main loop : basicly each scene has its own loop """
        while self.running:  
            gui.render_background()
            self.render_template()
            self.get_events()
            pygame.display.update()
            Scene.clock.tick(60)

    def get_events(self):
        """ This function collects Mouse clicks from the user """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button: 
                    self.mx, self.my = pygame.mouse.get_pos()
                    self.transition(controle.scenes)
    
    def transition(self, scenes):
        """ One hell of an importante method it checks if mouse points to a text or 
        button (rect) and also allows scene transitions from self to another depending 
        on the button's name"""
        for button_name, button in self.buttons.items():   
            if button.collidepoint((self.mx, self.my)):
                for scene_key, scene in scenes.items():
                    if scene_key == button_name:
                        controle.previous_scene = self.scene_name
                        # This may cause bugs in futur if it didn't ur a lucky mothafucka
                        self.buttons.popitem()
                        scene.run_scene()

class Gui:
    def __init__(self):
        self.stars = [pygame.Rect(random.randint(0, DISPLAY_WIDTH), random.randint(0, DISPLAY_HEIGHT), 3, 3) for i in range(30)]

    def render_background(self):
        Scene.display.fill(colors["dark green"])
        for star in self.stars:
            pygame.draw.rect(Scene.display, colors["white"], star)

    def render_logo(self, y, big_logo = True):
        if big_logo:
            self.render_text("woods", DISPLAY_WIDTH/2 + 6, y + 6, colors["dark blue"], 80)
            self.render_text("runner", DISPLAY_WIDTH/2 + 6, y + 66, colors["dark blue"], 80)
            self.render_text("woods", DISPLAY_WIDTH/2, y, colors["white"], 80)
            self.render_text("runner", DISPLAY_WIDTH/2, y + 60, colors["white"], 80)
        else:
            self.render_text("woods", DISPLAY_WIDTH/2 + 4, y + 4, colors["dark blue"], 30)
            self.render_text("runner", DISPLAY_WIDTH/2 + 4, y + 24, colors["dark blue"], 30)
            self.render_text("woods", DISPLAY_WIDTH/2, y, colors["white"], 30)
            self.render_text("runner", DISPLAY_WIDTH/2, y + 20, colors["white"], 30)

    def render_button(self, name, x, y):
        path = f"./assets/buttons/{name}.png"
        button = self.render_image(path, x, y)
        mx, my = pygame.mouse.get_pos()
        if button.collidepoint((mx, my)):
            path = f"./assets/buttons/{name}_pressed.png"
            button_pressed = self.render_image(path, x, y)
            return button_pressed


    def render_text(self, text, x, y, color, size = 20):
        """ Draws any text on the scene window and also returns a rectangle object wich have 
        coord attributes and collide methode """
        game_font = pygame.font.Font("./assets/fonts/Minecraft.ttf", size)
        text_surface = game_font.render(text, False, color)
        text_rect = text_surface.get_rect(center = (int(x), int(y)))
        Scene.display.blit(text_surface, text_rect)
        return text_rect

    def render_image(self, path, x, y):
        """ Renders images and icons on the screen and returns a rect object """
        image = pygame.image.load(path).convert_alpha()
        image_rect = image.get_rect(center = (int(x), int(y)))
        Scene.display.blit(image, image_rect)
        return image_rect

class Start(Scene):
    """ This is a sub class from scene base class """
    def __init__(self, scene_name):
        super().__init__(scene_name)
        
    def render_template(self):
        # Logo
        gui.render_logo(130)
        # start game button
        gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 160)       

class Controle: 
    def __init__(self):
        self.previous_scene = None
        self.scenes = {}
        
        self.scenes["start"] = Start("start")

    def run_game(self):
        self.scenes["start"].run_scene()
        

gui = Gui()
controle = Controle()
controle.run_game()

    
       



