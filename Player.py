import re 
import random

class Player:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.intellect = 10
        self.level = 1
        self.strength = 10
        self.actionRE = self.compileActionRE()
        self.isAlive = True

    def rollDice(self):
        return random.randint(1,6)

    def takeDamage(self,damage):
        if self.health - damage <= 0:
            self.health = 0
            print(self.name + " has died")
            self.kill()
        else:
            self.health = self.health - damage

    # heal()
    def healSelf(self,heal):
        self.health = self.health + heal


    # attk(i) / attk(s)
    def strengthAttack(self,roll, enemy):
        damageDealt = roll * self.strength
        enemy.takeDamage(damageDealt)
        return damageDealt

    def intellectAttack(self,roll, Enemy):
        damageDealt = roll * self.intellect
        Enemy.takeDamage(damageDealt)
        return damageDealt

    def getHealth(self):
        return self.health

    # returns the enemy to battle based on index entered
    def chooseEnemy(self):
        enemy_choice = int(input("Which enemy do you want to battle?: "))
        return enemy_choice
        
    # compile the actions regular expressions into one list, probably a better way heh
    def compileActionRE(self):
        actions = [r'atk\(',r'heal\(']
        actionsRE = []
        for action in actions:
            actionsRE.append(re.compile(action, re.I))
        return actionsRE
    
    def takeTurn(self, enemy):
        turnOver = False
        while not turnOver:
            action = input("What are you going to do?: ")
            for actRE in self.actionRE:
                match = actRE.match(action)
                if match is not None:
                    roll = self.rollDice()
                    if action[match.end():] == 'i)':
                        print("You rolled a " + str(roll) + " and dealt " + str(self.intellectAttack(roll,enemy)) + " damage.")
                        turnOver = True
                    elif action[match.end():] == 's)':
                        print("You rolled a " + str(roll) + " and dealt " + str(self.strengthAttack(roll,enemy)) + " damage.")
                        turnOver = True
                    elif match.group() == 'heal(':
                        print("You healed yourself 15 hp")
                        self.healSelf(15)
                        turnOver = True
    
    def getExistance(self):
        return self.isAlive
    def kill(self):
        self.isAlive = False


class Mage(Player):
    def __init__(self,name):
        Player.__init__(self,name)
        self.intellect = 25

class Warrior(Player):
	def __init__(self,name):
		Player.__init__(self,name)
		self.strength = 25

class Archer(Player):
	def __init__(self,name):
		Player.__init__(self,name)
		self.intellect = 17
		self.strength = 17