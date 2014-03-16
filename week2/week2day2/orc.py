from entity import Entity

class Orc(Entity):
    """docstring for Orc"""
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        if (berserk_factor > 2):
            self.berserk_factor = 2
        elif(berserk_factor < 1):
            self.berserk_factor = 1
        else:
            self.berserk_factor = berserk_factor

    def get_berserk_factor(self):
        return self.berserk_factor

    def attack(self):
        return self.berserk_factor*super().attack()