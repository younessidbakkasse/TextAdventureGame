class Level:
    def __init__(self, level = 0):
        self.level = level
        self.current_score = 0
        self.max_score = 5 + (5 * self.level ** 2)
    
    

class Entity:
    def __init__(self, base_health = 250, base_level_score = 10, level = 0, attack = 10, defence = 2, gold = 10):
        self.level = level
        self.max_level_score = base_level_score + (base_level_score/2 * self.level)
        self.current_level_score = level * 10 + (level)
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