# [Dictionare] 1. Scrie un dictionar in care sa ai 3 camere ca si chei
# (Baie, Bucatarie, Dormitor) si ca valori pentru fiecare cheie,
# o lista cu 3 obiecte din fiecare camera.
# Exercitiu: Printeaza toate obiectele unul sub altul.

# dictionar = {"Baie":["chiuveta","wc","cada"], "Bucatarie":["lingura", "furculita", "farfurie"],
# "Dormitor":["pat", "pc", "laptop"]}
#
# lista = [1,2,3,4,5]
#
# for camera in dictionar.keys():
#     for obiect in dictionar[camera]:
#         print(obiect)

# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# alt exercitiu
# listaDeListe = [[0, 1, 6], [3, 4, 5], [6, 7, 8]]
#
# for lista in listaDeListe:
#     for nr in range(0, len(lista)):
#         if lista[nr] == 6:
#             lista[nr] = "Andrei"
# print(listaDeListe)

def ex2(word):
    # 2. Scrie un program care sa genereze un dictionar in care sa se contorizeze numarul de litere dintr-o propozitie (un string).
    dictionar = {}

    for letter in word:
        flag: int = 0
        for repeat in word:
            if letter == repeat:
                flag = flag + 1
            dictionar.update({letter: flag})
    #or     dictionar[letter] = flag
    print(dictionar)


def ex3():
    oameni = {'oameni':
        [
            {'nume': 'Gheorghe',
             'prenume': 'Gabriel',
             'inaltime': 170,
             'varsta': 23},
            {'nume': 'Despa',
             'prenume': 'Gabriel',
             'inaltime': 165,
             'varsta': 45},
            {'nume': 'Marin',
             'prenume': 'Andrei',
             'inaltime': 185,
             'varsta': 18},
            {'nume': 'Despa',
             'prenume': 'Andrei',
             'inaltime': 168,
             'varsta': 25},
            {'nume': 'Marin',
             'prenume': 'Gabriel',
             'inaltime': 210,
             'varsta': 68},
            {'nume': 'Gheorghe',
             'prenume': 'Ion',
             'inaltime': 173,
             'varsta': 52},
            {'nume': 'Moga',
             'prenume': 'Gabriel',
             'inaltime': 163,
             'varsta': 31},
            {'nume': 'Moga',
             'prenume': 'Liviu',
             'inaltime': 186,
             'varsta': 33},
            {'nume': 'Gheorghe',
             'prenume': 'Liviu',
             'inaltime': 192,
             'varsta': 28},
            {'nume': 'Despa',
             'prenume': 'Ion',
             'inaltime': 177,
             'varsta': 39},
        ]
    }
    # a. Scrie o functie care sa puna intr-o lista, toate varstele
    listaVarste = []

    for om in oameni.get('oameni'):
        listaVarste.append(om.get('varsta'))

    print("Varstele sunt " + str(listaVarste))

    # b. Scrie o functie care sa calculeze varsta medie din lista de mai sus
    varstaTotala = 0
    for varsta in listaVarste:
        varstaTotala = varstaTotala + varsta

    varstaMedie = varstaTotala / len(listaVarste)
    print("Varsta medie este: " + str(varstaMedie))

    # c. Scrie o functie care sa calculeze inaltimea medie
    listaInaltime = []
    for om in oameni.get('oameni'):
        listaInaltime.append(om.get('inaltime'))

    inaltimeTotala = 0
    for inaltime in listaInaltime:
        inaltimeTotala = inaltimeTotala + inaltime

    inaltimeMedie = inaltimeTotala / len(listaInaltime)
    print("Inaltimea medie este: " + str(inaltimeMedie))

    # d. Scrie o functie care sa gaseasca cea mai mare varsta si cea mai mare inaltime
    varstaMaxima = max(listaVarste)
    # maxVarsta = 0
    # for varsta in range(len(listaVarste)-1):
    #     if varsta == len(listaVarste)-1:
    #         break
    #     else:
    #         if listaVarste[varsta] > listaVarste[varsta+1]:
    #             maxVarsta = listaVarste[varsta]
    # print(maxVarsta)
    inaltimeMaxima = max(listaInaltime)
    print("Varsta maxima este: " + str(varstaMaxima) + "\nInaltimea maxima: " + str(inaltimeMaxima))

    # e. Scrie o functie care sa gaseasca numele persoanei cu cea mai mare inaltime.
    print(listaInaltime)
    persoana = ''
    for inaltime in range(len(listaInaltime)):
        if listaInaltime[inaltime] == inaltimeMaxima:
            persoana = inaltime
    print(persoana)

    xPersoana = oameni['oameni'][persoana]
    numePersoana = xPersoana['nume']
    prenumePersoana = xPersoana['prenume']
    print("Cea mai inalta persoana este " + numePersoana + " " + prenumePersoana)


