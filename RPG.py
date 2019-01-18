import random


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

        '''Level and Experience'''

        self.level = 1
        self.exp = 0
        '''Skills'''

        self.sword = 10

        self.inventory = []

    def attack(self, enemy):

        attackrating = self.attackbonus + round(self.sword * 2) + round(self.might / 2) + round(self.speed / 2)
        modattackrating = attackrating - enemy.defense
        damage = random.randint(2, 7) + self.damagebonus

        print('Attack Rating: ' + str(attackrating))
        print('Modified Attack Rating: ' + str(modattackrating))
        attackroll = random.randint(1, 100)
        print('Attack Roll: ' + str(attackroll))

        if attackroll <= modattackrating:
            print('Hit!')
            print('Damage: ' + str(damage))
            enemy.hp -= damage

        else:
            print('Miss!')

        if enemy.hp <= 0:
            print('You killed the ' + enemy.name + '!')


class Enemy:

    def __init__(self, name, hp, mp, stamina, attack, defense, slash, pierce, blud, damage):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stamina = stamina
        self.attack = attack
        self.defense = defense
        self.slash = slash
        self.pierce = pierce
        self.blud = blud
        self.damage = damage


def main(char):
    running = True

    while running:

        command = input('See Character, Generate Encounter, or Quit?: ').lower()
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

        elif command == 'g' or command == 'e':
            pass

        elif command == 'q':
            running = False

        else:
            continue


##while gobby.hp > 0:
##
##    command = input('Attack: ').lower()
##    if command == 'a':
##        pc.attack(gobby)
##    else:
##        continue


pc = Character('Pooper', 20, 10, 5, 5, 20, 5, 20, 15)
gobby = Enemy('Goblin', 20, 0, 10, 50, 15, 10, 5, 10, [5, 10])
main(pc)
