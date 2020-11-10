# game modules 
import pygame, sys

# pygame set up
pygame.init()
clock = pygame.time.Clock()

# pygame window set up
displayWidth = 500
displayHeight = 400


display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('game')

def textSurface(text, size = 30):
        """ draws any text on the main window """
        gameFont = pygame.font.Font("Minecraft.ttf", size)
        return gameFont.render(text, False, (255, 255, 255))



def menu():
    while True: 
        
        display.fill((165, 123, 73))
        mx, my = pygame.mouse.get_pos()
                
        textSurface1 = textSurface("Start game")
        buttonText1 = textSurface1.get_rect(center = (int(displayWidth/2), int(displayHeight/2 - 25)))
        display.blit(textSurface1, buttonText1)

        textSurface2 = textSurface("Options")
        buttonText2 = textSurface2.get_rect(center = (int(displayWidth/2), int(displayHeight/2 + 25)))
        display.blit(textSurface2, buttonText2)

        if buttonText1.collidepoint((mx, my)):
            if click:
                game()
        if buttonText2.collidepoint((mx, my)):
            if click:
                options()

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
        display.fill((165, 123, 73))

        textSurface1 = textSurface("Game")
        buttonText1 = textSurface1.get_rect(center = (int(displayWidth/2), int(displayHeight/2)))
        display.blit(textSurface1, buttonText1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        pygame.display.update()
        clock.tick(60)

def options():
    running = True
    while running:
        display.fill((165, 123, 73))

        textSurface1 = textSurface("Options")
        buttonText1 = textSurface1.get_rect(center = (int(displayWidth/2), int(displayHeight/2)))
        display.blit(textSurface1, buttonText1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        pygame.display.update()
        clock.tick(60)

menu()