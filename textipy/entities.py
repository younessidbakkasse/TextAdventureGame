import manager, random

class Entity:
    # Eng: this is a main entity class for both monsters and player 
    # Fr: ceci est la class pour les monstres et le joueur
    def __init__(self, level = 1, attack = 8, defence = 4, gold = 10):
        # Eng: initializing data
        # Fr: initialisation des données 
        self.level = level
        self.max_xp = 5 + (5 * self.level ** 2)
        self.current_xp = 0
        self.equiped = dict()
        self.is_fighting = None
        self.is_turn = False

        self.max_health = 150 + (15 * self.level)
        self.health = self.max_health
        
        self.attack = attack
        self.defence = defence
        self.gold = gold

        self.inventory = dict()

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.inventory_checked = True
        self.is_turn = True
        self.combat, self.won = False, False
        self.n = 0

    def reset(self):
        """ Eng: resets all stats after game over
            Fr: reset les caracteristiques et les stats après un game over"""
        self.__init__()

    def update_levels(self):
        """ Eng: update health bar and other stats when player level up
            Fr: augmente la seuile de la bar de santé et attack, deffence pour chaque niveau d'experience"""
        self.max_xp = 5 + (5 * self.level ** 2)
        self.max_health = 150 + (15 * self.level)
        self.attack = self.attack + int(self.attack * self.level/4)
        self.defence = self.defence + int(self.defence * self.level/6)

    def eat(self, food):
        """ Eng: this function test if your health is maxed out if not it adds the food to your health bar
            Fr: c'est pour boire les potions ou manger la nourriture"""
        if self.health < self.max_health:
            self.health += food.health
            if self.health > self.max_health:
                self.health = self.max_health
            self.inventory.pop(food.name.casefold())
            manager.game.scenes['Inventory'].buttons.pop(f'use {food.name.casefold()}')

    def sell(self, item):
        """Eng: this function sells your items that can be sold in your inventory
            Fr: cette fonction sert a vendre les items dans ton inventaire"""
        self.gold += item.value
        self.inventory.pop(item.name.casefold())
        manager.game.scenes['Inventory'].buttons.pop(f'sell {item.name.casefold()}')

    def equip(self, item):   
        """Eng: this function equip items ex shield or weapons when click button equip in inventory
            Fr: cette fonction c'est pour equiper les armes et tout type de bouclier dans ton inventaire.""" 
        # This equips item and adds stats 
        def equip_item():
            self.equiped[item.name] = item
            self.attack += item.attack
            self.defence += item.defence
            self.inventory[item.name.casefold()].status = 'Equiped'
        # This check if there is two same item types in inventory 
        if len(self.equiped) == 0:
            equip_item()
        else:
            for equiped_item in list(self.equiped.values()):
                if equiped_item.type != item.type and len(self.equiped) < 2:
                    equip_item()

    def unequip(self, item):
        """Eng: this function unequip items ex shield or weapons when click button equiped in inventory
            Fr: cette fonction sert à enlever les armes et les boucliers bref l'inverse de equip""" 
        self.equiped.pop(item.name)
        self.attack -= item.attack
        self.defence -= item.defence
        self.inventory[item.name.casefold()].status = 'Equip' 

    def level_up(self):
        """Eng: this function is bisacly a level up function
            Fr: cette fonction sert a limiter l'xp du joueur comme ça il est tjr inferieure à l'xp max.""" 
        if self.current_xp >= self.max_xp:
            self.current_xp -= self.max_xp
            self.level += 1
            self.update_levels()

    def add_item_inventory(self, item):
        """Eng: check name
            Fr: sert à ajouter des items à l'inventaire"""
        self.inventory[item] = Object(item)
        if manager.Scene.sound:
            # inventory sound
            manager.Gui.add_item_sound.play()
        self.inventory_checked = False

    def fight(self, monster):
        """Eng: adds monster to dict
            Fr: conserver le monstre que le joueur va combattre"""
        self.is_fighting = Monster(monster)

    def attacking(self):
        """Eng: this function convert monster attacks and removes health from monster when player is attacking
            Fr: cette fonction enleve les HP du monstre quand le joueur l'attaque"""
        self.is_turn = False
        if self.attack < self.is_fighting.defence:
            self.health -= int((self.is_fighting.defence - self.attack)/2)
        else:
            self.is_fighting.health -= abs(self.attack - self.is_fighting.defence)
        if self.is_fighting.health < 1:
            self.combat, self.won = False, True
            self.get_fight_goods()
            self.level_up()

    def gameover(self):
        """Eng: end game
            Fr: termine le jeu"""
        manager.game.scenes['Game Over'].run_scene()

    def get_fight_goods(self):
        """Eng: get game items when you beat a monster
            Fr: C'est pour avoir les items après avoir gagner le combat contre un monstre"""
        self.gold += self.is_fighting.gold
        self.current_xp += self.is_fighting.xp_release
        self.add_item_inventory(self.is_fighting.item)

