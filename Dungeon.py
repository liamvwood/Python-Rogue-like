import Player
import Enemy
import random

class Dungeon:
    def __init__(self):
        self.number_of_rooms = random.randint(1,10)
        self.rooms = self.generateRooms()

    def __str__(self):
        return "This dungeon has " + str(self.number_of_rooms) + " rooms."

    def generateRooms(self):
        rooms = []
        for i in range(self.number_of_rooms):
            room = Room(i)
            for j in range(room.number_of_enemies):
                rand = random.randint(0,1)
                if rand == 0:
                    room.enemies.append(Enemy.Bat())
                else:
                    room.enemies.append(Enemy.Zombie())
            rooms.append(room)
        return rooms

    def enterDungeon(self,hero):
        print(self.__str__())
        for room in self.rooms:
            print(room)
            room.startRoomBattle(hero)

class Room:
    def __init__(self, room_number):
        self.number_of_enemies = random.randint(1,3)
        self.enemies = []
        self.room_number = room_number

    def __str__(self):
        output = f"The enemies in room {self.room_number} are:"
        count = 0
        for enemy in self.enemies:
            output = f'{output} \n{count} {str(enemy)}'
            count = count + 1
        return output
    
    def startRoomBattle(self, hero):
        battleOver = False
        enemy_choice = 0
        while not battleOver:
            enemy_choice = hero.chooseEnemy()
            self.startEnemyBattle(hero, self.enemies[enemy_choice])
            self.enemies.pop(enemy_choice)
            if len(self.enemies) == 0:
                print(f"{hero.name} has conquered room {self.room_number}\nMoving onto room {self.room_number + 1}")
                battleOver = True
            else:
                print(self)

    def startEnemyBattle(self,hero,enemy):
        battleOver = False
        while not battleOver:
            if not self.checkHealths(hero,enemy):
                if hero.getExistance():
                    hero.takeTurn(enemy)
                if enemy.getExistance():
                    enemy.takeTurn(hero)
            else:
                battleOver = True
        return battleOver

    def getEnemies(self):
        return self.enemies

    def checkHealths(self,hero,enemy):
        print(f"{hero.name} has {hero.getHealth()} health and {enemy} has {enemy.getHealth()} health")
        if not hero.getExistance():
            return True
        elif not enemy.getExistance():
            return True
        return False
        