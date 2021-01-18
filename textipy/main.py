from textipy import game, scenario_en

if __name__ == "__main__":
    # Remove this line if you want to start your game from scratch
    game.scenes.update(scenario_en)
    # This is the only thing you need to starts your game    
    game.run()


