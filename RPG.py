import random
import re
class warrior: #warrio_creator
    def __init__(self,name,AD,health,agility):
        self.name=name
        self.AD = AD
        self.health=health
        self.agility = agility
class warrior_creator:
    def __init__(self):
        pass
    def create(self):
        max_points=random.randint(85,100)
        name_reg="/^[a-z_-]$/"
        while True:
            name = input("Choose a name for your warrior: ")
            check = re.search(name_reg, name)
            if check:
                print("You entered wrong name (It must be text)")
            else:
                break
        print(" ")
        print("Your will add points to every category except agility. Agility will be rest of you reamaining points")
        print("Every addition to attack or health costs points",end=" \n")
        print("Your points: ", max_points,"\n")
        while True:
            try:
                AD = int(input("How much attack damage would you like to have? "))
                if AD>=1 and AD<max_points:
                    max_points-=AD
                    break
            except:
                print("You have to enter a number beetween 1 -",max_points)
        health = random.randint(90, 110)
        while True:
            try:
                print("Your points: ", max_points)
                health_add = int(input("How much points would you like to spend on health? "))
                if health_add >= 1 and health_add <= max_points:
                    max_points -= health_add
                    break
            except:
                print("You have to enter a number beetween 1 -", max_points)
        health+=health_add
        agility=max_points
        print("Your warrior:")
        stats="Name"
        for j in range(len(name)-3):
            stats+=" "
        stats+="| AD | Health | Agility"
        print(stats)
        print(name,"|",AD,"|  ",health," |   ",agility)
        return warrior(name,AD,health,agility)

filepath="Baza"
my_objects={} #dictionary

def question(text):
    try:
        would=int(input(text))
        return would
    except ValueError:
        print("You have to input a number")

def add_tobase(filepath,my_objects): #dodaje 1 element
    file=open(filepath, 'w', encoding="utf8")
    for name in my_objects:
        file.write(str(my_objects[name].name)+" "+str(my_objects[name].AD)+" "+str(my_objects[name].health)+" "+str(my_objects[name].agility)+"\n")
    file.close()

def read_frombase(filepath,my_objects):
    file = open(filepath, 'r', encoding="utf8")
    for i in file:
        new_object = i.strip().split(" ")
        if new_object[0] not in my_objects:
            my_objects[new_object[0]] = my_objects.get(new_object[0], warrior(new_object[0], new_object[1], new_object[2], new_object[3]))

def delete_from_base(my_objects):
    while True:
        print("If you don't want to delete any warrior answer None")
        name = input("Which warrior would you like to delete from the data base:")
        if name in my_objects:
            my_objects.pop(name)
            add_tobase(filepath, my_objects)
            break
        elif name == "None":
            break

def available_warriors(my_objects):
    print("Your available warriors: \n")
    print("Name | AD | Health | Agility")
    for j in my_objects:
        print(my_objects[j].name,my_objects[j].AD,my_objects[j].health,my_objects[j].agility)

def add(my_objects):
    name='{}'
    while True:
        question1 = input("Would you like to make a new character (y/n): ")
        if question1 == 'y':
            wc=warrior_creator()
            war_obj=wc.create()
            my_objects[war_obj.name]=war_obj
            add_tobase(filepath, my_objects)
        else:
            break

def choose_fighters(my_objects):
    choose = input("Write a name of the first warrior\n")
    warrior1=0
    while True:
        try:
            if choose == my_objects[choose].name:
                warrior1 = choose
                break
        except:
            print("There is no warrior called like that in a list")
            continue
    choose2 = input("Write a name of second warrior\n")
    while True:
        try:
            if choose2 == my_objects[choose2].name and choose2 != my_objects[choose].name:
                warrior2=choose2
                break
        except:
            print("There is no warrior called like that in a list")
    return [warrior1,warrior2]

def fight(id_warrior1,id_warrior2,DMG1, DMG2, health1, health2):
    print(id_warrior1," hit the ",id_warrior2," with ",DMG1)
    health1-=DMG2
    print(id_warrior2, " hit the ", id_warrior1," with ", DMG2)
    health2-=DMG1
    print(id_warrior1,health1)
    print(id_warrior2,health2)
    if health1<=0:
        print(id_warrior2, "won the fight")
        return [health1,health2,False]
    elif health2<=0:
        print(id_warrior1, "won the fight")
        return [health1,health2,False]
    else:
        print(health1,health2)
        return [health1,health2,True]

def fight_pattern(my_objects):
    read_frombase(filepath, my_objects)
    available_warriors(my_objects)
    [id_warrior1,id_warrior2]=(choose_fighters(my_objects))
    tmhp1=my_objects[id_warrior1].health
    tmhp2 = my_objects[id_warrior2].health
    DMG1 = int(my_objects[id_warrior1].AD)*int((1+int(my_objects[id_warrior1].agility)/100))
    DMG2 = int(my_objects[id_warrior2].AD)*int((1+int(my_objects[id_warrior2].agility)/100))
    my_objects[id_warrior1].health=int(my_objects[id_warrior1].health)
    my_objects[id_warrior2].health=int(my_objects[id_warrior2].health)
    end=True
    while end==True:
        [my_objects[id_warrior1].health,my_objects[id_warrior2].health,end]=fight(id_warrior1,id_warrior2,DMG1,DMG2,(my_objects[id_warrior1].health),(my_objects[id_warrior2].health))
    my_objects[id_warrior1].health=tmhp1
    my_objects[id_warrior2].health=tmhp2

def game_menu():
    print("What would you like to do?\n1. Add new warrior\n2. Delete warrior\n3. Show available warriors\n4. Fight with warrior\n5. Go back to menu")
    ans2 = question("Choose one from above: ")
    if ans2==1 or ans2==2 or ans2==3 or ans2==4 or ans2==5:
        if ans2 == 1:
            read_frombase(filepath, my_objects)
            add(my_objects)
        elif ans2 == 2:
            delete_from_base(my_objects)
        elif ans2 == 3:
            read_frombase(filepath, my_objects)
            available_warriors(my_objects)
        elif ans2 == 4:
            fight_pattern(my_objects)
        elif ans2 == 5:
            exit(menu())
    game_menu()

def menu():
    print("-----------------Menu------------------- \n1. Informations about the game \n2. Play \n3. Exit")
    ans1=question("Choose one from menu: ")
    if ans1==1 or ans1==2 or ans1==3:
        if ans1 == 1:
            print(
                "This is a RPG game about warriors \nYou can add warrior to your data base and fight with different one\nFight process works in the way that fighter gets minus health points which are equal to total damage of different fighter\nTotal damage=Attack damage multipled by (1+(agility/100))\nThe fight is over when one of the fighters is dead it means that his health is equal or lower than zero")
            menu()
        elif ans1 == 2:
            game_menu()
        elif ans1 == 3:
            print("End")
    else:
        menu()
menu()
