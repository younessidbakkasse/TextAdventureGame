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
    scenes = {}
    def __init__(self, name, category):
        """ Set up the game display """
        self.running, self.click = True, False
        Scene.scenes[name] = category  

    def run_scene(self):
        """ scene main loop : basicly each scene has its own loop """
        while self.running:
            Scene.display.fill(colors["brown"])
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

    def mouse_clicks_run_scene(self, button_rect, scene):
        """ Checks if mouse points to a text or button (rect) """
        self.mx, self.my = pygame.mouse.get_pos()
        if button_rect.collidepoint((self.mx, self.my)) and self.click:
            self.click = False
            scene.run_scene()



class Menu(Scene):
    """ This is a sub class from scene base class ; sceneMenu = a variant of scene with a menu """
    def __init__(self, path):
        super().__init__()
        self.music_icon_path = path
        self.buttons = {}
    
    def render(self):
        # logo
        self.render_text("woods", 200, 55, colors["yellow"], 32)
        self.render_text("runner", 200, 100, colors["yellow"], 80)

        # menu items
        self.buttons["new game"] = self.render_text("New game", 200, int(DISPLAY_HEIGHT/2), colors["orange"], 40)
        self.buttons["options"] = self.render_text("Options", 200, int(DISPLAY_HEIGHT/2) + 50, colors["orange"], 40)        
        self.buttons["credit"] = self.render_text("Credit", 200, int(DISPLAY_HEIGHT/2) + 100, colors["orange"], 40)

        # render sound icon
        self.buttons["music on"] = self.render_image(self.music_icon_path, int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT - 40))

    def scene_events(self, event):
       if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button:
                self.click = True
                for button in self.buttons: 
                    self.mouse_clicks_run_scene(self.buttons[button], scene)

class Description(Scene):
    def render(self):
        # rendering the menu title
        self.render_text("Options", int(DISPLAY_WIDTH/2), 50, colors["orange"], 35)

        # render back icon
        self.render_image("Back Icon.png", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT - 40))

    def scene_events(self, event):
        pass
          
menu_music_on = Menu("music_on_icon.png")
menu_music_off = Menu("music_off_icon.png")


menu_music_on.run_scene()


    
       



