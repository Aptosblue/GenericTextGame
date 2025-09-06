print("Welcome to Pocket Aventure!\n")
name = input("What is your name? ")
class_types = ['warrior', 'archer', 'mage']
warrior_subclasses = ['fighter', 'tank', 'Paladin'] #placeholder names
archer_subclasses = ['hunter', 'deadeye', 'crossbowman'] #placeholder names
mage_subclasses = ['plasma', 'elemental', 'time'] #placeholder names
inventory = []
weight = 0
print(f"Hello, {name}, before we begin, you will need to choose a class.\nThe options are: Warrior, Archer, and Mage. \n")
player_class = str(input('What class do you choose? ')).lower()
while player_class not in class_types:
    print('That is not a valid class. Please choose again.')
    player_class = str(input('What class do you choose? '))

#Possibly make a class instead of a list/function for player classes
class Weapon:
    def __init__ (self, name, damage, weight):
        self.name = name
        self.damage = damage
        self.weight = weight

    def weapon_info(self):
        return f'Weapon: {self.name}\nDamage: {self.damage}\nWeight: {self.weight}'
    
        

Weapon.sword = Weapon('Sword', 10, 5)
Weapon.mace = Weapon('Mace', 10, 3)
Weapon.bow = Weapon('Bow', 10, 3)

def check_overburdened(weight): #incomplete function
    while weight > 100:
        print('You are overburdened! Please choose an item to remove from your inventory.')


if player_class == 'warrior':
    print('You have chosen the Warrior class! You may choose between Fighter, Tank, and Paladin as your subclass.')
    player_subclass = str(input('Which Warrior subclass do you choose? ')).lower()
    while player_subclass not in warrior_subclasses:
        print('That is not a valid subclass. Please choose again.')
        player_subclass = str(input('Which Warrior subclass do you choose? '))
    if player_subclass == 'fighter':
        print(f'You have chosen the {player_subclass.capitalize()} subclass for {player_class.capitalize()}!\n')
        print(f'You have received a {Weapon.sword.name} to start your adventure!\n')
        print(Weapon.sword.weapon_info())
        inventory.append(Weapon.sword)
        print(f'{Weapon.sword.name} added to inventory.')
        weight = weight + Weapon.sword.weight
        print(f'Current weight: {weight}')
    
        