def ex3fresh():
    oameni = {'oameni':
        [
            {'nume': 'Gheorghe',
             'prenume': 'Gabriel',
             'inaltime': 170,
             'varsta': 23},
            {'nume': 'Despa',
             'prenume': 'Gabriel',
             'inaltime': 165,
             'varsta': 45},
            {'nume': 'Marin',
             'prenume': 'Andrei',
             'inaltime': 185,
             'varsta': 18},
            {'nume': 'Despa',
             'prenume': 'Andrei',
             'inaltime': 168,
             'varsta': 25},
            {'nume': 'Marin',
             'prenume': 'Gabriel',
             'inaltime': 210,
             'varsta': 68},
            {'nume': 'Gheorghe',
             'prenume': 'Ion',
             'inaltime': 173,
             'varsta': 52},
            {'nume': 'Moga',
             'prenume': 'Gabriel',
             'inaltime': 163,
             'varsta': 31},
            {'nume': 'Moga',
             'prenume': 'Liviu',
             'inaltime': 186,
             'varsta': 33},
            {'nume': 'Gheorghe',
             'prenume': 'Liviu',
             'inaltime': 192,
             'varsta': 28},
            {'nume': 'Despa',
             'prenume': 'Ion',
             'inaltime': 177,
             'varsta': 39},
        ]
    }

    # a. Scrie o functie care sa puna intr-o lista, toate varstele
    listaVarste = list()
    for om in oameni['oameni']:
        listaVarste.append(om['varsta'])

    # b. Scrie o functie care sa calculeze varsta medie din lista de mai sus
    varstaMedie = 0
    varste = 0

    for varsta in listaVarste:
        varste += varsta

    varstaMedie = varste / len(listaVarste)

    # d. Scrie o functie care sa gaseasca cea mai mare varsta
    varstaMax = 0
    for varsta in listaVarste:
        if varstaMax < varsta:
            varstaMax = varsta

    # e. Scrie o functie care sa gaseasca numele persoanei cu cea mai mare inaltime.
    for om in oameni['oameni']:
        if om['varsta'] == varstaMax:
            print(f"Cea mai inalta persoana este {om['nume']} {om['prenume']}.")
            break

    for om in oameni['oameni']:
        print(om)


def ex4(num1, num2):
    return num1 + num2


# print(ex4(5, 10) + ex4(12, -5) + ex4(16, 32))

def ex5():
    # 5. Scrie doua functii (get si set) pe care sa le poti aplica pe dictionarul asta: listaInformatii= [{"inaltime": 150}, {"inaltime": 170}, {"inaltime": 185}]. 
    # Spre exemplu: cu set-ul sa poti seta o inaltimea unei persoane din dictionarul respectiv iar cu get-ul sa poti lua inaltimea unei persoane specifice
    listaInformatii = [{"Alex": 150},
                       {"Geroge": 170},
                       {"Cristi": 185}]

    nume = "Alex"
    inaltime = 133

    def get(nume):
        for om in range(len(listaInformatii)):
            if listaInformatii[om].__contains__(nume):
                return str(listaInformatii[om][nume])
            return "Persoana nu exista."

    def set(nume, inaltime):
        flag = 0
        for om in range(len(listaInformatii)):
            if listaInformatii[om].__contains__(nume):
                listaInformatii[om][nume] = inaltime
                flag = 1
        if flag == 0:
            print("Persoana nu exista.")

    listaInformatii = [{"Alex": 150},
                       {"Geroge": 170},
                       {"Cristi": 185}]

    nume = "Alex"
    inaltime = 133

    def get(nume):
        for om in range(len(listaInformatii)):
            if listaInformatii[om].__contains__(nume):
                return str(listaInformatii[om][nume])
            return "Persoana nu exista."

    def set(nume, inaltime):
        flag = 0
        for om in range(len(listaInformatii)):
            if listaInformatii[om].__contains__(nume):
                listaInformatii[om][nume] = inaltime
                flag = 1
        if flag == 0:
            print("Persoana nu exista.")


