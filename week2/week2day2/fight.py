import random
import entity
import hero
import orc

class Fight():
    """docstring for Fight"""
    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc
        if(random.random()*100 < 50):
            self.first = self.hero
            self.second = self.orc
        else:
            self.first = self.orc
            self.second = self.hero

    def simulate_fight(self):
        while (self.hero.is_alive() and self.orc.is_alive()):
            if(self.first.is_alive()):
                damage1 = self.first.attack()
                self.second.take_damage(damage1)
            else:
                break
            if(self.second.is_alive()):
                damage2 = self.second.attack()
                self.first.take_damage(damage2)
            else:
                break

        if(self.hero.is_alive() and self.orc.is_alive() == False):
            winner = self.hero.name
        elif(self.orc.is_alive() and self.hero.is_alive() == False):
            winner = self.orc.name
        else:
            winner = False
        return winner


""" Hand testinng
    def check_critical_strike(self, attacker, damage):
        if (attacker == self.hero):
            if(damage == 2*attacker.weapon.default_damage):
                dd = " Double damage!!!"
            else:
                dd = ""
        elif (attacker == self.orc):
            if(damage == 2*attacker.weapon.default_damage*attacker.berserk_factor):
                dd = " Double damage!!!"
            else:
                dd = ""
        return dd

    def simulate_fight(self):
        print("Hero life: ", self.hero.get_health(), "Orc life: ", self.orc.get_health())
        while (self.hero.is_alive() and self.orc.is_alive()):
            if(self.first.is_alive()):
                damage1 = self.first.attack()
                print(damage1)
                double_damage = self.check_critical_strike(self.first, damage1)

                self.second.take_damage(damage1)
                attack = self.first.name + " attacking!"
                first_life = str(self.first.name) + " life: " + str(self.first.get_health())
                second_life = str(self.second.name) + " life: " + str(self.second.get_health())
                print(attack, first_life, second_life, double_damage)
            else:
                break
            if(self.second.is_alive()):
                damage2 = self.second.attack()
                print(damage2)
                double_damage = self.check_critical_strike(self.second, damage2)

                self.first.take_damage(damage2)
                attack = self.second.name + " attacking!"
                first_life = str(self.first.name) + " life: " + str(self.first.get_health())
                second_life = str(self.second.name) + " life: " + str(self.second.get_health())
                print(attack, first_life, second_life, double_damage)
            else:
                break

        if(self.hero.is_alive() and self.orc.is_alive() == False):
            winner = self.hero.name
        elif(self.orc.is_alive() and self.hero.is_alive() == False):
            winner = self.orc.name
        else:
            winner = False
        return winner


def main():
    hero2 = hero.Hero("Hero", 100, "WOW")
    orc2 = orc.Orc("Orc", 50, 1.5)
    sword = entity.Weapon("sword", 20, 0.3)
    hero2.equip_weapon(sword)
    orc2.equip_weapon(sword)
    fight2 = Fight(hero2, orc2)
    print(fight2.simulate_fight())

if __name__ == '__main__':
    main()

"""