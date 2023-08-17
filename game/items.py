import random

class Sword:
    swords = ['young sword', 'long sword', 'bamboo sword', 'golden sword', 'bloody sword']
    def __init__(self, name = random.choice(swords)):
        self.name = name
        self.property = random.randint(2,9)
        self.attack_value = self.property * 50

    def getProperties(self):
        """
        :return: The properties of the item
        """
        return f"Name: {self.name}, Value: +{self.property}, Attack Value: {self.attack_value}"


class Boots:
    boots = ['leather shoes', 'wooden shoes', 'golden shoes', 'bronze shoes', 'jade shoes']
    def __init__(self, name = random.choice(boots)):
        self.name = name
        self.property = random.randint(2,9)
        self.defence = self.property * 5
        self.max_hp = self.property * 10
        self.change_of_defense = random.randint(1, 15)

    def getProperties(self):
        """
        :return: The properties of the item
        """
        return f"Name: {self.name}, Value: +{self.property}, Defence: {self.defence}, Max HP: {self.max_hp}, Change of defense: {self.change_of_defense}"


class Helmet:
    helmets = ['traditional helmet', 'iron helmet', 'ghost helmet', 'fear helmet', 'dragon helmet']
    def __init__(self, name = random.choice(helmets)):
        self.name = name
        self.property = random.randint(2,9)
        self.defence = self.property * 5
        self.max_hp = self.property * 20

        self.change_of_defense = random.randint(1, 15)
        if self.property > 5:
            self.change_of_defense = random.randint(10,20)
        else:
            self.change_of_defense = random.randint(5,15)

    def getProperties(self):
        """
        :return: The properties of the item
        """
        return f"Name: {self.name}, Value: +{self.property}, Defence: {self.defence}, Max HP: {self.max_hp}, Change of defense: {self.change_of_defense}"


class Shield:
    shields = ['battle shield', 'pentagon shield', 'dragon shield', 'falcon shield', 'tiger shield']
    def __init__(self, name = random.choice(shields)):
        self.name = name
        self.property = random.randint(2,9)
        # helmet x5
        self.defence = self.property * 10
        self.max_hp = self.property * 100

    def getProperties(self):
        """
        :return: The properties of the item
        """
        return f"Name: {self.name}, Value: +{self.property}, Defence: {self.defence}, Max HP: {self.max_hp}"


class Armour:
    armours = ['iron plate armour', 'tiger plate armour', 'lion plate armour', 'dragon plate armour', 'gold plate armour']
    def __init__(self, name = random.choice(armours)):
        self.name = name
        self.property = random.randint(2,9)
        # helmet x10
        self.defence = self.property * 15
        self.max_hp = self.property * 200

        self.movement_speed = random.randint(1,15) * (-1)

    def getProperties(self):
        """
        :return: The properties of the item
        """
        return f"Name: {self.name}, Value: +{self.property}, Defence: {self.defence}, Max HP: {self.max_hp}, Movement Speed: {self.movement_speed}"


class nearItems:
    def __init__(self):
        self.nearItemsList = list()

        # Generate random number of items
        for i in range(random.randint(0,2)):
            swords = ['young sword', 'long sword', 'bamboo sword', 'golden sword', 'bloody sword']
            for s in range(random.randint(0,1)):
                sword = Sword(random.choice(swords))
                self.nearItemsList.append(sword)

            boots = ['leather shoes', 'wooden shoes', 'golden shoes', 'bronze shoes', 'jade shoes']
            for b in range(random.randint(0,1)):
                boot = Boots(random.choice(boots))
                self.nearItemsList.append(boot)

            helmets = ['traditional helmet', 'iron helmet', 'ghost helmet', 'fear helmet', 'dragon helmet']
            for h in range(random.randint(0,1)):
                helmet = Helmet(random.choice(helmets))
                self.nearItemsList.append(helmet)

            armours = ['iron plate armour', 'tiger plate armour', 'lion plate armour', 'dragon plate armour', 'gold plate armour']
            for a in range(random.randint(0,1)):
                armour = Armour(random.choice(armours))
                self.nearItemsList.append(armour)

            shields = ['battle shield', 'pentagon shield', 'dragon shield', 'falcon shield', 'tiger shield']
            for sh in range(random.randint(0,1)):
                shield = Shield(random.choice(shields))
                self.nearItemsList.append(shield)

