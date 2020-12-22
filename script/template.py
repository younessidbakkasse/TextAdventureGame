import manager
from scene import (
    Gui,
    gui, 
    player, 
    DISPLAY_HEIGHT, 
    DISPLAY_WIDTH,
)

################################# Story Template #################################
# todo: needs to be a StoryScene
def before_game_template():
    gui.render_gui()
    #story text
    gui.render_text('Hi there, this is a story game.', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2- 80), size = 22, Regular=True)
    gui.render_text('are you sure you wanna play its', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2- 50), size = 22, Regular=True)
    gui.render_text('scary out there !', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2- 20), size = 22, Regular=True)
    # render left direction buttons
    manager.game.scenes['before game'].buttons['game'] = gui.render_button('button_small', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 70))
    gui.render_text('Play', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 70))


################################# Menu Template #################################
def menu_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame 
    gui.render_frame('normal', 'pause')
    # render menu options
    manager.game.scenes['menu'].buttons["home"] = gui.render_text('New Game', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 40), size = 35, Regular=True)
    manager.game.scenes['menu'].buttons["exit"] = gui.render_text('Exit Game', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 10), size = 35, Regular=True)
    manager.game.scenes['menu'].buttons["credit"] = gui.render_text('Credit', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 60), size = 35, Regular=True)
    

################################# Monster Fight Template #################################
def fight_template():
    gui.render_gui()
    # render frame
    gui.render_frame('normal', 'fight')

################################# Game Credit Template #################################
def credit_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    ## render frame
    gui.render_frame('big', 'credit')
    # render credit
    gui.render_text('Game design & production', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 40), size = 16, Regular=True)
    gui.render_text('Youness Id bakkasse', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 10), size = 25, Regular=True)
    gui.render_text('Sound effects', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 50), size = 16, Regular=True)
    gui.render_text('Soundhound.com', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 80), size = 25, Regular=True)


################################# Stats Template #################################
def stats_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame
    gui.render_frame('normal', 'stats')
    # render stats
    gui.render_text(f'Gold {int(player.gold)}', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 40))
    gui.render_text(f'Attack {int(player.attack)}', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 20))
    gui.render_text(f'Diffence {int(player.defence)}', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2))
    
    # render player's health bar
    gui.render_image('./assets/frames/bar.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 30))
    # render player's armor bar
    gui.render_image('./assets/frames/bar.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 65))

    # render icons
    gui.render_image('./assets/icons/heart.png', int(DISPLAY_WIDTH/2 - 65), int(DISPLAY_HEIGHT/2 + 30))
    gui.render_image('./assets/icons/level.png', int(DISPLAY_WIDTH/2 - 65), int(DISPLAY_HEIGHT/2 + 65))

    # render dynamique bar for both health and levels
    gui.render_rect(int(DISPLAY_WIDTH/2 - 50), int(DISPLAY_HEIGHT/2 + 20), int(125 * player.health/player.max_health), 20, Gui.colors['red'])
    gui.render_rect(int(DISPLAY_WIDTH/2 - 50), int(DISPLAY_HEIGHT/2 + 55), int(125 * player.current_xp/player.max_xp), 20, Gui.colors['yellow'])

    # render stats on bars
    gui.render_text(f'{int(player.health)}/{int(player.max_health)}', int(DISPLAY_WIDTH/2 + 10), int(DISPLAY_HEIGHT/2 + 32), size = 13)
    gui.render_text(f'Level {int(player.level)}', int(DISPLAY_WIDTH/2 + 10), int(DISPLAY_HEIGHT/2 + 67), size = 13)

################################# HomeTemplate #################################
def home_template():
    # render big centered logo
    gui.render_logo(160, True)
    # start game button
    manager.game.scenes['home'].buttons["before game"] = gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 170) 

################################# How to play Template #################################
def howtoplay_template():
    gui.render_gui()
    gui.render_transparent_background()
    # render frame
    gui.render_frame('big', 'how to play')
    # render how to play content
    gui.render_text('Use your mouse to play', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2), size = 22, Regular=True)


################################# Inventory Template #################################
def inventory_template():
    # render frame
    gui.render_frame('big', 'inventory')

    #render inventory boxes
    for i in range(3):
        for j in range(4):
            gui.render_image('./assets/frames/tall.png', int(80 * j + 80), int(150 + i * 120))


################################# Quests Template #################################
def quests_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame
    gui.render_frame('normal', 'quests')
    # render how to play content
    gui.render_text('Current quest: Kill the boss', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2), size=22, Regular=True)

################################# Store Template #################################
def store_template():
    gui.render_gui()
    gui.render_transparent_background()
    # render frame
    gui.render_frame('normal', 'store')
    # render left and right buttons
    gui.render_button("button_left", 40, int(DISPLAY_HEIGHT/2)) 
    gui.render_button("button_right", DISPLAY_WIDTH - 40, int(DISPLAY_HEIGHT/2)) 
    # render how to play content
    gui.render_text("Store is available only", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 10), Regular=True, size=19)
    gui.render_text("for Pro members.", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 10), Regular=True, size=19)
    # render store elements







