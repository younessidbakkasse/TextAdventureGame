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

class scene:
    def __init__(self):
        """ Set up the game display """
        self.running, self.click = True, False

    def gameLoop(self, function):
        """ scene main loop : basicly each scene has its own loop """
        while self.running:
            game.display.fill(color["brown"])
            self.eventLoop()
            pygame.display.update()
            game.clock.tick(60)

    def eventLoop(self):
        """ This function collects keyboard and mouse clicks from the user """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def renderText(self, text, x, y, color,size = 20):
        """ Draws any text on the scene window """
        gameFont = pygame.font.Font("Minecraft.ttf", size)
        textSurface = gameFont.render(text, False, color)
        textRect = textSurface.get_rect(center = (int(x), int(y)))
        game.display.blit(textSurface, textRect)

    def renderImage(self, path, x, y):
        """ Renders images on the screen """
        image = pygame.image.load(path)
        imageRect = image.get_rect(center = (int(x), int(y)))
        game.display.blit(image, imageRect)

class mainMenu(scene):
    """ This is a sub class from scene base class ; sceneMenu = a variant of scene with a menu """
    def __init__(self):
        super().__init__()
        self.gameLoop(self.render())

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


class Menu(scene):
    """ This is a sub class from scene base class ; sceneMenu = a variant of scene with a menu """
    def __init__(self, name):
        super().__init__()
        self.name = name

    def gameLoop(self):
        """ scene main loop : basicly each scene has its own loop """
        while self.running:
            game.display.fill(color["brown"])
            self.renderText(self.name, 200, 50, color["orange"], 40)
            self.eventLoop()
            pygame.display.update()
            game.clock.tick(60)

class Game:
    displayWidth = 400
    displayHeight = 500
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((Game.displayWidth, Game.displayHeight))

    def run(self):
        self.mainMenu = mainMenu()


game = Game()
game.run()

    
       



