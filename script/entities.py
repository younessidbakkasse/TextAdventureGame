class Entity:
    def __init__(self, base_health = 250, level = 1, attack = 10, defence = 2, gold = 10):
        self.level = level
        self.max_health = base_health + (base_health/10 * self.level)
        self.health =  self.max_health
        self.attack = attack * self.level 
        self.defence = defence * self.level
        self.gold = gold
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