def ex5fresh():
    # [Functii] 5. Scrie doua functii (get si set) pe care sa le poti aplica pe dictionarul asta.
    # Spre exemplu: cu set-ul sa poti seta o inaltimea unei persoane din dictionarul respectiv iar cu get-ul sa poti lua
    # inaltimea unei persoane specifice.

    listaInformatii = [{"Alex": 150},
                       {"Dante": 170},
                       {"Andrei": 185}]

    for i in range(len(listaInformatii)):
        print(listaInformatii[i])

    def setInaltime(nume, inaltime):
        flag = 0
        for i in range(len(listaInformatii)):
            if nume in listaInformatii[i]:
                listaInformatii[i][nume] = inaltime
                flag = 1
                break
        if flag == 0:
            print("Numele nu exista.")

    def getInaltime(nume):
        for i in range(len(listaInformatii)):
            if nume in listaInformatii[i]:
                return f"Inaltimea lui {nume} este {listaInformatii[i][nume]}."
        return "Numele nu exista."

    setInaltime("Alex", 120)
    print()

    print(getInaltime("Alex"))


def ex6():
    def ex6var1():
        cuvant = "andrei"
        for litera in range(len(cuvant)):
            print(str(litera) + " " + str(cuvant[litera]))

    def ex6var2(cuvant, index):
        return str(cuvant[index]) + " " + str(index)

    def ex6final():
        # 6. Scrie o functie care sa printeze indexul unei litere si litera de pe un string ca exemplu
        string = "asfkjqlkwjfqawifoqnavlkmnlvanLANaSLFKaQWLaFKQaJLflaakjsflqkjfsfq"
        litera = "a"
        indexList = []

        for i in range(len(string)):
            if string[i] == litera:
                indexList.append(i)

        print(f"Litera {litera} se afla pe indexul: {indexList}")


def ex7():
    # 7. Scrie o functie cu care sa adaugi iteme in inventarul dictionarInventar si o functie cu care sa scoti iteme din inventar. Trebuie sa alegi itemul si pozitia. Exemple functii: daJosItem(item), puneItem(pozitia, item). Dictionarul: dictionarInventar = {"coif": "", "armura": "", "pantaloni": "", "bocanci": ""}
    inventar = {}

    def addItem(item: str, number=1):
        inventar[item] = number

    def removeItem(item: str, number=0):
        if number <= inventar[item]:
            if number != 0:
                inventar[item] = inventar[item] - number
            else:
                inventar.pop(item)
        else:
            print("Numar prea mare de iteme!")


import json


def ex8a():
    #  8. Scrie o functie care sa modifice 'area_codes' din fisierul .json cu un input de la user, si o functie care sa incarce fisierul json intr-un dictionar de python.
    with open('states.json') as f:
        data = json.load(f)

    for state in data["states"]:
        print(state)

    country = input("In ce tara doriti sa schimbati codurile? ")
    newCode = []

    for state in data["states"]:
        if country == state["name"]:
            nr = int(input("Cate coduri doriti? "))
            for i in range(nr):
                newCode.append(input("Introduceti codul: "))
            state["area_codes"] = newCode

    for state in data["states"]:
        print(state)

    with open("states.json", "w") as f:
        json.dump(data, f, indent=2)


def ex8b():
    with open("states.json") as f:
        dictionar = json.load(f)

    print(dictionar)


def ex9():
    # 9. Scrie un program care sa ia dictionarul din fisierul json states.json si sa genereze o lista de dictionare de forma: 
    #  [{"Arkansas": {"area_codes": ["479", "501", "870"]}}, {"Arizona": {"area_codes": ["480", "520", "602", "623", "928"]}}] dar pentru toate statele
    with open("states.json") as f:
        dictionar = json.load(f)

    dictList = []

    for stat in dictionar["states"]:
        newDict = {}
        # print(str(stat["name"]) + " " + str(stat["area_codes"]))
        newDict[stat["name"]] = {"area_codes": stat["area_codes"]}
        dictList.append(newDict)

    print(dictList)


