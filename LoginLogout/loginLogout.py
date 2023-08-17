import json

def writeFile(newInfo):
    with open("database.json", "w") as f:
        json.dump(newInfo, f, indent=2)

def readFile():
    with open("database.json") as f:
        data = json.load(f)
    return data

inregistrat = {}

def creareCont():
    global inregistrat
    if len(inregistrat) == 0:
        name = input("Introduceti numele: ")
        password = input("Introduceti parola: ")
        date = {name:password}
        checkCont = 0

        with open("database.json") as f:
            database = json.load(f)

        for cont in database["oameni"]:
            if name in cont:
                checkCont = 1

        if checkCont != 0:
                print("Contul deja exista.")
        else:
            database["oameni"].append(date)
            print("Contul a fost creat cu succes.")

        writeFile(database)
    else:
        print("Nu puteti face un cont nou cand sunteti logat.")

def login():
    global inregistrat
    if len(inregistrat) == 0:
        name = input("Introduceti numele: ")
        password = input("Introduceti parola: ")
        date = {name:password}
        flag = 0

        with open("database.json") as f:
            database = json.load(f)

        for cont in database["oameni"]:
            if cont == date:
                print("V-ati logat cu succes.")
                flag = 1
                inregistrat = {name: password}

        if flag == 0:
            print("Numele sau parola incorecte.")
    else:
        print("Sunteti deja logat.")


def stergeCont():
    # login
    print("Trebuie sa scrieti datele contului pentru a putea sterge contul.")
    name = input("Introduceti numele: ")
    password = input("Introduceti parola: ")
    date = {name: password}
    flag = 0

    with open("database.json") as f:
        database = json.load(f)

    for cont in database["oameni"]:
        if cont == date:
            flag = 1

    if flag == 0:
        print("Numele sau parola incorecte.")

    global inregistrat
    inregistrat = {name: password}

    # Logat^

    # Stergere cont
    for cont in database["oameni"]:
        if cont == date:
            database["oameni"].remove(cont)
            print("Contul a fost sters cu succes.")
            inregistrat = {}

    writeFile(database)

def logout():
    if len(inregistrat) != 0:
        inregistrat.clear()
        print("Ati iesit din cont.")
    else:
        print("Nu sunteti logat.")


act = 0
print("Bine ati venit.")

while(act == 0):
    print("\nAlegeti o actiune.\n1. Creare cont\n2. Login\n3. Sterge cont\n4. Logout\n5. Inchide aplicatia")
    rasp = input()
    if rasp == "1":
        creareCont()
    elif rasp == "2":
        login()
    elif rasp == "3":
        stergeCont()
    elif rasp == "4":
        logout()
    elif rasp == "5":
        act = 1
        print("O zi buna.")
    else:
        print("Alegeti o varianta corecta.")


# def stergeCont():
#     name = "crissy"
#     password = "gggi"
#     date = {name: password}
#
#     with open("database.json") as f:
#         database = json.load(f)
#
#     for cont in database["oameni"]:
#         if cont == date:
#             database["oameni"].remove(cont)
#             print("contu a fost sters cu succes")
#
#     writeFile(database)