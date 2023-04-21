from warrior_creator import Warrior_creator
from warriors import Warriors

filepath="Baza"
my_objects={} #słownik


def try_parse_int(text):
    try:
        return int(text)
    except:
        return None


def question(text) -> int:
    try:
        would=int(input(text))
        return would
    except ValueError:
        print("You have to input a number")



def add_tobase(filepath,my_objects): #dodaje 1 element
    file=open(filepath, 'w', encoding="utf8")
    for name in my_objects:
        file.write(str(my_objects[name].name)+" "+str(my_objects[name].ad)+" "+str(my_objects[name].health)+" "+str(my_objects[name].agility)+"\n")
    file.close()


def read_frombase(filepath,my_objects):
    file = open(filepath, 'r', encoding="utf8")
    for i in file:
        new_object = i.strip().split(" ")
        if new_object[0] not in my_objects:
            my_objects[new_object[0]] = Warriors(new_object[0],int(new_object[1]), int(new_object[2]), int(new_object[3]))


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
    if len(my_objects)!=0:
        print(f"Your available warriors: \n"
              f"{'Name':15s}|{'AD ':4s}|{'Health':5s}|{'Agility':2s}")
        for j in my_objects:
            print(f"{my_objects[j].name:15s}|{my_objects[j].ad:3} |{my_objects[j].health:4}  |{my_objects[j].agility:2}")
    else:
        print("There are no warriors available")


def add(my_objects):
    while True:
        question1 = input("Would you like to make a new character (y/n): ")
        if question1 == 'y':
            wc=Warrior_creator()
            war_obj=wc.create()
            my_objects[war_obj.name]=war_obj
            add_tobase(filepath, my_objects)
        else:
            break


def choose_fighters(my_objects):
    if len(my_objects)>=2:
        warrior1 = ""
        print("If you are scared of fighting type None")
        while True:
            choose = input("Write a name of the first warrior\n")
            if choose=="None":
                break
            try:
                if choose == my_objects[choose].name:
                    warrior1 = choose
                    break
            except ValueError:
                print("There is no warrior called like that in a list")
                continue

        while True:
            choose2 = input("Write a name of second warrior\n")
            try:
                if choose2 == my_objects[choose2].name and choose2 != my_objects[choose].name:
                    warrior2=choose2
                    break
            except ValueError:
                print("There is no warrior called like that in a list")
        return [warrior1,warrior2]
    else:
        print("There are no warriors available")
        return [0,0]


def fight(id_warrior1,id_warrior2,DMG1, DMG2, health1, health2):
    if health1!=0:     #Fight comments
        print(f'{id_warrior1} hit the {id_warrior2} with {DMG1}')
        health1-=DMG2
        print(f'{id_warrior2} hit the {id_warrior1} with {DMG2}')
        health2-=DMG1
        print(f'{id_warrior1},{health1},{id_warrior2}, {health2}\n')
        if health1<=0:
            print(f'{id_warrior2} won the fight')
            return [health1,health2,False]
        elif health2<=0:
            print(f'{id_warrior1} won the fight')
            return [health1,health2,False]
        else:
            return [health1,health2,True]
    else:
        print("There are no warriors available")


def fight_pattern(my_objects):
    if len(my_objects)>=2: #implementing data from my_objects dictionary
        read_frombase(filepath, my_objects)
        available_warriors(my_objects)
        [id_warrior1,id_warrior2]=(choose_fighters(my_objects))
        tmhp1 = my_objects[id_warrior1].health
        tmhp2 = my_objects[id_warrior2].health
        DMG1 = int(my_objects[id_warrior1].ad)*int((1+int(my_objects[id_warrior1].agility)/100))
        DMG2 = int(my_objects[id_warrior2].ad)*int((1+int(my_objects[id_warrior2].agility)/100))
        my_objects[id_warrior1].health=int(my_objects[id_warrior1].health)
        my_objects[id_warrior2].health=int(my_objects[id_warrior2].health)
        end=True
        while end==True:
            [my_objects[id_warrior1].health,my_objects[id_warrior2].health,end]=fight(id_warrior1,id_warrior2,DMG1,DMG2,(my_objects[id_warrior1].health),(my_objects[id_warrior2].health))
        my_objects[id_warrior1].health=tmhp1
        my_objects[id_warrior2].health=tmhp2
    else:
        print("There are no warriors available")


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
    print("-----------------Menu------------------- \n1. Informations about the game \n2. Play \n3. Exit\n")
    ans1=question("Choose one from menu: ")
    if ans1==1 or ans1==2 or ans1==3:
        if ans1 == 1:
            print(
                "This is a RPG game about warriors \n"
                "You can add warrior to your data base and fight with different one\n"
                "Fight process works in the way that fighter gets minus health points which are equal to total damage of different fighter\n"
                "Total damage=Attack damage multipled by (1+(agility/100))\n"
                "The fight is over when one of the fighters is dead it means that his health is equal or lower than zero\n")
            menu()
        elif ans1 == 2:
            game_menu()
        elif ans1 == 3:
            print("End")
    else:
        menu()
menu()