def ex10():
    # 10. Scrie un program care sa transforme range-ul urmator: range(0, 10) intr-o lista de liste. 
    # Expected result: [[0, 1, 2], [3, 4, 5], [6, 7, 8]] 
    listaDeListe = []
    flag = 0

    for i in range(0, 3):
        lista = []
        for j in range(flag, 10):
            if len(lista) < 3:
                lista.append(j)
            else:
                flag = flag+3
                break
        listaDeListe.append(lista)
    print(listaDeListe)


def ex11():
    # 11. Scrie un program care sa printeze primele 20 de numere din secventa Fibonacci (Expected result: 0  1  1  2  3  5  8  13  21  34)
    a = 0
    b = 0
    c = 1
    d = 20

    for i in range(0, d):
        print(a)
        a = b + c
        c = b
        b = a

def ex12():
    # 12. Scrie o functie care sa calculeze suma dintr-un range de numere (range(0, 50) daca numerele sunt divizibile cu 3, si sa returneze suma respectiva.
    suma = 0
    for i in range(0,50):
        if i % 3 == 0:
            suma = suma + i

    return suma

def ex13(*args):
    # 13. Scrie o functie care sa calculeze aria unui dreptunghi, functia trebuie sa accepte si lungime si latime, dar latimea sa aibe deja o valoare default (Spre exemplu 20). La final functia trebuie sa returneze aria respectiva.
    if len(args) == 1 and isinstance(args[0], int):
        return "Aria dreptunghiului cu lungimea " + str(args[0]) + " si latimea 20 este " + str(args[0]*20)
    elif len(args) == 2 and isinstance(args[1], int):
        return "Aria dreptunghiului cu lungimea " + str(args[0]) + " si latimea " + str(args[1]) + " este " + str(args[0]*args[1])

def ex14(*args):
    # 14. Scrie o functie care sa calculeze perimetrul unui dreptunghi, similar ca la exercitiul 13, functia trebuie sa accepte lungime si latime, dar de data asta, latimea trebuie sa aibe o valoare default (Spre exemplu 20). La final functia trebuie sa returneze perimetrul calculat.
    if len(args) == 1 and isinstance(args[0], int):
        return "Perimetrul dreptunghiului cu lungimea " + str(args[0]) + " si latimea 20 este " + str(2*(args[0]+20))
    elif len(args) == 2 and isinstance(args[1], int):
        return "Perimetrul dreptunghiului cu lungimea " + str(args[0]) + " si latimea " + str(args[1]) + " este " + str(2*(args[0]+args[1]))


def ex15():
    #   Creeaza o clasa (clasa om), cu cel putin 3 argumente, si 2 metode (functii) pe care orice obiect din clasa om sa le faca
    # (exemplu: sa mearga si sa citeasca o carte).
    #   Bonus: unul dintre argumente sa tina cont de cate carti a citit si dupa fiecare apelare a metodei "citesteOCarte" acest
    # argument sa se incrementeze cu 1.
    class Om:
        def __init__(self, nume, prenume, varsta):
            self.nume = nume
            self.prenume = prenume
            self.varsta = varsta
            self.citite = 0

        def walk(self):
            print(f"{self.nume} {self.prenume} merge.")

        def read(self):
            self.citite = self.citite + 1
            print(f"{self.prenume} citeste o carte. Are {self.citite} carti citite.")

    om = Om("Balan", "Andrei", 22)

    om.read()
    om.read()
    om.read()


def ex16():
    #   Bazat pe clasa creata la exercitiul 15, creeaza clasa carte, si in loc de carti citite, modifica in pagini citite si
    # modifica metoda de citit carti intr-o metoda care sa tina cont de cate pagini sunt citite in functie de fiecare carte.
    #   Exemplu narativ: Un om citeste o carte cu 50 de pagini, dupa ce a citit-o are un numar de 50 de pagini citite.
    # Daca acelasi om citeste o alta carte cu 75 de pagini, va avea un numar de 125 de pagini citite. Transpune exemplul asta in cod.

    class Carte:
        def __init__(self, nume, prenume, varsta):
            self.nume = nume
            self.prenume = prenume
            self.varsta = varsta
            self.paginiCitite = 0

        def citeste(self, pagini):
            self.paginiCitite += pagini
            print(f"{self.prenume} are {self.paginiCitite} pagini citite.")

    cititor = Carte("Bln", "Andrei", 22)

    cititor.citeste(50)
    cititor.citeste(75)


