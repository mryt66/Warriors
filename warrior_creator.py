import random
import re
from dataclasses import dataclass


@dataclass
class Warriors:
    name: str
    ad: int
    health: int
    agility: int


class Warrior_creator:
    @staticmethod
    def create(self):
        max_points = random.randint(85, 100)
        check = False
        name = ""
        ad = 0
        health_add = 0
        while not check:
            print("You have to enter text with 3 - 15 symbols")
            name = input("Choose a name for your warrior: ")
            if re.match('^.{3,15}$', name):
                break
        print("Your will add points to every category except agility. Agility will be rest of you remaining points"'\n',
              "Every addition to attack or health costs points")

        # attack damage
        print(f'Your points: {max_points}')
        while ad == 0:
            ad = input("How much points would you like to spend on attack damage? ")
            ad = try_parse_int(ad)
            if 1 <= ad <= max_points:
                max_points -= ad
                break
            else:
                print(f'You have to enter a number between 1 - {max_points}')
                ad = 0

        # health
        health = random.randint(90, 110)
        print(f'Your points: {max_points}')
        while health_add == 0:
            health_add = input("How much points would you like to spend on health? ")
            health_add = try_parse_int(health_add)
            if 1 <= health_add <= max_points:
                max_points -= health_add
                break
            else:
                print(f'You have to enter a number between 1 - {max_points}')
                health_add = 0
        health += health_add

        # agility
        agility = max_points

        print(f'Your warrior:{ad} {health} {agility}')
        print(f"{'Name':15s}|{' AD ':2s}|{' Health ':3s}|{' Agility ':2s}")
        print(f"{name:15s}| {ad:2} |{health:5}   |  {agility:3}")
        return Warriors(name, ad, health, agility)


def try_parse_int(text):
    try:
        return int(text)
    except:
        return None
