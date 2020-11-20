""" This game is made by Youness ID BAKKASSE; https://github.com/younessidbakkasse/
its a school project to initiat with Python programming 
for more informations and licence please check README file attached to the folder."""

# Importing modules: pygame is a module that allows us to draw on screen
import pygame, sys
from entity import Entity, Player
from gui import Gui, Scene

gui = Gui()

class Start(Scene):
    """ This is a sub class from scene base class """
    def __init__(self, scene_name):
        super().__init__(scene_name)
        
    def render_template(self):
        # Logo
        gui.render_logo(150, True)
        # start game button
        self.buttons["main_game"] = gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 160) 

class Game(Scene):
    def __init__(self, scene_name):
        super().__init__(scene_name)

    def render_template(self):
        # renders small logo on the screen
        gui.render_logo(30, False)

        # render ui common buttons
        gui.render_ui_buttons()   

class Controle: 
    def __init__(self):
        self.previous_scene = "main_game"
        self.scenes_keys = ["start", "main_game"]
        self.scenes_values = [Start("start"), Game("main_game")]
        self.scenes = {key:value for key, value in zip(self.scenes_keys, self.scenes_values)}
    
    def run_game(self):
        self.scenes["start"].run_scene()

player = Player()

controle = Controle()
controle.run_game()


    

    


    

    
       