def ex17():
    #   Creeaza o clasa bidon in care sa ti cont de cati litri poate avea bidonul respectiv si cati litri de lichid are deja in el.
    #   Pe langa asta, fa si doua metode, una de adaugat lichid in bidon si una de scos lichid din bidon (Tine cont de faptul ca din
    # bindon nu poti scoate mai multi litri de lichid decat ai deja in acel bidon)
    class Bidon:
        def __init__(self, cantitate, capacitate):
            self.capacitate = capacitate
            self.cantitate = cantitate

        def adauga(self, litri):
            if litri + self.cantitate > self.capacitate:
                print("Prea mult lichid!")
            else:
                self.cantitate += litri

        def scoate(self, litri):
            if litri > self.cantitate:
                print("Nu poti scoate mai multi litri decat ai deja.")
            else:
                self.cantitate -= litri

    bidon = Bidon(2, 5)
    print(f"{bidon.cantitate} din {bidon.capacitate}")

    bidon.adauga(3)
    print(f"{bidon.cantitate} din {bidon.capacitate}")

    bidon.scoate(5)
    print(f"{bidon.cantitate} din {bidon.capacitate}")


def ex18():
    #   Creeaza o clasa portofel si o metoda de transferat bani dintr-un portofel in altul. Tine cont! Portofelul trebuie
    # sa poata tine mai multe tipuri de monede (Euro, Lei, Dolar, etc).
    #   Exemplu narativ: Ai un portofel (WalletX) si vrei sa transferi banii intr-un alt portofel (WalletY), ca sa faci
    # asta, poti apela metoda WalletX.transfer(toWallet=WalletY, coin="Euro", howMuch=10), aceasta metoda va transfera
    # 10 Euro din WalletX in WalletY, chiar daca WalletX nu detine deja moneda Euro si detine doar moneda Lei

    class Portofel:

        def __init__(self):
            self.balanta = {}

        def adauga_bani(self, cantitate, moneda):
            if moneda in self.balanta:
                self.balanta[moneda] += cantitate
            else:
                self.balanta[moneda] = cantitate

        def transfer(self, toWallet, moneda, cantitate):
            if moneda in self.balanta and self.balanta[moneda] >= cantitate:
                toWallet.adauga_bani(cantitate, moneda)
                self.balanta[moneda] -= cantitate
                print("Transferul a fost realizat.")
            else:
                print("Nu ai suficienti bani.")

    portofel1 = Portofel()
    portofel2 = Portofel()

    portofel1.transfer(portofel2, "euro", 5)


def exempluEx1():
    # 1. Scrie un dictionar in care sa ai 3 camere ca si chei (Baie, Bucatarie, Dormitor) si ca valori pentru fiecare cheie,
    # o lista cu 3 obiecte din fiecare camera.
    # Exercitiu: Printeaza toate obiectele unul sub altul.

    dictionar = {"Baie": ["wc", "oglinda", "robinet"],
                 "Bucatarie": ["cutit", "lingura", "furculita"],
                 "Dormitor": ["pat", "tv", "dulap"]}

    print(dictionar)

    for cheie in dictionar:
        for i in range(len(dictionar[cheie])):
            if dictionar[cheie][i] == "dulap":
                dictionar[cheie][i] = "noptiera"

    print(dictionar)


def ex19():
    # Creeaza o clasa device care sa contina un numar de porturi, porturile respective ar trebui sa fie obiecte din clasa
    # port (fiecare port sa aibe un portID).
    class Device:
        def __init__(self, nrPorturi):
            self.nrPorturi = nrPorturi
            self.listaPorturi = []

            for i in range(1, nrPorturi+1):
                port = Port(i)
                self.listaPorturi.append(port.portID)

            for port in self.listaPorturi:
                print(port)

        def setViteza(self, port, viteza):
            port.viteza = viteza


    class Port:
        def __init__(self, portID):
            self.portID = portID
            self.viteza = 15

    port1 = Port("p01")
    print(port1.viteza)
    print(port1)
    device1 = Device(5)

    device1.setViteza(port1, 15)
    print(port1.viteza)


