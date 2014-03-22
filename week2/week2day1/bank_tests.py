import unittest
import bank

class BankAccountTests(unittest.TestCase):
    """Testing the bank module"""

    def test_deposit_money(self):
        bank.balance = 0
        self.assertEqual(50, bank.deposit_money(50))


    def test_withdraw_money(self):
        bank.balance = 100
        self.assertEqual(40, bank.withdraw_money(60))


if __name__ == '__main__':
    unittest.main()
