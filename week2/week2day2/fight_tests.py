import hero
import orc
import entity
import fight
import unittest


class Fight_Test(unittest.TestCase):
    """docstring for Fight"""

    def test_simulate_fight(self):
        hero1 = hero.Hero("Hero", 100, "WOW")
        orc1 = orc.Orc("Orc", 20, 1.5)
        sword = entity.Weapon("sword", 20, 0.4)
        hero1.equip_weapon(sword)
        fight1 = fight.Fight(hero1, orc1)
        winner = fight1.simulate_fight()
        self.assertEqual("Hero", winner)
        


if __name__ == '__main__':
    unittest.main()