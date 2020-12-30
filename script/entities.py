import manager

class Entity:
    def __init__(self, level = 1, attack = 8, defence = 4, gold = 10):
        self.level = level
        self.max_xp = 5 + (5 * self.level ** 2)
        self.current_xp = 0

        self.max_health = 150 + (15 * self.level)
        self.health = 100

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
        self.equiped = dict()

    def healing(self):
        pass

    def eat(self, food):
        if self.health < self.max_health:
            self.health += food.health
            if self.health > self.max_health:
                self.health = self.max_health
            self.inventory.pop(food.name.casefold())
            manager.game.scenes['Inventory'].buttons.pop(f'use {food.name.casefold()}')

    def sell(self, item):
        self.gold += item.value
        self.inventory.pop(item.name.casefold())
        manager.game.scenes['Inventory'].buttons.pop(f'sell {item.name.casefold()}')

    def level_up(self):
        if self.current_xp >= self.max_xp:
            self.current_xp -= self.max_xp
            self.update_levels()
            self.level += 1

    def add_item_inventory(self, item):
        print(item)
        self.inventory[item] = Object(item)

    def equip(self, item):
        self.equiped[item.name] = item


    def reset(self):
        pass

# loot items
class Object:
    items_list = {
        # Weapons
        'axe' : {'name' : 'Axe', 'atk' : 35, 'def' : 5, 'type' : 'weapon'},
        'bow' : {'name' : 'Bow', 'atk' : 55, 'def' : 0, 'type' : 'weapon'},
        'iron sword' : {'name' : 'Iron Sword', 'atk' : 38, 'def' : 10, 'type' : 'weapon'},
        'silver sword' : {'name' : 'Silver Sword', 'atk' : 49, 'def' : 15, 'type' : 'weapon'},
        'golden sword' : {'name' : 'Golden Sword', 'atk' : 90, 'def' : 30, 'type' : 'weapon'},
        'knife' : {'name' : 'Knife', 'atk' : 12, 'def' : 0, 'type' : 'weapon'},
        'pickaxe' : {'name' : 'Pickaxe', 'atk' : 24, 'def' : 3, 'type' : 'weapon'},
        'hammer' : {'name' : 'Hammer', 'atk' : 30, 'def' : 4, 'type' : 'weapon'},
        'torch' : {'name' : 'Torch', 'atk' : 20, 'def' : 30, 'type' : 'weapon'},
        'wand' : {'name' : 'Magic Wand', 'atk' : 120, 'def' : 20, 'type' : 'weapon'},
        'great wand' : {'name' : 'Great Wand', 'atk' : 180, 'def' : 20, 'type' : 'weapon'},

        # shields
        'wooden shield' : {'name' : 'Wooden Shield', 'atk' : 0, 'def' : 40, 'type' : 'shield'},
        'iron shield' : {'name' : 'Iron Shield', 'atk' : 2, 'def' : 60, 'type' : 'shield'},
        'wooden armor' : {'name' : 'Wooden Armor', 'atk' : 0, 'def' : 50, 'type' : 'shield'},
        'iron armor' : {'name' : 'Iron Armor', 'atk' : 3, 'def' : 80, 'type' : 'shield'},
        'wizard hat' : {'name' : 'Wizard Hat', 'atk' : 15, 'def' : 30, 'type' : 'shield'},

        # materials
        'book' : {'name' : 'Book', 'value' : 5, 'type' : 'material'},
        'golden coin' : {'name' : 'Golden Coin', 'value' : 1, 'type' : 'material'},
        'golden key' : {'name' : 'Golden Key', 'value' : 10, 'type' : 'material'},
        'map' : {'name' : 'Map', 'value' : 3, 'type' : 'material'},
        'gear' :  {'name' : 'Gear', 'value' : 2, 'type' : 'material'},

        # Monster parts
        'bone' : {'name' : 'Bone', 'value' : 3, 'type' : 'material'},
        'monster meat' : {'name' : 'Monster Meat', 'value' : 8, 'type' : 'material'},
        'monster eye' : {'name' : 'Monster Eye', 'value' : 15, 'type' : 'material'},
        'skull' : {'name' : 'Human Skull', 'value' : 20, 'type' : 'material'},

        # Gems
        'gold ingot' : {'name' : 'Gold Ingot', 'value' : 50, 'type' : 'or'},
        'pearl' : {'name' : 'Pearl', 'value' : 100, 'type' : 'or'},
        'emerald' : {'name' : 'Emerald', 'value' : 150, 'type' : 'or'},
        'topaz' : {'name' : 'Topaz', 'value' : 80, 'type' : 'or'},
        'diamond' : {'name' : 'Diamond', 'value' : 250, 'type' : 'or'},
        'obsidian' : {'name' : 'Obsidian', 'value' : 180, 'type' : 'or'},

        # potions
        'blue potion' : {'name' : 'Blue Potion', 'health' : 100, 'type' : 'potion'},
        'green potion' : {'name' : 'Green Potion', 'health' : 150, 'type' : 'potion'},
        'red potion' : {'name' : 'Red Potion', 'health' : 200, 'type' : 'potion'},
        'water' : {'name' : 'Water', 'health' : 15, 'type' : 'potion'},

        # food
        'apple' : {'name' : 'Apple', 'health' : 20, 'type' : 'food'},
        'fish' : {'name' : 'Fish', 'health' : 40, 'type' : 'food'},
        'meat' : {'name' : 'Meat', 'health' : 50, 'type' : 'food'},
        'wine' : {'name' : 'Wine', 'health' : 30, 'type' : 'food'},
        'bread' : {'name' : 'Bread', 'health' : 35, 'type' : 'food'},
    }
    
    def __init__(self, name):
        for item_key, item in Object.items_list.items():
            if item_key == name:
                self.name = item['name']
                self.type = item['type']
                if self.type == 'weapon' or self.type == 'shield':
                    self.attack = item['atk']
                    self.defence = item['def']
                elif self.type == 'potion' or self.type == 'food':
                    self.health = item['health']
                elif self.type == 'or' or self.type == 'material':
                    self.value = item['value']

    def __str__(self):
        return f'{self.name}, {self.type}'

# create a player 
player = Player()
