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


class Scene():
    pygame.init()
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()
    def __init__(self):
        """ Set up the game display """
        self.running, self.click = True, False

    def run_scene(self):
        """ scene main loop : basicly each scene has its own loop """
        while self.running:
            Scene.display.fill(color["brown"])
            self.render()
            self.get_events()
            pygame.display.update()
            Scene.clock.tick(60)

    def get_events(self):
        """ This function collects keyboard and mouse clicks from the user """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.scene_events(event)

    def render_text(self, text, x, y, color, size = 20):
        """ Draws any text on the scene window """
        game_font = pygame.font.Font("Minecraft.ttf", size)
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

    def mouse_click(self, button_rect):
        """ Checks if mouse points to a text or button (rect) """
        self.mx, self.my = pygame.mouse.get_pos()
        if button_rect.collidepoint((self.mx, self.my)) and self.click:
            return True
        else: 
            return False


class Menu(Scene):
    """ This is a sub class from scene base class ; sceneMenu = a variant of scene with a menu """
    def __init__(self, path):
        super().__init__()
        self.music_icon_path = path
    
    def render(self):
        # logo
        self.render_text("woods", 200, 55, color["yellow"], 32)
        self.render_text("runner", 200, 100, color["yellow"], 80)

        # menu items
        self.render_text("New game", 200, int(DISPLAY_HEIGHT/2), color["orange"], 40)
        self.render_text("Options", 200, int(DISPLAY_HEIGHT/2) + 50, color["orange"], 40)        
        self.render_text("Credit", 200, int(DISPLAY_HEIGHT/2) + 100, color["orange"], 40)

        # render sound icon
        music_button = self.render_image(self.music_icon_path, int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT - 40))

        if self.mouse_click(music_button):
            menu_music_off.run_scene()

    def scene_events(self, event):
       if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button:
                self.click = True

class Description(Scene):
    def render(self):
        # rendering the menu title
        self.render_text("Options", int(DISPLAY_WIDTH/2), 50, color["orange"], 35)

        # render back icon
        self.render_image("Back Icon.png", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT - 40))

    def scene_events(self, event):
        pass
          
menu_music_on = Menu("music_on_icon.png")
menu_music_off = Menu("music_off_icon.png")

menu_music_on.run_scene()


    
       



