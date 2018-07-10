import random
import Player, Dungeon, Enemy

# Main
def main():
    name = input("Enter your characters name: ")
    hero = chooseClass(name)

    dungeon = Dungeon.Dungeon()

    dungeon.enterDungeon(hero)    

def createClass(role, name):
    if role == 'Mage':
        return Player.Mage(name)
    elif role == 'Warrior':
        return Player.Warrior(name)
    elif role == 'Archer':
        return Player.Archer(name)

def chooseClass(name):
    roles = ['Mage','Warrior','Archer' ]
    while True:
        for role in roles:
            choice = input("Is " + name + " a " + role + "? (Y/N): ")
            if choice == "Y":
                return createClass(role, name)

# Function calls
main()


# coding livestream
#  


