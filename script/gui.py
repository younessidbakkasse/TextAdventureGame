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

    # Eng : display set up
    # FR :
    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    pygame.display.set_caption("Wood Runner", "favicon")

    # Eng : set up game favicon
    # Fr : 
    favicon = pygame.image.load("./assets/icons/favicon.png")
    pygame.display.set_icon(favicon)

    # Eng : the following loop generates random white squares
    # Fr :
    stars = [pygame.Rect(random.randint(0, DISPLAY_WIDTH), random.randint(0, DISPLAY_HEIGHT), 3, 3) for i in range(35)]
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
    
    def __init__(self):
        self.gui_buttons = {}

    def render_ui_buttons(self, pause = False):
        """ Eng : renders the same user interface buttons acroos all the scenes and stores them on list"""
        """ Fr : """

        # Eng : buttons on the right side
        # Fr :
        self.gui_buttons["music"] = self.render_button('button_music_on', DISPLAY_WIDTH - 40, 40)
        self.gui_buttons["how to play"] = self.render_button("button_help", DISPLAY_WIDTH - 90, 40)

        # Eng : buttons on the left side
        # Fr :
        self.gui_buttons["store"] = self.render_button("button_cart", 90, 40)
        if not pause:
            self.gui_buttons["menu"] = self.render_button("button_pause", 40, 40)
        else:
            # todo : there is a bug here
            self.gui_buttons.pop('menu', 'key not found')
            self.gui_buttons['pause'] = self.render_button("button_start", 40, 40)

        # Eng : buttons on the right down corner 
        # Fr :
        self.gui_buttons["inventory"] = self.render_button("button_inventory", DISPLAY_WIDTH - 40, DISPLAY_HEIGHT - 40)
        self.gui_buttons["stats"] = self.render_button("button_character", DISPLAY_WIDTH - 90, DISPLAY_HEIGHT - 40)

        # Eng : quest's button on the left down corner
        # Fr :
        self.gui_buttons["quests"] = self.render_button("button_large", 85, DISPLAY_HEIGHT - 40)
        self.render_text("quests", 85, DISPLAY_HEIGHT - 39, Gui.colors['white'])
        
    def render_background(self):
        """ Eng : renders a dark green background with random white stars """
        """ Fr : """
        Gui.display.fill(Gui.colors["dark green"])
        for star in self.stars:
            pygame.draw.rect(Gui.display, Gui.colors["white"], star)

    def render_frame(self, frame_type, frame_name):
        # render frame
        self.render_image(f'./assets/frames/{frame_type}.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2))
        if frame_type == 'normal':
            # render close button
            # todo Scene.previous_scene is undefined
            self.gui_buttons['Scene.previous_scene'] = self.render_button('button_close', 355, 155)
            # render menu pause title
            self.render_text(frame_name, int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 80))
        if frame_type == 'big':
            # render close button
            self.gui_buttons['Scene.previous_scene'] = self.render_button('button_close', 355, 45)
            # render menu pause title
            self.render_text(frame_name, int(DISPLAY_WIDTH/2), 60)

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
        if button.collidepoint(mx, my):
            path = f"./assets/buttons/buttons_pressed/{name}.png"
            button_pressed = self.render_image(path, x, y)
            return button_pressed
        return button
        
    def render_text(self, text, x, y, color = colors['white'], size = 16):
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

    def render_rect(self, x, y, width, height, color):
        pygame.draw.rect(Gui.display, color, pygame.Rect(int(x), int(y), width, height))
