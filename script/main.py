""" This game is made by Youness ID BAKKASSE; https://github.com/younessidbakkasse/
its a school project to initiat with Python programming 
for more informations and licence please check README file attached to the folder."""

# Importing modules: pygame is a module that allows us to draw on screen
import pygame, sys

# Colors
colors = {
    "black" : (15, 15, 15),
    "white" : (245, 245, 245),
    "yellow": (249, 200, 51),
    "brown" : (49, 45, 46),
    "orange" : (238, 117, 57)
}

DISPLAY_HEIGHT = 500
DISPLAY_WIDTH = 400

class Scene():
    # Set up the game display
    pygame.init()
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()

    def __init__(self, scene_name, previous_scene):
        """ Constructor method runs when I creat an object using the Scene class """
        self.running = True 
        self.scene_name, self.previous_scene = scene_name, previous_scene 
        self.buttons = {}

    def run_scene(self):
        """ scene's main loop : basicly each scene has its own loop """
        while self.running:
            Scene.display.fill(colors["brown"])
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
                    self.transition(controle.scenes)
    
    def transition(self, scenes):
        """ One hell of an importante method it checks if mouse points to a text or 
        button (rect) and also allows scene transitions from self to another depending 
        on the button's name"""
        self.mx, self.my = pygame.mouse.get_pos()
        for button_name, button in self.buttons.items():   
            if button.collidepoint((self.mx, self.my)):
                for scene_key, scene in scenes.items():
                    if scene_key == button_name:
                        print(self.previous_scene, button_name)
                        scene.run_scene()

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
        image = pygame.image.load(path)
        image_rect = image.get_rect(center = (int(x), int(y)))
        Scene.display.blit(image, image_rect)
        return image_rect

class MainMenu(Scene):
    """ This is a sub class from scene base class """
    def __init__(self, scene_name, previous_scene, destination_scene, music_icon_path):
        super().__init__(scene_name, previous_scene)
        # The menu scene have an a music icon
        self.music_icon_path = music_icon_path
        
    def render_template(self):
        """ This is the template function for scene with similar template """
        # Logo
        self.render_text("woods", int(DISPLAY_WIDTH/2), 55, colors["yellow"], 32)
        self.render_text("runner", int(DISPLAY_WIDTH/2), 100, colors["yellow"], 80)

        # Menu items
        self.buttons["game_scene"] = self.render_text("New game", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2), colors["orange"], 40)
        self.buttons["option_menu"] = self.render_text("Options", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2) + 50, colors["orange"], 40)        
        self.buttons["credit_menu"] = self.render_text("Credit", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2) + 100, colors["orange"], 40)

        # Music on/off icon
        self.buttons[self.previous_scene] = self.render_image(self.music_icon_path, int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT - 50))       

class MenuDescription(Scene):
    """ This is a sub class from scene base class and it refers to menu definitions """
    def __init__(self, scene_name, previous_scene, menu_title, ):
        super().__init__(scene_name, previous_scene)
        self.menu_title = menu_title

    def render_template(self):
        """ This is the template function for scene with similar template """
        # menu title
        self.render_text(self.menu_title, int(DISPLAY_WIDTH/2), 60, colors["orange"], 40)        

        # Music on/off icon
        self.buttons[self.previous_scene] = self.render_image("./assets/icons/back_icon.png", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT - 50))       

class Controle: 
    def __init__(self):
        self.scenes = {}
        
        self.scenes["music_on"] = Menu("music_on", "music_off", "./assets/icons/music_on_icon.png")
        self.scenes["music_off"] = Menu("music_off", "music_on", "./assets/icons/music_off_icon.png")
        self.scenes["credit_menu"] = MenuDescription("credit_menu", "Credit")                 
   
    def run_game(self):
        self.scenes["music_on"].run_scene()

controle = Controle()
controle.run_game()

    
       



