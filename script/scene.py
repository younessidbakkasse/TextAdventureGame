from gui import *
import sys

class Scene:
    # Set up the game display
    def __init__(self, scene_name):
        """ Constructor method runs when I creat an object using the Scene class """
        self.running = True 
        self.scene_name = scene_name
        self.buttons = {}
        self.mx, self.my = 0, 0

    def run_scene(self):
        """ scene's main loop : basicly each scene has its own loop """
        while self.running:  
            gui.render_background()
            self.render_template()
            self.get_events()
            pygame.display.flip()
            Gui.clock.tick(60)

    def render_template(self):
        pass

    def get_events(self):
        """ This function collects Mouse clicks from the user """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button: 
                    self.transition(controle.scenes)
    
    def transition(self, scenes):
        """ One hell of an importante method it checks if mouse points to a text or 
        button (rect) and also allows scene transitions from self to another depending 
        on the button's name"""
        for button_name, button in self.buttons.items():
            self.mx, self.my = pygame.mouse.get_pos()   
            if button != None and button.collidepoint((self.mx, self.my)):
                for scene_key, scene in scenes.items():
                    if scene_key == button_name:
                        controle.previous_scene = self.scene_name
                        # This may cause bugs in futur if it didn't ur a lucky mothafucka
                        self.buttons.popitem()
                        scene.run_scene()