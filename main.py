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

class Scene:
    def __init__(self):
        """ Set up the game display """
        self.running, self.click = True, False

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
        game.display.blit(text_surface, text_rect)

    def render_image(self, path, x, y):
        """ Renders images on the screen """
        image = pygame.image.load(path)
        image_rect = image.get_rect(center = (int(x), int(y)))
        game.display.blit(image, image_rect)

class mainMenu(Scene):
    """ This is a sub class from scene base class ; sceneMenu = a variant of scene with a menu """
    def __init__(self):
        super().__init__()
        self.gameLoop()

    def gameloop(self):
        """ scene main loop : basicly each scene has its own loop """
        while self.running:
            game.display.fill(color["brown"])
            self.render()
            self.get_events()
            pygame.display.update()
            game.clock.tick(60)

    def render(self):
        # logo
        self.renderText("woods", 200, 55, color["yellow"], 32)
        self.renderText("runner", 200, 100, color["yellow"], 80)

        # menu items
        self.renderText("New game", 200, int(Game.displayHeight/2), color["orange"], 40)
        self.renderText("Options", 200, int(Game.displayHeight/2) + 50, color["orange"], 40)        
        self.renderText("Credit", 200, int(Game.displayHeight/2) + 100, color["orange"], 40)

        # render icon
        self.renderImage("Sound Icon.png", int(Game.displayWidth/2), int(Game.displayHeight - 40))



    
       



