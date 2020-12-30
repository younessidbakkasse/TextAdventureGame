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
    manager.game.scenes['Menu'].buttons['close'] = Button('button_close', int(DISPLAY_WIDTH) - 55, int(DISPLAY_HEIGHT/2) - 135, Scene.previous_scene)
    # render menu options
    manager.game.scenes['Menu'].buttons["home"] = Button('New Game', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 40), 'home', category='text')
    manager.game.scenes['Menu'].buttons["exit"] = Button('Exit Game', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 10), 'exit', category='text')
    manager.game.scenes['Menu'].buttons["credit"] = Button('Credit', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 60), 'credit', category='text')
    

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
    manager.game.scenes['Credit'].buttons['close'] = Button('button_close', DISPLAY_WIDTH - 60,  int(DISPLAY_HEIGHT/2) - 160, Scene.previous_scene)
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
    manager.game.scenes['Stats'].buttons['close'] = Button('button_close', int(DISPLAY_WIDTH) - 55, int(DISPLAY_HEIGHT/2) - 135, Scene.previous_scene)
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
    manager.game.scenes['Home'].buttons["Pregame"] = Button('button_game', DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 170, 'Pregame')

################################# How to play Template #################################
def howtoplay_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame
    gui.render_frame('big', 'how to play')
    # render close button
    manager.game.scenes['Help'].buttons['close'] = Button('button_close', int(DISPLAY_WIDTH) - 55,  int(DISPLAY_HEIGHT/2) - 165, Scene.previous_scene)
    # render how to play content
    gui.render_text('Use your mouse to play', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2), size = 22, Regular=True)


################################# Inventory Template #################################
def inventory_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    def frame():
        # render frame
        gui.render_frame('big', 'inventory')
        # render close button
        manager.game.scenes['Inventory'].buttons['close'] = Button('button_close', int(DISPLAY_WIDTH) - 55,  int(DISPLAY_HEIGHT/2) - 165, Scene.previous_scene)
    frame()
    if len(player.inventory) == 0:
        # render no item message
        gui.render_text("There's no items", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 3), Regular=True, size=19)
        gui.render_text("in your inventory.", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 21), Regular=True, size=19)
    # render left and right buttons
    else:
        # render item holder
        for i, item in enumerate(list(player.inventory.items())[player.n:player.n+2]):
            gui.render_image('./assets/frames/holder.png', int(DISPLAY_WIDTH/2 - (-2*i+1)*75), int(DISPLAY_HEIGHT/2))

            # render item info
            # render shields and weapons elements
            gui.render_text(item[1].name, int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) - 100, Regular=True, size=16)
            if item[1].type == 'shield' or item[1].type == 'weapon':
                gui.render_text(f'Atk +{item[1].attack}', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) - 64, Regular=True, size=18)
                gui.render_text(f'Def +{item[1].defence}', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) - 42, Regular=True, size=18)
                manager.game.scenes['Inventory'].buttons[f'equip {item[0]}'] = Button('button_really_small', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) + 120, 'equip', obj=item[1])
                gui.render_text('Equip', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) + 120, Regular=True, size=20)
            # render food elements
            elif item[1].type == 'food' or item[1].type == 'potion':
                gui.render_text(f'Health', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) - 64, Regular=True, size=18)
                gui.render_text(f'+{item[1].health} HP', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) - 42, Regular=True, size=18)
                manager.game.scenes['Inventory'].buttons[f'use {item[0]}'] = Button('button_really_small', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) + 120, 'use', obj=item[1])
                gui.render_text('Use', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) + 120, Regular=True, size=20)
            # render Sell buttons
            elif item[1].type == 'or' or item[1].type == 'material':
                gui.render_text(f'Value', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) - 64, Regular=True, size=18)
                gui.render_text(f'+{item[1].value} Gold', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) - 42, Regular=True, size=18)
                manager.game.scenes['Inventory'].buttons[f'sell {item[0]}'] = Button('button_really_small', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) + 120, 'sell', obj=item[1])
                gui.render_text('Sell', int(DISPLAY_WIDTH/2 - (-2*i+1)*75),  int(DISPLAY_HEIGHT/2) + 120, Regular=True, size=20)
            # render item image
            gui.render_image(f'./assets/items/{item[0]}.png', int(DISPLAY_WIDTH/2 - (-2*i+1)*75), int(DISPLAY_HEIGHT/2 + 25), scale=True)
            i += 1

        # render navigation button for carsuoal
        # render right arrow
        if len(player.inventory) > 2 and not player.n >= len(player.inventory) - 2:
            manager.game.scenes['Inventory'].buttons['right arrow'] = Button("button_right", DISPLAY_WIDTH - 45, int(DISPLAY_HEIGHT/2), 'next', category='navigate')
        # render left arrow
        if len(player.inventory) > 2 and player.n > 0:
            manager.game.scenes['Inventory'].buttons['left arrow'] = Button("button_left", 45, int(DISPLAY_HEIGHT/2), 'previous', category='navigate')   
    # player checked his inventory
    player.inventory_checked = True


################################# Quests Template #################################
def quests_template():
    gui.render_gui(pause=True)
    gui.render_transparent_background()
    # render frame
    gui.render_frame('normal', 'quests')
    # render close button
    manager.game.scenes['Quests'].buttons['close'] = Button('button_close', int(DISPLAY_WIDTH) - 55, int(DISPLAY_HEIGHT/2) - 135, Scene.previous_scene)
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
    manager.game.scenes['Store'].buttons['close'] = Button('button_close', int(DISPLAY_WIDTH) - 55, int(DISPLAY_HEIGHT/2) - 135, Scene.previous_scene)
    # render left and right buttons
    gui.render_button("button_left", 40, int(DISPLAY_HEIGHT/2)) 
    gui.render_button("button_right", DISPLAY_WIDTH - 40, int(DISPLAY_HEIGHT/2)) 
    # render how to play content
    gui.render_text("Store is available only", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 10), Regular=True, size=19)
    gui.render_text("for Pro members.", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 10), Regular=True, size=19)



