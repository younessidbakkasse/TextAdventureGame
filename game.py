
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

while True: 
    display.fill((255, 83, 43))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.display.update()
    clock.tick(60)
