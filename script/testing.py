def myfunc(n):
  return lambda a : a * n

doubli = myfunc(3)

print(doubli)

class Description(Scene):
    """ This is a sub class from scene base class ; sceneMenu = a variant of scene with a menu """
    back_icon_path = "./assets/icons/back_icon.png"
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def render(self):
        # menu item
        self.render_text(self.name, int(DISPLAY_WIDTH/2), 70, colors["orange"], 40)

        # render sound icon
        self.buttons["back_icon"] = self.render_image(Description.back_icon_path, int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT - 50))

    def scene_events(self, event):
       if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button:
                self.click = True 
                controle.to_destination_scene()