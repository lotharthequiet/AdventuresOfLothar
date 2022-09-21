#!/bin/python3
import csv
import logging
import os

class Log:                                              #Logging class
    Logger = logging.getLogger(__name__)
    Logger.setLevel(logging.DEBUG)
    Loggerfmt = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    #Logh = logging.FileHandler('game.log')
    Logh = logging.StreamHandler()
    Logh.setFormatter(Loggerfmt)
    Logger.addHandler(Logh)

class GameMechanics:                                    #Game mechanics class (Contains all mechanisms for game) 
    def get_armor(self):                                #Get armor.dat file
        try:
            with open('armor.dat', newline='') as f:
                reader = csv.reader(f)
                armor = list(reader)
                return armor
        except Exception as e:
            Log.Logger.error("Unable to open armor.dat.", e)
    
    def get_rooms(self):                                #Get rooms.dat file
        try: 
            with open('rooms.dat', newline='') as f:
                reader = csv.reader(f)
                rooms = list(reader)
                return rooms
        except Exception as e:
            Log.Logger.error("Unable to open rooms.dat.", e)
            
    def get_weapons(self):                              #Get weapons.dat file
        try:
            with open('weapons.dat', newline='') as f:
                reader = csv.reader(f)
                weapons = list(reader)
                return weapons
        except Exception as e:
            Log.Logger.error("Unable to open weapons.dat.", e)

    def cls():                                          #Clear screen func
        os.system('cls' if os.name=='nt' else 'clear')

    def randomize_npc(self):                            #This func will randomize the QTY and type of NPC in each room
        print("Do something here")

    def do_battle(self):                                #This func will calculate battle stats and apply HP, damage, subtract health, etc.
        print("Do something here")

    def enter_room(self):                               #This func will be used when enterring a room
        print("Do something here")

    def inspect_item(self, item):                       #This func will inspect item
        print("Do something here")

class Player:
    def __init__(self):
        self.name = "Lothar"                            #Player Name
        self.health = 100                               #Player max health
        self.skills = 0                                 #Player skill level
        self.weapon = None                              #Player Weapon
        self.level = 0                                  #Player game level
        self.armor = 0                                  #Player armor
        self.inventory = list(range(10))                #Player inventory
        self.location = None

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

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

class Weapon:
    def __init__(self, name, hp, reqskill, damage):
        self.name = name                            #Name of weapon
        self.hp = hp                                #Hit points delivered from weapon
        self.reqskill = reqskill                    #Required skill level
        self.damage = damage                            #Damage limit of weapon

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
    def __init__(self, name, hp, reqskill, damage):
        self.name = name                                #Armor name
        self.hp = hp                                    #Armor protection
        self.reqskill = reqskill                        #Required skill level
        self.damage = damage                            #Damage limit of weapon

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_protection(self):
        return self.hp

    def set_protection(self, hp):
        self.hp = hp

    def get_reqskill(self):
        return self.reqskill

    def set_reqskill(self, reqskill):
        self.reqskill = reqskill

    def get_damage(self):
        return self.damage

    def set_damage(self, damage):
        self.damage = damage

class Room:
    def __init__(self, name, greeting, item, info, mapN, mapE, mapS, mapW):
        self.name = name                                #Room name
        self.greeting = greeting                        #Room greeting
        self.item = list(range(4))                      #Room item
        self.info = info                                #Room info
        self.mapN = mapN                                #Room to north of current room
        self.mapE = mapE                                #Room to east of current room
        self.mapS = mapS                                #Room to south of current room
        self.mapW = mapW                                #Room to west of current room
        self.npc = list(range(3))                       #Room NPC inventory
    
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
    player1 = Player()
    #Beyond this line still sucks
    armor = GameMechanics.get_armor()
    armor = Armor()
    rooms = GameMechanics.get_rooms()
    rooms = Room()
    weapons = GameMechanics.get_weapons()
    weapons = Weapon()
    print("Welcome to the Adventures of Lothar.")
    print("A text-based adventure game.")
    print("")
    print("")
    print("")
    print("You are a peasant. Your name is:")
    #print(player1.get_name())

    
