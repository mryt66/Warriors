import random
import re
from Warriors import Warriors

class Warrior_creator:
    def create(self):
        max_points = random.randint(85, 100)
        check=False
        name=""
        ad=0
        health_add=0
        while check==False:
            print("You have to enter text with 3 - 15 symbols")
            name = input("Choose a name for your warrior: ")
            if re.match('^.{3,15}$', name):
                break
        print("Your will add points to every category except agility. Agility will be rest of you reamaining points"'\n',
            "Every addition to attack or health costs points")

        #attack damage
        print(f'Your points: {max_points}')
        while ad == 0:
            ad = input("How much points would you like to spend on attack damage? ")
            ad = try_parse_int(ad)
            if 1 <= ad <= max_points:
                max_points -= ad
                break
            else:
                print(f'You have to enter a number beetween 1 - {max_points}')
                ad=0

        # health
        health = random.randint(90, 110)
        print(f'Your points: {max_points}')
        while health_add==0:
            health_add = input("How much points would you like to spend on health? ")
            health_add=try_parse_int(health_add)
            if 1<=health_add<=max_points:
                max_points -= health_add
                break
            else:
                print(f'You have to enter a number beetween 1 - {max_points}')
                health_add=0
        health+=health_add

        #agility
        agility=max_points

        print(f'Your warrior:{ad} {health} {agility}')
        print(f"{'Name':15s}|{' AD ':3s}|{' Health ':3s}|{' Agility ':2s}")
        print(f"{name:15s}| {ad:2} |{health:5}   |  {agility:3}")
        return Warriors(name,ad,health,agility)
