""" This game is made by Youness ID BAKKASSE; https://github.com/younessidbakkasse/
its a school project to initiat with Python programming 
for more informations and licence please check README file attached to the folder."""

# Importing modules: pygame is a module that allows us to draw on screen
import pygame, sys

# Game set up
pygame.init()
clock = pygame.time.Clock()

# Colors
color = {
    "black" : (15, 15, 15),
    "white" : (245, 245, 245),
    "yellow": (249, 200, 51),
    "brown" : (49, 45, 46),
    "orange" : (238, 117, 57)
}

class scene:
    displayWidth = 400
    displayHeight = 500
    display = pygame.display.set_mode((displayWidth, displayHeight))

    def __init__(self):
        """ Set up the game display """
        self.running, self.click = True, False

    def gameLoop(self):
        """ scene main loop : basicly each scene has its own loop """
        while self.running:
            scene.display.fill(color["brown"])
            self.eventLoop()
            pygame.display.update()
            clock.tick(60)

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
        scene.display.blit(textSurface, textRect)

    def renderImage(self, path, x, y):
        """ Renders images on the screen """
        image = pygame.image.load(path).convert()
        imageRect = image.get_rect(center = (int(x), int(y)))
        scene.display.blit(image, imageRect)

class menuScene(scene):
    """ This is a sub class from scene base class ; sceneMenu = a variant of scene with a menu """
    def __init__(self):
        super().__init__()
    
    
    

    


mainMenu = scene()
mainMenu.gameLoop()