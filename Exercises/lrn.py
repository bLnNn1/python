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

def ex8():
    DB = dataBase("states.json")

    read = DB.readDataBase()

    country = input("In ce tara schimbati codurile? ")
    newCodeList = []

    for state in read['states']:
        if state['name'] == country:
            newCodeNumbers = input("Cate coduri adaugati? ")
            for i in range(1, int(newCodeNumbers)+1):
                newCode = input(f"Introduceti codul #{i}: ")
                newCodeList.append(newCode)
            state['area_codes'] = newCodeList

    print(newCodeList)

    DB.writeDataBase(read)

def ex9():
    DB = dataBase("states.json")

    read = DB.readDataBase()

    listaDictionare = []

    for state in read['states']:
        listaDictionare.append({state['name']:{"area_codes":state['area_codes']}})

    print(listaDictionare)

def ex10():
    listaDeListe = []
    nr = 10

    for i in range(0, nr, 3):
        if i+2 > nr:
            break
        else:
            lista = [i, i+1, i+2]
            listaDeListe.append(lista)

    print(listaDeListe)

