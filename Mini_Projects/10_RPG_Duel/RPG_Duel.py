class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.inventory = []

    def add_to_inventory(self, item):
        print(f'Adding {item} to inventory {self.name}.')
        self.inventory.append(item)
        self.attack += 5
        self.hp += 5

    def remove_from_inventory(self, item):
        if item not in self.inventory:
            print(f'Item {item} not in inventory.')
            return

        print(f'Removing {item} from inventory {self.name}.')
        self.inventory.remove(item)
        self.attack -= 5
        self.hp -= 5

    def show_inventory(self):
        print(f'\n=== {self.name} inventory ===')
        if not self.inventory:
            print(f'Inventory is empty.')
            return

        for item in self.inventory:
            print(item)

    def show_characteristics(self):
        print(f'\n~~~ Characteristics of {self.name} ~~~')
        print(f'Attack - {self.attack}\nHP - {self.hp}\n')

class RPGSystem:
    def battle(self, person1, person2):
        while True:
            person2.hp -= person1.attack

            if person2.hp <= 0:
                if person2.hp < 0:
                    person2.hp = 0
                break

            person1.hp -= person2.attack

            if person1.hp <= 0 :
                if person1.hp < 0:
                    person1.hp = 0
                break

        if person1.hp > 0:
            print(f'{person1.name} win!')
        else:
            print(f'{person2.name} win!')

        print(f'\nCharacters status after battle:\n {person1.name} - {person1.hp} HP\n {person2.name} - {person2.hp} HP')

rpg_system = RPGSystem()

character1 = Character('Warrior', 100, 10)
character2 = Character('Monster', 100, 15)

character1.add_to_inventory('Sword')
character1.add_to_inventory('Shield')

character1.show_inventory()
character1.show_characteristics()

character2.show_characteristics()

rpg_system.battle(character1, character2)
