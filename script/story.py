from gui import Gui, pygame

# Eng : creating gui object
# Fr : 
gui = Gui()


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
        Also one we choose a scene ex (1, 0) a whole scene column is deleted since we will never
        pass by those scenes.
        - Also if we made some choices that lead us to a scene that is connected to the first 
        scene (0, 0), the choice leading to that first will be deleted to prevent player from 
        stating from the beginning.
        - One column or a row will be deleted each time a player choses one direction. This 
        way we insure story consistency and story flow.

    Fr : 

"""

story = {
    "scene1" : {
        "text" : "Washed ashore, you have only vague recollections of what happened. The past seems unimportant now. Shivering, you watch the bodies float among the debris. No ships can be seen on the horizon.",
        "choices" : ["Explore the beach"] 
    },

    "scene2" : {
        "text" : "There is nothing here but sand and gravel. Or so it may seem. You feel a painful sensation in your left foot, causing you to take a step backawards. Glimmering in the sun, a sharp object is revealed.",
        "choices" : ["Examine the object"] 
    },

    "scene3" : {
        "text" : "You discover footprints in the sand, leading north. it's late in the afternoon. If there's another survivor out there , you should find this person before it gets dark.",
        "choices" : ["Follow the footprints", "Study the footprints"]
    },

    "scene4" : {
        "sub_scene4" : "test",
        "choices" : "fight"
    }

}




