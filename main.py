""" This game is made by Youness ID BAKKASSE; https://github.com/younessidbakkasse/
its a school project to initiat with Python programming 
for more informations and licence please check README file attached to the folder."""


import pygame

class Game:
    def __init__(self):
        """ Set up the game window """
        pygame.init()
        self.running = True
        self.windowWidth = 500
        self.windowHeight = 400
        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))


    def gameLoop(self):
        """ main game loop """
        while self.running:
            pygame.display.fl

    def drawText(self, text, x, y ,size = 20):
        """ draws any text on the main window """
        gameFont = pygame.font.Font("./assets/Minecraft.ttf", size)
        textSurface = gameFont.render(text, False, objectColor)
        textRect = textSurface.get_rect(center = (int(x), int(y)))
        display.blit(textSurface, textRect)