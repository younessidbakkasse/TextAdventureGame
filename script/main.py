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
    pygame.init()
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()

    def __init__(self):
        """ Set up the game display """
        self.running= True 
        self.buttons = {}

    def run_scene(self):
        """ scene main loop : basicly each scene has its own loop """
        while self.running:
            Scene.display.fill(colors["brown"])
            self.render_template()
            self.get_events()
            pygame.display.update()
            Scene.clock.tick(60)

    def get_events(self):
        """ This function collects keyboard and mouse clicks from the user """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button: 
                    self.transition(controle.scenes)
    
    def transition(self, scenes):
        """ Checks if mouse points to a text or button (rect) """
        self.mx, self.my = pygame.mouse.get_pos()
        for button_name, button in self.buttons.items():
            if button.collidepoint((self.mx, self.my)):
                for scene_name, scene in scenes.items():
                    if scene_name != button_name:
                        scene.run_scene()


    def render_text(self, text, x, y, color, size = 20):
        """ Draws any text on the scene window """
        game_font = pygame.font.Font("./assets/fonts/Minecraft.ttf", size)
        text_surface = game_font.render(text, False, color)
        text_rect = text_surface.get_rect(center = (int(x), int(y)))
        Scene.display.blit(text_surface, text_rect)
        return text_rect

    def render_image(self, path, x, y):
        """ Renders images on the screen """
        image = pygame.image.load(path)
        image_rect = image.get_rect(center = (int(x), int(y)))
        Scene.display.blit(image, image_rect)
        return image_rect



class Menu(Scene):
    """ This is a sub class from scene base class ; sceneMenu = a variant of scene with a menu """
    def __init__(self, name, path):
        super().__init__()
        self.icon = (name, path)
        
    def render_template(self):
        """ This is the template function for scene with similar template """
        # logo
        self.render_text("woods", int(DISPLAY_WIDTH/2), 55, colors["yellow"], 32)
        self.render_text("runner", int(DISPLAY_WIDTH/2), 100, colors["yellow"], 80)

        # menu items
        self.buttons["game_scene"] = self.render_text("New game", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2), colors["orange"], 40)
        self.buttons["option_menu"] = self.render_text("Options", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2) + 50, colors["orange"], 40)        
        self.buttons["credit_menu"] = self.render_text("Credit", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2) + 100, colors["orange"], 40)

        # render sound icon
        self.buttons[self.icon[0]] = self.render_image(self.icon[1], int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT - 50))       

class Controle: 
    def __init__(self):
        self.scenes = {}
        self.scenes["music_on"] = Menu("music_on", "./assets/icons/music_on_icon.png")
        self.scenes["music_off"] = Menu("music_off", "./assets/icons/music_off_icon.png")

        # self.scenes["option_menu_description"] = Description("Options")                 
            
    def run_game(self):
        self.scenes["music_off"].run_scene()

    

controle = Controle()
controle.run_game()
controle.scenes["music_on"].transition("music_off")


    
       



