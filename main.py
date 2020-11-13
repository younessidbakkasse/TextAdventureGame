""" This game is made by Youness ID BAKKASSE; https://github.com/younessidbakkasse/
its a school project to initiat with Python programming 
for more informations and licence please check README file attached to the folder."""

# Importing modules: pygame is a module that allows us to draw on screen
import pygame, sys

# Colors
color = {
    "black" : (15, 15, 15),
    "white" : (245, 245, 245),
    "yellow": (249, 200, 51),
    "brown" : (49, 45, 46),
    "orange" : (238, 117, 57)
}

DISPLAY_HEIGHT = 500
DISPLAY_WIDTH = 400


class Scene:
    def __init__(self):
        """ Set up the game display """
        self.running, self.click = True, False
        pygame.init()
        self.display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()

    def get_events(self):
        """ This function collects keyboard and mouse clicks from the user """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def render_text(self, text, x, y, color, size = 20):
        """ Draws any text on the scene window """
        game_font = pygame.font.Font("Minecraft.ttf", size)
        text_surface = game_font.render(text, False, color)
        text_rect = text_surface.get_rect(center = (int(x), int(y)))
        self.display.blit(text_surface, text_rect)

    def render_image(self, path, x, y):
        """ Renders images on the screen """
        image = pygame.image.load(path)
        image_rect = image.get_rect(center = (int(x), int(y)))
        self.display.blit(image, image_rect)

class Menu(Scene):
    """ This is a sub class from scene base class ; sceneMenu = a variant of scene with a menu """
    def __init__(self):
        super().__init__()

    def run_scene(self):
        """ scene main loop : basicly each scene has its own loop """
        while self.running:
            self.display.fill(color["brown"])
            self.render()
            self.get_events()
            pygame.display.update()
            self.clock.tick(60)

    def render(self):
        # logo
        self.render_text("woods", 200, 55, color["yellow"], 32)
        self.render_text("runner", 200, 100, color["yellow"], 80)

        # menu items
        self.render_text("New game", 200, int(DISPLAY_HEIGHT/2), color["orange"], 40)
        self.render_text("Options", 200, int(DISPLAY_HEIGHT/2) + 50, color["orange"], 40)        
        self.render_text("Credit", 200, int(DISPLAY_HEIGHT/2) + 100, color["orange"], 40)

        # render icon
        self.render_image("Sound Icon.png", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT - 40))

menu = Menu()
menu.run_scene()


    
       



