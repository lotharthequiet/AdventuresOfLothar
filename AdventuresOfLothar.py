#!/bin/python3
import csv
import logging
import os

class Log:
    Logger = logging.getLogger(__name__)
    Logger.setLevel(logging.DEBUG)
    Loggerfmt = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    #Logh = logging.FileHandler('LinuxSystemToolbox.log')
    Logh = logging.StreamHandler()
    Logh.setFormatter(Loggerfmt)
    Logger.addHandler(Logh)

class GameMechanics:
    def get_armor(self):
        try:
            with open('armor.csv', newline='') as f:
                reader = csv.reader(f)
                armor = list(reader)
                return armor
        except Exception as e:
            Log.Logger.error("Unable to open armor.csv.", e)
    def get_rooms(self):
        try: 
            with open('rooms.csv', newline='') as f:
                reader = csv.reader(f)
                rooms = list(reader)
                return rooms
        except Exception as e:
            Log.Logger.error("Unable to open rooms.csv.", e)
            
    def get_weapons(self):
        try:
            with open('weapons.csv', newline='') as f:
                reader = csv.reader(f)
                weapons = list(reader)
                return weapons
        except Exception as e:
            Log.Logger.error("Unable to open weapons.csv.", e)

    def cls():
        os.system('cls' if os.name=='nt' else 'clear')

    def start_game(self):
        self.cls()
        print("Welcome to the Adventures of Lothar.")
        print("A text-based adventure game.")


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.skills = 0
        self.weapon = None
        self.level = 0
        self.armor = 0
        self.inventory = list(range(10))

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = self.health + health

    def get_skills(self):
        return self.skills

    def set_skills(self, skills):
        self.skills = self.skills + skills
    
    def get_weapon(self):
        return self.weapon

    def set_weapon(self, weapon):
        self.weapon = weapon

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = self.level + level

    def get_armor(self):
        return self.armor

    def set_armor(self, armor):
        self.level = armor

    def add_inventory(self, item):
        self.inventory.append(item)

    def sub_inventory(self, item):
        self.inventory.remove(item)

class Weapon:
    def __init__(self, name, damage, reqskill, hp):
        self.name = name
        self.damage = damage
        self.reqskill = reqskill
        self.hp = hp

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_damage(self):
        return self.damage
    
    def set_damage(self, damage):
        self.name = damage

    def get_reqskill(self):
        return self.level
    
    def set_reqskill(self, reqskill):
        self.name = reqskill

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.name = self.hp + hp

class Armor:
    def __init__(self, name, protection, reqskill):
        self.name = name
        self.protection = protection
        self.reqskill = reqskill

    def get_name(self):
        return self.name

    def get_protection(self):
        return self.protection

    def get_reqskill(self):
        return self.reqskill

class Room:
    def __init__(self, name, greeting, item, info, mapN, mapE, mapS, mapW):
        self.name = name
        self.greeting = greeting
        self.item = item
        self.info = info
        self.mapN = mapN
        self.mapE = mapE
        self.mapS = mapS
        self.mapW = mapW
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_greeting(self):
        return self.greeting

    def set_greeting(self, greeting):
        self.greeting = greeting

    def get_item(self):
        return self.item
    
    def set_item(self, item):
        self.item = item

    def get_info(self):
        return self.info
    
    def set_info(self, info):
        self.info = info

if __name__ == "__main__":
    GameMechanics.cls()
    print("Welcome to the Adventures of Lothar.")
    print("A text-based adventure game.")