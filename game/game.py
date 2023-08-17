from player import *

# Dupa challange, daca unul moare sa nu mai poti da challange iar
# Sa nu fie mai multe iteme identice echipate (dictionare)
# Sa alegi ce item sa dropezi
# in data base sa fie scrise si valorile itemelor

# FISIER

p = Player("Andrei")
p2 = Player("Dante")
print(f"Aici e playerul {p.username}")
print(f"helmet +{p.helmet.property}, shield +{p.shield.property}, armour +{p.armour.property}, boots +{p.boots.property}, sword +{p.sword.property}")
print(f"{p.username} hp: {p.hp} \n{p.username} defence: {p.defence}\n{p.username} attack value: {p.attack_value}")
print()
print(p2.username)
print(f"helmet +{p2.helmet.property}, shield +{p2.shield.property}, armour +{p2.armour.property}, boots +{p2.boots.property}, sword +{p2.sword.property}")
print(f"{p2.username} hp: {p2.hp} \n{p2.username} defence: {p2.defence}\n{p2.username} attack value: {p2.attack_value}")
print()



flag = 1
while(flag == 1):
    print("Choose an action:")
    print("1. Check inventory.\n2. Check your equipped items.\n3. Check items near you.\n4. Check your HP.\n5. Check an item.\n6. Equip an item from your inventory.\n7. Take off an item.\n8. Drop an item.\n9. Pick up an item near you.\n10. Move.\n11. Attack!\n12. Exit.")
    n = input()

    if n == "1":
        print(f"Your inventory: {p.get_inventory()}")
    elif n == "2":
        print(f"Your equiped items: {p.get_equipped()}")
    elif n == "3":
        print(f"The items near you: {p.getNearItems()}")
    elif n == "4":
        print(f"Your HP: {p.hp}")
    elif n == "5":
        var = input("Write the item. \n")
        print(p.checkItem(var))
    elif n == "6":
        print(f"Your inventory: {p.get_inventory()}.")
        p.equipItem(input("Write the item. "))
    elif n == "7":
        print(f"Your equiped items: {p.get_equipped()}")
        p.takeOffItem(input("Write the item: "))
    elif n == "8":
        print(f"Your inventory: {p.get_inventory()}.")
        print(f"Your equiped items: {p.get_equipped()}")
        p.drop_item(input("Write the item. "))
    elif n == "9":
        print(f"Items near you: {p.getNearItems()}")
        p.pickUpItem(input("Write the item you want to pick up. "))
    elif n == "10":
        p.move(int(input("Write the meters. ")))
    elif n == "11":
        name = input("Write the player you want to attack. ")
        if name == p2.username:
            print(p.attack(p2))
        else:
            print("This player doesn't exist.")
    elif n == "12":
        flag = 0
    else:
        print("Invalid option.")

    print()