import manager
from scene import (
    Scene,
    Gui,
    Button,
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
    manager.game.scenes['Menu'].buttons.insert(0, Button('button_close', int(DISPLAY_WIDTH) - 55, int(DISPLAY_HEIGHT/2) - 135, Scene.previous_scene))
    # render menu options
    manager.game.scenes['Menu'].buttons.insert(1, Button('New Game', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 40), 'home', category='text'))
    manager.game.scenes['Menu'].buttons.insert(2,Button('Exit Game', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 10), 'exit', category='text'))
    manager.game.scenes['Menu'].buttons.insert(3,Button('Credit', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 60), 'credit', category='text'))
    

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
    manager.game.scenes['Credit'].buttons.insert(0,Button('button_close', DISPLAY_WIDTH - 60,  int(DISPLAY_HEIGHT/2) - 160, Scene.previous_scene))
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
    manager.game.scenes['Stats'].buttons.insert(0,Button('button_close', int(DISPLAY_WIDTH) - 55, int(DISPLAY_HEIGHT/2) - 135, Scene.previous_scene))
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
    manager.game.scenes['Home'].buttons.insert(0, Button('button_game', DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 170, 'Pregame'))

################################# How to play Template #################################
def howtoplay_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame
    gui.render_frame('big', 'how to play')
    # render close button
    manager.game.scenes['Help'].buttons.insert(0, Button('button_close', int(DISPLAY_WIDTH) - 55,  int(DISPLAY_HEIGHT/2) - 165, Scene.previous_scene))
    # render how to play content
    gui.render_text('Use your mouse to play', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2), size = 22, Regular=True)


################################# Inventory Template #################################
def inventory_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame
    gui.render_frame('big', 'inventory')
    # render close button
    manager.game.scenes['Inventory'].buttons.insert(10, Button('button_close', int(DISPLAY_WIDTH) - 55,  int(DISPLAY_HEIGHT/2) - 165, Scene.previous_scene))
    if len(player.inventory) == 0:
        # render no item message
        gui.render_text("There's no items", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 3), Regular=True, size=19)
        gui.render_text("in your inventory.", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 21), Regular=True, size=19)
    # render left and right buttons
    else:
        # render item holder
        for i, item in enumerate(list(player.inventory.items())[player.n:player.n+2]):
            gui.render_image('./assets/frames/holder.png', int(DISPLAY_WIDTH/2 - (-2*i+1)*75), int(DISPLAY_HEIGHT/2))
            manager.game.scenes['Inventory'].buttons.insert(i, Button('button_really_small', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) + 120, ' '))
            gui.render_text(item[0], int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) - 50, Regular=True, size=20)
            gui.render_text('Equip', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) + 120, Regular=True, size=20)
            i += 1
            
        # render navigation button for carsuoal

        # render right arrow
        if len(player.inventory) > 2 and not player.n >= len(player.inventory) - 2:
            manager.game.scenes['Inventory'].buttons.insert(2, Button("button_right", DISPLAY_WIDTH - 45, int(DISPLAY_HEIGHT/2), 'add', category='navigate'))
        # render left arrow
        if len(player.inventory) > 2 and player.n > 0:
            manager.game.scenes['Inventory'].buttons.insert(4, Button("button_left", 45, int(DISPLAY_HEIGHT/2), 'del', category='navigate'))
            del manager.game.scenes['Inventory'].buttons[:-2]
            
        print(player.n)
        #print(len(manager.game.scenes['Inventory'].buttons))
    # player checked inventory
    player.inventory_checked = True


################################# Quests Template #################################
def quests_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame
    gui.render_frame('normal', 'quests')
    # render close button
    manager.game.scenes['Quests'].buttons.insert(0, Button('button_close', int(DISPLAY_WIDTH) - 55, int(DISPLAY_HEIGHT/2) - 135, Scene.previous_scene))
    # render how to play content
    gui.render_text('Current quest:', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 30), size=22, Regular=True)
    gui.render_text('Kill the boss', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 10), size=30, Regular=True)

################################# Store Template #################################
def store_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame
    gui.render_frame('normal', 'store')
    # render close          
    manager.game.scenes['Store'].buttons.insert(0, Button('button_close', int(DISPLAY_WIDTH) - 55, int(DISPLAY_HEIGHT/2) - 135, Scene.previous_scene))
    # render left and right buttons
    gui.render_button("button_left", 40, int(DISPLAY_HEIGHT/2)) 
    gui.render_button("button_right", DISPLAY_WIDTH - 40, int(DISPLAY_HEIGHT/2)) 
    # render how to play content
    gui.render_text("Store is available only", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 10), Regular=True, size=19)
    gui.render_text("for Pro members.", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 10), Regular=True, size=19)

################################# Game Templates #################################
def loot_template():
    # only needed for a story game
    gui.render_gui()
    # render notification for inventory
    if not player.inventory_checked:
        gui.render_circle(DISPLAY_WIDTH - 70, DISPLAY_HEIGHT - 75, 8, Gui.colors['red'])



