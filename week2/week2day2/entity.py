import weapon
import random


class Entity():
    """docstring for Hero"""
    def __init__(self, name, health):
        self.name = name
        self.__max_health = health
        self.current_health = health
        self.weapon = ""

    def is_alive(self):
        if(self.current_health > 0):
            return True
        else:
            return False

    def get_health(self):
        return self.current_health

    def take_damage(self, damage_points):
        if(self.current_health < damage_points):
            self.current_health = 0
        else:
            self.current_health = self.current_health - damage_points
        return self.current_health

    def take_healing(self, healing_points):
        if(self.current_health == 0):
            return False
        elif(self.__max_health < self.current_health + healing_points):
            self.current_health = self.__max_health
        else:
            self.current_health = self.current_health + healing_points
        return True

    def has_weapon(self):
        if(self.weapon == ""):
            return False
        else:
            return True

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if(self.has_weapon()):
            weapon_damage = self.weapon.default_damage
            if(self.weapon.critical_hit()):
                weapon_damage *= 2
        else:
            weapon_damage = random.random()*10
        return weapon_damage



class Weapon():
    """docstring for Weapon"""
    def __init__(self, type, damage, critical_strike_percentage):
        super(Weapon, self).__init__()
        self.type = type
        self.default_damage = damage
        self.current_damage = damage
        self.critical_strike_percentage = critical_strike_percentage
        
    def critical_hit(self):
        if(random.random() < self.critical_strike_percentage):
            self.current_damage *= 2
            return True
        else:
            return False
