class Entity:
    def __init__(self, health = 250, level = 1, attack = 10, defence = 2):
        self.health = health
        self.level = level
        self.attack = attack
        self.defence = defence
        self.inventory = list()

    def death(self):
        pass

    def attacking(self):
        pass

    def defending(self):
        pass

    def running(self):
        pass

class Object:
    def __init__(self):
        self.name = None
        self.type = None

    def __str__(self):
        print(self.name, self.type)



    
class Player(Entity):
    def __init__(self):
        super().__init__()

    def healing(self):
        pass