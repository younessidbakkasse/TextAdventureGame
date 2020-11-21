import pygame, random

# Eng : global variables
# Fr : 
DISPLAY_HEIGHT = 500
DISPLAY_WIDTH = 400

class Gui:
    """ Eng : this class takes care of everything that has to do with rendering content and gui
    elements such as buttons, hover effect, text.."""

    """ Fr : this class takes care of everything that has to do with rendering content and gui
    elements such as buttons, hover effect, text.."""

    # Eng : initialising the pygame display and module it's a must
    # Fr : 
    pygame.init()
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()
    pygame.mouse.set_cursor(*pygame.cursors.tri_left)

    # Eng : the following loop generates random white squares
    # Fr :
    stars = [pygame.Rect(random.randint(0, DISPLAY_WIDTH), random.randint(0, DISPLAY_HEIGHT), 3, 3) for i in range(35)]
    
    # Eng : constructed a dict object for gui common button
    # Fr :
    gui_buttons = dict()

    # Eng : game color palette
    # Fr :
    colors = {
        "dark green" : (14, 43, 35),
        "dark blue" : (2, 17, 29),
        "white" : (251, 251, 251),
        "green": (18, 168, 113),
        "red" : (255, 0, 69),
        "yellow" : (250, 200, 50)
    }

    def render_ui_buttons(self):
        """ Eng : renders the same user interface buttons acroos all the scenes and stores them on list"""
        """ Fr : """

        # Eng : buttons on the right side
        # Fr :
        self.gui_buttons["scene1"] = self.render_button("button_music_on", DISPLAY_WIDTH - 40, 40)
        self.gui_buttons["scene2"] = self.render_button("button_help", DISPLAY_WIDTH - 90, 40)

        # Eng : buttons on the left side
        # Fr :
        self.gui_buttons["scene3"] = self.render_button("button_return", 40, 40)
        self.gui_buttons["scene4"] = self.render_button("button_pause", 90, 40)

        # Eng : buttons on the right down corner 
        # Fr :
        self.gui_buttons["scene5"] = self.render_button("button_inventory", DISPLAY_WIDTH - 40, DISPLAY_HEIGHT - 40)
        self.gui_buttons["scene6"] = self.render_button("button_character", DISPLAY_WIDTH - 90, DISPLAY_HEIGHT - 40)

        # Eng : quest's button on the left down corner
        # Fr :
        self.gui_buttons["scene7"] = self.render_button("button_large", 85, DISPLAY_HEIGHT - 40)
        self.render_text("quests", 85, DISPLAY_HEIGHT - 39, Gui.colors['white'])

    def render_background(self):
        """ Eng : renders a dark green background with random white stars """
        """ Fr : """
        Gui.display.fill(Gui.colors["dark green"])
        for star in self.stars:
            pygame.draw.rect(Gui.display, Gui.colors["white"], star)

    def render_logo(self, y, big_logo = True):
        """ Eng : renders the two versions of game logo : small & big """
        """ Fr : """
        if big_logo:
            self.render_text("woods", DISPLAY_WIDTH/2 + 7, y + 7, Gui.colors["dark blue"], 80)
            self.render_text("runner", DISPLAY_WIDTH/2 + 7, y + 67, Gui.colors["dark blue"], 80)
            self.render_text("woods", DISPLAY_WIDTH/2, y, Gui.colors["white"], 80)
            self.render_text("runner", DISPLAY_WIDTH/2, y + 60, Gui.colors["white"], 80)
        else:
            self.render_text("woods", DISPLAY_WIDTH/2 + 4, y + 4, Gui.colors["dark blue"], 30)
            self.render_text("runner", DISPLAY_WIDTH/2 + 4, y + 26, Gui.colors["dark blue"], 30)
            self.render_text("woods", DISPLAY_WIDTH/2, y, Gui.colors["white"], 30)
            self.render_text("runner", DISPLAY_WIDTH/2, y + 22, Gui.colors["white"], 30)

    def render_button(self, name, x, y):
        """ Eng : this function draw buttons from the asset/button file and checks hover effect """
        """ Fr : """
        path = f"./assets/buttons/buttons_normal/{name}.png"
        button = self.render_image(path, x, y)
        mx, my = pygame.mouse.get_pos()
        if button.collidepoint((mx, my)):
            path = f"./assets/buttons/buttons_pressed/{name}.png"
            button_pressed = self.render_image(path, x, y)
            return button_pressed

    def render_text(self, text, x, y, color, size = 20):
        """ Eng : Draws any text on the scene window and also returns a rectangle object wich have 
        coord attributes and collide methode """
        """ Fr : """
        game_font = pygame.font.Font("./assets/fonts/Minecraft.ttf", size)
        text_surface = game_font.render(text, False, color)
        text_rect = text_surface.get_rect(center = (int(x), int(y)))
        Gui.display.blit(text_surface, text_rect)
        return text_rect

    def render_image(self, path, x, y):
        """ Eng : Renders images and icons on the screen and returns a rect object """
        """ Fr : """
        image = pygame.image.load(path).convert_alpha()
        image_rect = image.get_rect(center = (int(x), int(y)))
        Gui.display.blit(image, image_rect)
        return image_rect