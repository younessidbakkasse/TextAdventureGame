class Entity:
    def __init__(self, level = 1, attack = 8, defence = 4, gold = 10):
        self.level = level
        self.max_xp = 5 + (5 * self.level ** 2)
        self.current_xp = 0

        self.max_health = 150 + (15 * self.level)
        self.health = self.max_health

        #todo use setters and getters for this

        self.attack = attack + attack * self.level/2 
        self.defence = defence + defence * self.level/3
        self.gold = gold

        self.inventory = dict()

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

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.inventory_checked = True
        self.n = 0

    def healing(self):
        pass

    def level_up(self):
        if self.current_xp >= self.max_xp:
            self.current_xp -= self.max_xp
            self.update_levels()
            self.level += 1

    def add_item_inventory(self, item):
        self.inventory[item] = Object(item)

    def reset(self):
        pass

# loot items
class Object:
    items_list = {
        # Weapons
        'axe' : {'atk' : 35, 'def' : 5},
        'bow' : {'atk' : 55, 'def' : 0},
        'iron sword' : {'atk' : 38, 'def' : 10},
        'silver sword' : {'atk' : 49, 'def' : 15},
        'golden sword' : {'atk' : 90, 'def' : 30},
        'knife' : {'atk' : 12, 'def' : 0},
        'pickaxe' : {'atk' : 24, 'def' : 3},
        'hammer' : {'atk' : 30, 'def' : 4},
        'torch' : {'atk' : 20, 'def' : 30},
        'wand' : {'atk' : 120, 'def' : 20},
        'sapphire wand' : {'atk' : 180, 'def' : 20},

        # shields
        'wooden shield' : {'atk' : 0, 'def' : 40},
        'iron shield' : {'atk' : 2, 'def' : 60},
        'wooden armor' : {'atk' : 0, 'def' : 50},
        'iron armor' : {'atk' : 3, 'def' : 80},
        'wizard hat' : {'atk' : 15, 'def' : 30},

        # materials
        'book' : {'name' : 'Book'},
        'coin' : {'name' : 'Silver Coin'},
        'key' : {'name' : 'Golden Key'},
        'map' : {'name' : 'Map'},
        'gear' :  {'name' : 'Gear'},

        # Monster parts
        'bone' : {'name' : 'Bone'},
        'monster meat' : {'name' : 'Monster Meat'},
        'monster eye' : {'name' : 'Monster Eye'},
        'skull' : {'name' : 'Human Skull'},

        # Gems
        'gold ingot' : {'name' : 'Gold Ingot', 'value' : 50},
        'pearl' : {'name' : 'Pearl', 'value' : 100},
        'emerald' : {'name' : 'Emerald', 'value' : 150},
        'topaz' : {'name' : 'Topaz', 'value' : 80},
        'diamond' : {'name' : 'Diamond', 'value' : 250},
        'obsidian' : {'name' : 'Obsidian', 'value' : 180},

        # potions
        'blue potion' : {'name' : 'Blue Potion', 'health' : 100},
        'green potion' : {'name' : 'Green Potion', 'health' : 150},
        'red potion' : {'name' : 'Red Potion', 'health' : 200},
        'water' : {'name' : 'Water', 'health' : 50},
    }

    
    def __init__(self, name):
        self.name = name
        
        

    def __str__(self):
        print(self.name, self.type)

# create a player 
player = Player()