class Entity:
    def __init__(self, level = 1, attack = 8, defence = 4, gold = 10):
        self.level = level
        self.max_xp = 5 + (5 * self.level ** 2)
        self.current_xp = 0

        self.max_health = 150 + (15 * self.level)
        self.health = self.max_health

        self.attack = attack + attack * self.level/2 
        self.defence = defence + defence * self.level/3
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
    
    def update_levels(self):
        self.max_xp = 5 + (5 * self.level ** 2)
        self.max_health = 150 + (15 * self.level)
        self.attack = attack + attack * self.level/2 
        self.defence = defence + defence * self.level/3



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

    def level_up(self):
        if self.current_xp >= self.max_xp:
            self.current_xp -= self.max_xp
            self.update_levels()
            self.level += 1
            