from items import *
import json
from dataBase import *

global DB
DB = dataBase("dataBase.json")

global read
read = DB.readDataBase()

class Player:
    def __init__(self, username):
        self.username = username
        self.nearItems = nearItems()

        self.sword = Sword()

        self.helmet = Helmet()
        self.armour = Armour()
        self.shield = Shield()
        self.boots = Boots()

        self.inventory = [self.sword, self.helmet, self.armour, self.shield, self.boots]


        self.equipped = {"helmet":None, "sword":None, "armour":None, "shield":None, "boots":None}

        self.hp = 100 + self.helmet.max_hp + self.armour.max_hp + self.shield.max_hp + self.boots.max_hp
        self.defence = 100 + self.helmet.defence + self.armour.defence + self.shield.defence + self.boots.defence
        self.attack_value = self.sword.attack_value

        # DATABASE
        read["Players"].append({"username": self.username, "inventory": self.get_inventory(), "equipped": self.get_equipped()})
        DB.writeDataBase(read)

    def attack(self, player):
        """
        This method is used to attack a player.
        :param player: - string - Player's name
        :return: Player's HP
        """
        # mai trb cooldown.. asta cand o sa fie buton
        if player.hp > 0:

            if player.defence > self.attack_value:
                damage = player.defence - self.attack_value
            else:
                damage = self.attack_value - player.defence

            player.hp = player.hp - damage
            return f"-{damage} HP to {player.username}"
        else:
            return f"{player.username} is already dead."
        # 1 attack = 1 click
        # cooldown

    def get_inventory(self):
        """
        :return: - list - the items from inventory
        """
        inventory = list()
        for item in self.inventory:
            inventory.append(item.name)
        return inventory

    def get_equipped(self):
        """
        :return: -list- equipped items
        """
        equipedList = list()
        for item in self.equipped.values():
            if item is not None:
                equipedList.append(item.name)

        return equipedList

    def equipItem(self, item):
        """
        This method is used to equip an item from inventory.
        :param item: - string - Item name.
        :return: None
        """

        flag = 0
        itemList = self.checkItem(item)
        if len(itemList) > 1:
            print(self.checkItem(item))
            choose = input(f"You have multiple {item}'s. Wich property do you choose to equip? (Value: +X / Defence: Y / etc.)\n")
            for it in itemList:
                if choose in it:
                    for itm in self.inventory:
                        if itm.name == item:
                            if choose in itm.getProperties():
                                if itm.name == item:
                                    if type(itm) == Helmet:
                                        if self.equipped["helmet"] is not None:
                                            self.inventory.append(self.equipped["helmet"])
                                        self.equipped["helmet"] = itm
                                    elif type(itm) == Sword:
                                        if self.equipped["sword"] is not None:
                                            self.inventory.append(self.equipped["sword"])
                                        self.equipped["sword"] = itm
                                    elif type(itm) == Armour:
                                        if self.equipped["armour"] is not None:
                                            self.inventory.append(self.equipped["armour"])
                                        self.equipped["armour"] = itm
                                    elif type(itm) == Shield:
                                        if self.equipped["shield"] is not None:
                                            self.inventory.append(self.equipped["shield"])
                                        self.equipped["shield"] = itm
                                    elif type(itm) == Boots:
                                        if self.equipped["boots"] is not None:
                                            self.inventory.append(self.equipped["boots"])
                                        self.equipped["boots"] = itm
                                    self.inventory.remove(itm)
                                    flag += 1
        elif len(itemList) == 1:
            for itm in self.inventory:
                if itm.name == item:
                    if type(itm) == Helmet:
                        if self.equipped["helmet"] is not None:
                            self.inventory.append(self.equipped["helmet"])
                        self.equipped["helmet"] = itm
                    elif type(itm) == Sword:
                        if self.equipped["sword"] is not None:
                            self.inventory.append(self.equipped["sword"])
                        self.equipped["sword"] = itm
                    elif type(itm) == Armour:
                        if self.equipped["armour"] is not None:
                            self.inventory.append(self.equipped["armour"])
                        self.equipped["armour"] = itm
                    elif type(itm) == Shield:
                        if self.equipped["shield"] is not None:
                            self.inventory.append(self.equipped["shield"])
                        self.equipped["shield"] = itm
                    elif type(itm) == Boots:
                        if self.equipped["boots"] is not None:
                            self.inventory.append(self.equipped["boots"])
                        self.equipped["boots"] = itm
                    self.inventory.remove(itm)
                    flag += 1
        else:
            print("Invalid option.")

        # DATABASE
        for player in read["Players"]:
            if player["username"] == self.username:
                player["equipped"] = self.get_equipped()
                player["inventory"] = self.get_inventory()

        DB.writeDataBase(read)

    #         flag = 0
    #         for itm in self.inventory:
    #             if itm.name == item:
    #                 if type(itm) == Helmet:
    #                     if self.equipped["helmet"] is not None:
    #                         self.inventory.append(self.equipped["helmet"])
    #                     self.equipped["helmet"] = itm
    #                 elif type(itm) == Sword:
    #                     if self.equipped["sword"] is not None:
    #                         self.inventory.append(self.equipped["sword"])
    #                     self.equipped["sword"] = itm
    #                 elif type(itm) == Armour:
    #                     if self.equipped["armour"] is not None:
    #                         self.inventory.append(self.equipped["armour"])
    #                     self.equipped["armour"] = itm
    #                 elif type(itm) == Shield:
    #                     if self.equipped["shield"] is not None:
    #                         self.inventory.append(self.equipped["shield"])
    #                     self.equipped["shield"] = itm
    #                 elif type(itm) == Boots:
    #                     if self.equipped["boots"] is not None:
    #                         self.inventory.append(self.equipped["boots"])
    #                     self.equipped["boots"] = itm
    #                 self.inventory.remove(itm)
    #                 flag += 1
    #         if flag == 0:
    #             print("You don't have this item in your inventory.")

    def takeOffItem(self, item):
        """
        This method is used to take off an equipped item to inventory.
        :param item: - string - Item name
        :return: None
        """

        for itm in self.equipped.values():
            if itm is not None:
                if itm.name == item:
                    self.inventory.append(itm)
                    self.equipType(itm)

        # DATABASE
        for player in read["Players"]:
            if player["username"] == self.username:
                player["equipped"] = self.get_equipped()
                player["inventory"] = self.get_inventory()

        DB.writeDataBase(read)

        # flag = 0
        # for itm in self.equipedDict.values():
        #     if itm is not None:
        #         if itm.name == item:
        #             for i in range(len(self.equipedDict)):
        #                 if list(self.equipedDict.values())[i] == self.equipedDict[list(self.equipedDict.keys())[i]]:
        #                     self.equipedDict[list(self.equipedDict.keys())[i]] = None
        #             self.inventory.append(itm)
        #             flag = 1
        #             break
        # if flag == 0:
        #     print("You don't have equiped this item.")

    def equipType(self, itm):
        """
        This method is used to check the type of an item.
        :param itm: - Helmet | Sword | Armour | Shield | Boots -
        :return: None
        """
        if type(itm) == Helmet:
            self.equipped["helmet"] = None
        elif type(itm) == Sword:
            self.equipped["sword"] = None
        elif type(itm) == Armour:
            self.equipped["armour"] = None
        elif type(itm) == Shield:
            self.equipped["shield"] = None
        elif type(itm) == Boots:
            self.equipped["boots"] = None

    def pickUpItem(self, item):
        """
        This method is used to pick up a near item.
        :param item: - string - Item name
        :return: None
        """
        for itm in self.nearItems.nearItemsList:
            if itm.name == item:
                self.inventory.append(itm)
                self.nearItems.nearItemsList.remove(itm)

        # DATABASE
        for player in read["Players"]:
            if player["username"] == self.username:
                player["inventory"] = self.get_inventory()

        DB.writeDataBase(read)

    def getNearItems(self):
        """
        :return: - list - The names of near items.
        """
        itms = list()

        for item in self.nearItems.nearItemsList:
            itms.append(item.name)

        return itms

    def move(self, meters):
        """
        This method is used to get new near items. The player needs to move minimum 5 meters.
        :param meters: - int - Number of meters.
        :return: None
        """
        print(f"{self.username} is moving {meters} meters.")
        if meters >= 5:
            self.nearItems = nearItems()

    def checkItem(self, item):
        """
        :param item: - string - Item name
        :return: - list - Details about an item from inventory or equipped items.
        """
        itmList = list()
        item = item.lower()

        for itm in self.inventory:
            if itm.name == item:
                itmList.append(itm.getProperties())

        for itm in self.equipped.values():
            if itm is not None:
                if itm.name == item:
                    itmList.append(itm.getProperties())

        if len(itmList) == 0:
            return "Item not found."
        else:
            return itmList

    def drop_item(self, item):
        """
        This method is used to drop an item from your inventory or your equipped items.
        :param item: - string - Item name
        :return: None
        """
        itemList = self.checkItem(item)
        if len(itemList) > 1 and type(itemList) == list:
            print(self.checkItem(item))
            choose = input(f"You have multiple {item}'s. Wich property do you choose to drop? (Value: +X / Defence: Y / etc.)\n")
            for it in itemList:
                if choose in it:
                    for itm in self.inventory:
                        if itm.name == item:
                            if choose in itm.getProperties():
                                self.nearItems.nearItemsList.append(itm)
                                self.inventory.remove(itm)

                    for itm in self.equipped.values():
                        if itm is not None:
                            if itm.name == item:
                                if choose in itm.getProperties():
                                    self.nearItems.nearItemsList.append(itm)
                                    self.equipType(itm)
        elif len(itemList) == 1 and type(itemList) == list:
            for itm in self.inventory:
                if itm.name == item:
                    self.nearItems.nearItemsList.append(itm)
                    self.inventory.remove(itm)

            for itm in self.equipped.values():
                if itm is not None:
                    if itm.name == item:
                        self.nearItems.nearItemsList.append(itm)
                        self.equipType(itm)
        else:
            print("Item not found.")

        # DATABASE
        for player in read["Players"]:
            if player["username"] == self.username:
                player["equipped"] = self.get_equipped()
                player["inventory"] = self.get_inventory()

        DB.writeDataBase(read)