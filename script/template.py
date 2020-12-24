import manager
from scene import (
    Scene,
    Gui,
    gui, 
    player, 
    DISPLAY_HEIGHT, 
    DISPLAY_WIDTH,
)

################################# Menu Template #################################
def menu_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame 
    gui.render_frame('normal', 'pause')
    # render close button
    manager.game.scenes['menu'].buttons[Scene.previous_scene] = gui.render_button('button_close', int(DISPLAY_WIDTH) - 55, int(DISPLAY_HEIGHT/2) - 135)
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
    # render close button
    manager.game.scenes['credit'].buttons[Scene.previous_scene] = gui.render_button('button_back', DISPLAY_WIDTH - 60,  int(DISPLAY_HEIGHT/2) - 160)
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
    # render close button
    manager.game.scenes['stats'].buttons[Scene.previous_scene] = gui.render_button('button_close', int(DISPLAY_WIDTH) - 55, int(DISPLAY_HEIGHT/2) - 135)
    # render stats
    gui.render_text(f'Gold {int(player.gold)}', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 70), size=22, Regular=True)
    gui.render_text(f'Attack {int(player.attack)}', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 40), size=22, Regular=True)
    gui.render_text(f'Defense {int(player.defence)}', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 10), size=22, Regular=True)
    
    # render player's health bar
    gui.render_image('./assets/frames/bar.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 35))
    # render player's armor bar
    gui.render_image('./assets/frames/bar.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 80))

    # render icons
    gui.render_image('./assets/icons/heart.png', int(DISPLAY_WIDTH/2 - 72), int(DISPLAY_HEIGHT/2 + 35))
    gui.render_image('./assets/icons/level.png', int(DISPLAY_WIDTH/2 - 72), int(DISPLAY_HEIGHT/2 + 80))

    # render dynamique bar for both health and levels
    gui.render_rect(int(DISPLAY_WIDTH/2 - 55), int(DISPLAY_HEIGHT/2 + 22), int(140 * player.health/player.max_health), 25, Gui.colors['red'])
    gui.render_rect(int(DISPLAY_WIDTH/2 - 55), int(DISPLAY_HEIGHT/2 + 57), int(140 * player.current_xp/player.max_xp), 25, Gui.colors['yellow'])

    # render stats on bars
    gui.render_text(f'{int(player.health)}/{int(player.max_health)}', int(DISPLAY_WIDTH/2 + 10), int(DISPLAY_HEIGHT/2 + 35), size = 14)
    gui.render_text(f'Level {int(player.level)}', int(DISPLAY_WIDTH/2 + 10), int(DISPLAY_HEIGHT/2 + 80), size = 14)

################################# HomeTemplate #################################
def home_template():
    # render big centered logo
    gui.render_logo(160, True)
    # start game button
    manager.game.scenes['home'].buttons["pregame"] = gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 170) 

################################# How to play Template #################################
def howtoplay_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame
    gui.render_frame('big', 'how to play')
    # render close button
    manager.game.scenes['how to play'].buttons[Scene.previous_scene] = gui.render_button('button_close', int(DISPLAY_WIDTH) - 55,  int(DISPLAY_HEIGHT/2) - 165)
    # render how to play content
    gui.render_text('Use your mouse to play', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2), size = 22, Regular=True)


################################# Inventory Template #################################
def inventory_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame
    gui.render_frame('big', 'inventory')
    # render close button
    manager.game.scenes['inventory'].buttons[Scene.previous_scene] = gui.render_button('button_close', int(DISPLAY_WIDTH) - 55,  int(DISPLAY_HEIGHT/2) - 165)
    # render left and right buttons
    gui.render_button("button_left", 45, int(DISPLAY_HEIGHT/2)) 
    gui.render_button("button_right", DISPLAY_WIDTH - 45, int(DISPLAY_HEIGHT/2)) 
    # render how to play content
    gui.render_text("There's no items", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 3), Regular=True, size=19)
    gui.render_text("in your inventory.", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 21), Regular=True, size=19)
    # render store elements


################################# Quests Template #################################
def quests_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame
    gui.render_frame('normal', 'quests')
    # render close button
    manager.game.scenes['quests'].buttons[Scene.previous_scene] = gui.render_button('button_close', int(DISPLAY_WIDTH) - 55, int(DISPLAY_HEIGHT/2) - 135)
    # render how to play content
    gui.render_text('Current quest:', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 30), size=22, Regular=True)
    gui.render_text('Kill the boss', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 10), size=30, Regular=True)

################################# Store Template #################################
def store_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame
    gui.render_frame('normal', 'store')
    # render close button
    manager.game.scenes['store'].buttons[Scene.previous_scene] = gui.render_button('button_close', int(DISPLAY_WIDTH) - 55, int(DISPLAY_HEIGHT/2) - 135)
    # render left and right buttons
    gui.render_button("button_left", 40, int(DISPLAY_HEIGHT/2)) 
    gui.render_button("button_right", DISPLAY_WIDTH - 40, int(DISPLAY_HEIGHT/2)) 
    # render how to play content
    gui.render_text("Store is available only", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 10), Regular=True, size=19)
    gui.render_text("for Pro members.", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 10), Regular=True, size=19)
    # render store elements







