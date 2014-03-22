import random

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
