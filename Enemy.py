import random
class Enemy:
    def __init__(self):
        self.health = 100
        self.attackDamage = 15
        self.difficulty = 1
        self.isAlive = True
    def takeDamage(self,damage):
        if self.health - damage <= 0:
            self.health = 0
            print(f"{self} has been defeated")
            self.kill()
        else:
            self.health = self.health - damage
    def getHealth(self):
        return self.health
    def attack(self,hero):
        damageDealt = int(self.attackDamage * self.difficulty * random.uniform(0.5,1))
        print(f'{self} dealt {damageDealt} to {hero.name}')
        hero.takeDamage(damageDealt)
    def takeTurn(self,hero):
        self.attack(hero)
    def kill(self):
        self.isAlive = False
    def getExistance(self):
        return self.isAlive

class Bat(Enemy):
    def __init__(self):
        Enemy.__init__(self)
    def __str__(self):        
        return "Bat"

class Zombie(Enemy):
    def __init__(self):
        Enemy.__init__(self)
    def __str__(self):        
        return "Zombie"

class Cyclops(Enemy):
    # Shoots lasers out of its eye
    def __init__(self):
        Enemy.__init__(self)
        self.health = 150
        self.difficulty = 3
    def __str__(self):        
        return "Cyclops"