# game modules 
import pygame, sys

# pygame set up
pygame.init()
clock = pygame.time.Clock()

# pygame window set up
displayWidth = 400
displayHeight = 500

soundIcon = pygame.image.load("Sound Icon.png")
backIcon = pygame.image.load("Back Icon.png")

display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('game')

def textSurface(text, color, size = 38,):
        """ draws any text on the main window """
        gameFont = pygame.font.Font("Minecraft.ttf", size)
        return gameFont.render(text, False, color)

def menu():
    while True: 
        
        display.fill((49, 45, 46))
        mx, my = pygame.mouse.get_pos()

        textSurface1 = textSurface("woods", (249, 200, 51), 32)
        buttonText1 = textSurface1.get_rect(center = (int(displayWidth/2), 55))
        display.blit(textSurface1, buttonText1)

        textSurface2 = textSurface("Runner", (249, 200, 51), 80)
        buttonText2 = textSurface2.get_rect(center = (int(displayWidth/2), 100))
        display.blit(textSurface2, buttonText2)
                
        textSurface3 = textSurface("New game", (238, 117, 57))
        buttonText3 = textSurface3.get_rect(center = (int(displayWidth/2), int(displayHeight/2)))
        display.blit(textSurface3, buttonText3)

        textSurface4 = textSurface("Options", (238, 117, 57))
        buttonText4 = textSurface4.get_rect(center = (int(displayWidth/2), int(displayHeight/2 + 50)))
        display.blit(textSurface4, buttonText4)

        textSurface5 = textSurface("Credit", (238, 117, 57))
        buttonText5 = textSurface5.get_rect(center = (int(displayWidth/2), int(displayHeight/2 + 100)))
        display.blit(textSurface5, buttonText5)

        display.blit(soundIcon, (int(displayWidth/2 - 15), 440))

        if buttonText3.collidepoint((mx, my)):
            if click:
                game()
        if buttonText4.collidepoint((mx, my)):
            if click:
                options()
        if buttonText5.collidepoint((mx, my)):
            if click:
                credit()
        

        for event in pygame.event.get():
            click = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button:
                    click = True
            
        pygame.display.update()
        clock.tick(60)

def game():
    running = True
    while running:  
        display.fill((49, 45, 46))
        display.blit(backIcon, (int(displayWidth/2 - 15), 440))

        textSurface1 = textSurface("Game", (238, 117, 57))
        buttonText1 = textSurface1.get_rect(center = (int(displayWidth/2), 50))
        display.blit(textSurface1, buttonText1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button:
                    running = False
                    
        pygame.display.update()
        clock.tick(60)

def options():
    running = True
    while running:
        display.fill((49, 45, 46))
        display.blit(backIcon, (int(displayWidth/2 - 15), 440))

        textSurface1 = textSurface("Options", (238, 117, 57))
        buttonText1 = textSurface1.get_rect(center = (int(displayWidth/2), 50))
        display.blit(textSurface1, buttonText1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button:
                    running = False
                    
        pygame.display.update()
        clock.tick(60)

def credit():
    running = True
    while running:
        display.fill((49, 45, 46))
        display.blit(backIcon, (int(displayWidth/2 - 15), 440))

        textSurface1 = textSurface("Credit", (238, 117, 57))
        buttonText1 = textSurface1.get_rect(center = (int(displayWidth/2), 50))
        display.blit(textSurface1, buttonText1)

        textSurface2 = textSurface("Game design & production", (245, 245, 245), 20)
        buttonText2 = textSurface2.get_rect(center = (int(displayWidth/2), int(displayHeight/2 - 100)))
        display.blit(textSurface2, buttonText2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button:
                    running = False
                    
        pygame.display.update()
        clock.tick(60)

menu()