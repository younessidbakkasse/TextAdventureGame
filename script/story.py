""" This game is made by Youness ID BAKKASSE; https://github.com/younessidbakkasse/
its a school project to initiat with Python programming 
for more informations and licence please check README file attached to the folder."""

# Eng : the game map each point corresponds to a diffrent scene
# FR : 

""" 
You * * * * * * * * * * * 
    * * * * * * * * * * *
    * * * * * * * * * * *
    * * * * * * * * * * *
    * * * * * * * * * * *
    * * * * * * * * * * *
    * * * * * * * * * * *
    * * * * * * * * * * *
    * * * * * * * * * * * 
    * * * * * * * * * * * Boss

    
    # Rules

    Eng : monsters and loots will be deployed randomly, monsters level will increase as you get close to the 
    boss. each scene will have maximum 2 direction choices but there will 
    be other choices depending on the scene, if it contains monsters or objects. Once you passed a scene
    you can no longer go back to the previous scene but How ?
        - Take for example the first scene (0, 0), it has two direction choices, once we chose (1, 0) 
        or (0, 1), we can no longer go back to the previous scene (0, 0). 
        Also once we choose a scene ex (1, 0) a whole scene column is deleted since we will never
        pass by those scenes.
        - Also if we made some choices that lead us to a scene that is connected to the first 
        scene (0, 0), the choice leading to that first will be deleted to prevent player from 
        stating from the beginning.
        - One column or a row will be deleted each time a player choses one direction. This 
        way we insure story consistency and story flow.

    Fr : 
"""

# todo : 

