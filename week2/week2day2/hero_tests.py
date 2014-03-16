import hero
import orc
import entity
import fight
import unittest


class Hero_Test(unittest.TestCase):
    """docstring for Hero"""

    def setUp(self):
        self.oppo = hero.Hero("Oppo", 22, "SuperDog")
        self.nexus = hero.Hero("Nexus", 100, "VillainMegaDog")
        self.dodo = orc.Orc("Dodo", 50, 1.5)
        self.axe = entity.Weapon("Axe", 15, 0.18)

    """Tests for Hero"""
    def test_known_as(self):
        self.assertEqual("Oppo the SuperDog", self.oppo.known_as())

    def test_is_alive(self):
        self.assertEqual(True, self.oppo.is_alive())
        self.nexus.current_health = 0
        self.assertEqual(False, self.nexus.is_alive())

    def test_get_health(self):
        self.assertEqual(22, self.oppo.get_health())

    def test_take_damage(self):
        self.assertEqual(12, self.oppo.take_damage(10))
        self.assertEqual(12, self.oppo.get_health())
        self.assertEqual(0, self.oppo.take_damage(50))

    def test_max_health_stays_unchanged(self):
        self.nexus.take_damage(30)
        self.nexus.take_healing(50)
        self.assertEqual(100, self.nexus.get_health())

    def test_take_healing(self):
        self.oppo.take_damage(30)
        self.assertFalse(self.oppo.take_healing(15))
        self.nexus.take_damage(30)
        self.assertTrue(self.nexus.take_healing(50))

    def test_berserk_factor_range(self):
        self.assertEqual(1.5, self.dodo.get_berserk_factor())

    # Test including random result. If tested should return both true and false on different runs.
    """def test_critical_hit(self):
        self.assertTrue(self.axe.critical_hit())
    """

    def test_has_weapon(self):
        self.assertFalse(self.oppo.has_weapon())

    def test_equip_weapon(self):
        self.oppo.equip_weapon(self.axe)
        self.assertTrue(self.oppo.has_weapon())

    def test_attack(self):
        self.oppo.equip_weapon(self.axe)
        self.assertEqual(15, self.oppo.attack())
        # with no weapon equipped the damage is a random number between 0 and 10
        self.assertGreater(10, self.nexus.attack())
        self.assertLess(0, self.nexus.attack())
        # test berserk factor when attacking
        self.dodo.equip_weapon(self.axe)
        self.assertEqual(22.5, self.dodo.attack())



if __name__ == '__main__':
    unittest.main()