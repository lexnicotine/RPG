import random, time


class Character:

    def __init__(self, name, strength, will, endo, exo, agi, intel, beau, cha):

        '''Description'''

        self.name = name

        '''Attributes'''

        self.strength = strength
        self.will = will
        self.endo = endo
        self.exo = exo
        self.agi = agi
        self.intel = intel
        self.beau = beau
        self.cha = cha

        self.might = self.strength + self.will
        self.magic = self.endo + self.exo
        self.speed = self.agi + self.intel
        self.social = self.beau + self.cha

        '''Stats'''

        self.hp = 10 + round(self.might / 10) + round(self.magic / 10) + round(self.speed / 20) + round(self.social / 20)
        self.mp = 10 + round(self.magic / 10) + round(self.will / 10) + round(self.intel / 10) + round(self.cha / 10)
        self.stamina = 10 + round(self.might / 10)

        self.attackbonus = round(self.might / 4) + round(self.speed / 2)
        self.damagebonus = round(self.might / 4) + round(self.speed / 8)
        self.defense = round(self.speed/2) + round(self.social/4)

        '''Level and Experience'''

        self.level = 1
        self.exp = 0
        '''Skills'''

        self.sword = 10
        self.weapon = 'gladius'
        self.inventory = []

    def gainexp(self, exp):

        self.exp += exp

class Enemy:

    def __init__(self, name, hp, mp, stamina, attack, defense, speed, slash, pierce, blud, damage, exp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stamina = stamina
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.slash = slash
        self.pierce = pierce
        self.blud = blud
        self.damage = damage
        self.exp = exp

def combat(char, enemy):

    fighting = True

    charinitiative = random.randint(1, 100) + char.speed
    enemyinitiative = random.randint(1, 100) + enemy.speed
    print(str(char.name) + ' Initiative: ' + str(charinitiative))
    time.sleep(2)
    print(str(enemy.name) + ' Initiative: ' + str(enemyinitiative))
    time.sleep(2)
    print()

    if enemyinitiative > charinitiative:
        enemyattack(enemy, char)
        if char.hp <= 0 or enemy.hp <= 0:
            return



    while fighting:
        command = input('Attack, Use Item, or Flee?').lower()
        print()

        if command == 'a':
            attack(char, enemy)
            if char.hp <= 0 or enemy.hp <= 0:
                char.gainexp(enemy.exp)
                return
            time.sleep(2)
            enemyattack(enemy, char)
            if char.hp <= 0 or enemy.hp <= 0:
                return

        elif command == 'u' or command == 'i':
            pass

        elif command == 'f':
            fighting = flee(char, enemy)
            if fighting == True:
                enemyattack(enemy, char)

        if char.hp <= 0 or enemy.hp <= 0:
            return


def attack(char, enemy):

    attackrating = char.attackbonus + round(char.sword * 2) + round(char.might / 2) + round(char.speed / 2)
    modattackrating = attackrating - enemy.defense
    damage = random.randint(2, 7) + char.damagebonus

    print(str(char.name) + ' Attacks!')
    print()
    time.sleep(2)
    print('Attack Rating: ' + str(attackrating))
    print('Modified Attack Rating: ' + str(modattackrating))
    attackroll = random.randint(1, 100)
    time.sleep(2)
    print('Attack Roll: ' + str(attackroll))
    time.sleep(2)
    print()

    if attackroll <= modattackrating:
        print('Hit!')
        time.sleep(2)
        print('Damage: ' + str(damage))
        print()
        enemy.hp -= damage
        time.sleep(2)

    else:
        print('Miss!')
        print()
        time.sleep(2)

    if enemy.hp <= 0:
        print('You killed the ' + enemy.name + '!')
        print()
        time.sleep(2)

def enemyattack(enemy, char):

    modattackrating = enemy.attack - char.defense

    print(str(enemy.name) + ' Attacks!')
    print()
    time.sleep(2)
    print(str(enemy.name) + ' Attack Rating: ' + str(modattackrating))
    attackroll = random.randint(1, 100)
    time.sleep(2)
    damage = random.randint(enemy.damage[0], enemy.damage[1])
    print('Attack Roll: ' + str(attackroll))
    time.sleep(2)
    print()

    if attackroll <= modattackrating:
        print('Hit!')
        time.sleep(2)
        print('Damage: ' + str(damage))
        char.hp -= damage
        print()
        time.sleep(2)

    else:
        print('Miss!')
        print()
        time.sleep(2)

    if char.hp <= 0:
        print(str(enemy.name) + ' has killed ' + str(char.name) + '!')
        print()
        time.sleep(2)

def flee(char, enemy):

    roll = random.randint(1, 100)
    fleechance = round(char.speed*2) - enemy.speed
    print('Chance to Flee: ' + str(fleechance))
    time.sleep(2)
    print('Roll: ' + str(roll))
    time.sleep(2)
    print()
    if roll <= fleechance:
        print('You got away.')
        print()
        return False
    else:
        print('You can\'t escape.')
        print()
        time.sleep(2)
        return True

def main(char):
    running = True

    while running:

        command = input('See Character, Generate Encounter, or Quit?: ').lower()
        print()
        if command == 'c':
            print('Name: ' + char.name)
            print('Level: ' + str(char.level))
            print('Experience: ' + str(char.exp))
            print()
            print('Might: ' + str(char.might))
            print('Magic: ' + str(char.magic))
            print('Speed: ' + str(char.speed))
            print('Social: ' + str(char.social))
            print()
            print('Strength: ' + str(char.strength))
            print('Willpower: ' + str(char.will))
            print('Endothurgy: ' + str(char.endo))
            print('Exothurgy: ' + str(char.exo))
            print('Agility: ' + str(char.agi))
            print('Intelligence: ' + str(char.intel))
            print('Beauty: ' + str(char.beau))
            print('Charisma: ' + str(char.cha))
            print()
            print('Hit Points: ' + str(char.hp))
            print('Magic Points: ' + str(char.mp))
            print('Stamina: ' + str(char.stamina))
            print()
            print('Attack Bonus: ' + str(char.attackbonus))
            print('Damage Bonus: ' + str(char.damagebonus))
            print('Defense: ' + str(char.defense))
            print()

        elif command == 'g' or command == 'e':
            enemy = Enemy('Goblin', 20, 0, 10, 50, 15, 25, 10, 5, 10, [5, 10], 25)
            combat(char, enemy)

        elif command == 'q':
            running = False

        else:
            continue





pc = Character('Pooper', 20, 10, 5, 5, 20, 5, 20, 15)
gobby = Enemy('Goblin', 20, 0, 10, 50, 15, 25, 10, 5, 10, [5, 10], 25)
main(pc)