# create a player 
player = Player()

class Monster(Entity):
    monsters = {
        'wild dog' : {'name': 'Wild Dog', 'atk': 7, 'def': 4, 'level': 1, 'gold': 8, 'item': 'bone', 'run': False},
        'great snake': {'name': 'Great Snake', 'atk': 14, 'def': 1, 'level': 4, 'gold': 13, 'item': 'snake eye', 'run': True},
        'witch': {'name': 'The Witch', 'atk': 17, 'def': 11, 'level': 3, 'gold': 22, 'item': 'wand', 'run': False},
        'death claw': {'name': 'Death Claw', 'atk': 57, 'def': 25, 'level': 12, 'gold': 34, 'item': 'monster meat', 'run': False},
    }

    def __init__(self, name):
        for monster_key, monster in Monster.monsters.items():
            if monster_key == name:
                self.name = monster['name']
                self.item = monster['item']
                self.run = monster['run']
                self.xp_release = int(monster['level'] * random.randint(3, 7))

                super().__init__(monster['level'], monster['atk'], monster['def'], monster['gold'])
    
    def attacking(self):
        """Eng: deos same as function attack for player expet now its monster's turn
            Fr: fait exactement la meme chose que la fonction attack pour le joueur sauf ici le tour du monstre pour attacker"""
        if manager.Scene.sound and random.randint(0, 1):
            manager.Gui.hurt_sound.play()
        player.is_turn = True
        if self.attack < player.defence:
            self.health -= int((player.defence - self.attack)/2)
        else:
            player.health -= abs(self.attack - player.defence)
        if player.health < 1:
            player.gameover()

# loot items
class Object:
    items_list = {
        # Weapons
        # here you can only one equip one type of item ex you can equipe only on weapon and one shield
        'axe' : {'name' : 'Axe', 'atk' : 35, 'def' : 5, 'type' : 'weapon'},
        'bow' : {'name' : 'Bow', 'atk' : 55, 'def' : 0, 'type' : 'weapon'},
        'iron sword' : {'name' : 'Iron Sword', 'atk' : 38, 'def' : 10, 'type' : 'weapon'},
        'silver sword' : {'name' : 'Silver Sword', 'atk' : 49, 'def' : 15, 'type' : 'weapon'},
        'golden sword' : {'name' : 'Golden Sword', 'atk' : 90, 'def' : 30, 'type' : 'weapon'},
        'knife' : {'name' : 'Knife', 'atk' : 12, 'def' : 0, 'type' : 'weapon'},
        'pickaxe' : {'name' : 'Pickaxe', 'atk' : 24, 'def' : 3, 'type' : 'weapon'},
        'hammer' : {'name' : 'Hammer', 'atk' : 30, 'def' : 4, 'type' : 'weapon'},
        'torch' : {'name' : 'Torch', 'atk' : 20, 'def' : 30, 'type' : 'weapon'},
        'wand' : {'name' : 'Wand', 'atk' : 18, 'def' : 4, 'type' : 'weapon'},
        'great wand' : {'name' : 'Great Wand', 'atk' : 180, 'def' : 20, 'type' : 'weapon'},

        # shields
        'wooden shield' : {'name' : 'Wooden Shield', 'atk' : 0, 'def' : 40, 'type' : 'shield'},
        'iron shield' : {'name' : 'Iron Shield', 'atk' : 2, 'def' : 60, 'type' : 'shield'},
        'wooden armor' : {'name' : 'Wooden Armor', 'atk' : 0, 'def' : 50, 'type' : 'shield'},
        'iron armor' : {'name' : 'Iron Armor', 'atk' : 3, 'def' : 80, 'type' : 'shield'},
        'wizard hat' : {'name' : 'Wizard Hat', 'atk' : 7, 'def' : 6, 'type' : 'shield'},

        # materials
        'book' : {'name' : 'Book', 'value' : 5, 'type' : 'material'},
        'golden coin' : {'name' : 'Golden Coin', 'value' : 1, 'type' : 'material'},
        'golden key' : {'name' : 'Golden Key', 'value' : 10, 'type' : 'material'},
        'map' : {'name' : 'Map', 'value' : 3, 'type' : 'material'},
        'gear' :  {'name' : 'Gear', 'value' : 2, 'type' : 'material'},

        # Monster parts
        'bone' : {'name' : 'Bone', 'value' : 3, 'type' : 'material'},
        'monster meat' : {'name' : 'Monster Meat', 'value' : 8, 'type' : 'material'},
        'snake eye' : {'name' : 'Snake Eye', 'value' : 15, 'type' : 'material'},
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
                    self.status = 'Equip'
                elif self.type == 'potion' or self.type == 'food':
                    self.health = item['health']
                elif self.type == 'or' or self.type == 'material':
                    self.value = item['value']