def ex21():
    # [Dictionare] 21. Transforma lista respectiva in asa fel incat rezultatul sa fie cel din dictionar.
    #
    # dictionarRezultat = {"Device1": {"Monitorizat": True, "Controlat": True},
    #                 "Device2": {"Monitorizat": True, "Controlat": True},
    #                 "Device3": {"Monitorizat": True, "Controlat": True},
    #                 "Device4": {"Monitorizat": True, "Controlat": True},
    #                 "Device5": {"Monitorizat": True, "Controlat": True},
    #                 "Device6": {"Monitorizat": True, "Controlat": True}
    #                      }

    lista = ["Device1", "Monitorizat", True, "Controlat", True,
             "Device2", "Monitorizat", True, "Controlat", True,
             "Device3", "Monitorizat", True, "Controlat", True,
             "Device4", "Monitorizat", True, "Controlat", True,
             "Device5", "Monitorizat", True, "Controlat", True,
             "Device6", "Monitorizat", True, "Controlat", True
             ]

    dictionar = {}

    for i in range(0, len(lista), 5):
        dictionar[lista[i]] = {lista[i + 1]: lista[i + 2], lista[i + 3]: lista[i + 4]}

    for obiect in dictionar:
        if obiect == "Device6":
            dictionar[obiect]["Controlat"] = False

    print(dictionar)

#   Creeaza o clasa (clasa om), cu cel putin 3 argumente, si 2 metode (functii) pe care orice obiect din clasa om sa le faca
    # (exemplu: sa mearga si sa citeasca o carte).
    #   Bonus: unul dintre argumente sa tina cont de cate carti a citit si dupa fiecare apelare a metodei "citesteOCarte" acest
    # argument sa se incrementeze cu 1.

# class Om:
#     def __init__(self, nume):
#         self.nume = nume
#         self.cartiCitite = []
#
#     def citesteCarte(self, carte, pagini):
#         dictCarti = {carte : pagini}
#
#         self.cartiCitite.append(dictCarti)
#
#         for carteDict in self.cartiCitite:
#             if carte == list(carteDict.keys())[0]:
#                 pass
#
#
# class Carte:
#     def __init__(self, numeCarte):
#         self.numeCarte = numeCarte


def ex19Clear():
    # 19. Creeaza o clasa device care sa contina un numar de porturi, porturile respective ar trebui sa fie obiecte din clasa port (fiecare port sa aibe un portID).

    class Device:
        def __init__(self, nrPorturi):
            self.listaPorturi = []

            for i in range(1, nrPorturi+1):
                port = Port(i)
                self.listaPorturi.append(port)

        def setViteza(self, portID, viteza):
            for portObject in self.listaPorturi:
                if portObject.portID == portID:
                    portObject.viteza = viteza

        def getViteza(self, portID):
            for portObject in self.listaPorturi:
                if portObject.portID == portID:
                    return portObject.viteza


        def checkViteza(self, portID, viteza):
            for portObject in self.listaPorturi:
                if portObject.portID == portID:
                    if portObject.viteza == viteza:
                        return True
            return False

    class Port:
        def __init__(self, portID):
            self.portID = f"P0{portID}"
            self.viteza = 0

    device = Device(5)
    device.setViteza("P03", 10)

    print(device.getViteza("P03"))

    print(device.checkViteza("P08", 10))


def ex20():
    # 20. Creeaza o clasa poarta si o clasa cartela si conecteaza-le intre ele. Poarta ar trebui sa fie deschisa doar de
    # cartela corespunzatoare si un parametru care sa tina cont daca poarta e deschisa sau nu

    class Poarta:
        def __init__(self, frecventa):
            self.frecventa = frecventa
            self.deschisa = False

        def deschide(self, cartela):
            if self.deschisa == False:
                if cartela.frecventa == self.frecventa:
                    self.deschisa = True
                    print("Poarta a fost deschisa.")
                else:
                    print("Cartela nu se potriveste.")
            else:
                print("Poarta este deja deschisa.")

        def inchide(self, cartela):
            if self.deschisa == True:
                if cartela.frecventa == self.frecventa:
                    self.deschisa = False
                    print("Poarta a fost inchisa.")
                else:
                    print("Cartela nu se potriveste.")
            else:
                print("Poarta este deja inchisa.")

    class Cartela:
        def __init__(self, frecventa):
            self.frecventa = frecventa

    poarta = Poarta(10)
    cartela = Cartela(10)

    poarta.inchide(cartela)
    poarta.deschide(cartela)
    poarta.deschide(cartela)
    poarta.inchide(cartela)
    poarta.inchide(cartela)
    poarta.deschide(cartela)


