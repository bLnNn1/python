import json

class dataBase:
    def __init__(self, path):
        self.path = path

    def readDataBase(self):
        """
        This method is used to read the whole data base.
        :return: dictFromJson - dict object that represents the whole data base
        """
        with open(self.path, "r") as file:
            dictFromJson = json.load(file)
        return dictFromJson

    def writeDataBase(self, newInfo):
        """
        This method is used to write the data base.
        First, you modify the exact data that you want modified and when you write the data base,
        you have to input the whole new data base.
        :param newInfo: - dict - the new data base.
        :return: None
        """
        with open(self.path, "w") as file:
            json.dump(newInfo, file, indent=4)