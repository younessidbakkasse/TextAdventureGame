class Entity:
    def __init__(self, health = 250, level = 1, attack = 10, defence = 2):
        self.health = health
        self.level = level
        self.attack = attack
        self.defence = defence
        self.inventory = list()

    def death(self):
        pass

    def attack(self):
        pass

    def defend(self):
        pass

    def run(self):
        pass

    
class Player(Entity):
    def __init__(self):
        super().__init__()

    def heal(self):
        pass