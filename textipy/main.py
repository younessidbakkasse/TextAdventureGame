from scene import game

game.title = 'Dead Island'

# Comment : First scene
game.scenes['Pregame'] = StoryScene(
        name = 'Pregame',
        buttons = [['Commencer', 'Autre', 'normal']],
        text = 'Bonne annee à tous le monde.',
)

# Comment : Second scene
game.scenes['Autre'] = StoryScene(
        name = 'Autre',
        buttons = [['Start Playing', '', 'normal']],
        text = 'Hi there, this a story game, its scary out there are you sure you wanna play.',
)

game.run()
