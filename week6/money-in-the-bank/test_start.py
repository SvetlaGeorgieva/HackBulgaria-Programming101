import unittest
import hashlib
import sqlite3
import client
import sql_manager


class TestStart(unittest.TestCase):
    """docstring for TestStart"""
    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register("user1", "Tu6^^^pass1")

    # test against sql injections in login
    def test_login(self):
        self.assertEqual(True, isinstance(sql_manager.login("user1", "Tu6^^^pass1"), client.Client))
        self.assertEqual(False, isinstance(sql_manager.login("user1", "' OR 1 = 1 --"), client.Client))
        self.assertEqual(False, isinstance(sql_manager.login("' OR 1 = 1 --", "fsjfljkd"), client.Client))

    def test_strong_pass(self):
        pass1 = "123456"
        self.assertEqual(False, sql_manager.strong_pass("user1", pass1))
        pass1 = "123456789"
        self.assertEqual(False, sql_manager.strong_pass("user1", pass1))
        pass1 = "1234567abs89"
        self.assertEqual(False, sql_manager.strong_pass("user1", pass1))
        pass1 = "1234567ABC89"
        self.assertEqual(False, sql_manager.strong_pass("user1", pass1))
        pass1 = "1234567abcABC89"
        self.assertEqual(False, sql_manager.strong_pass("user1", pass1))
        pass1 = "1234567abcABC89#"
        self.assertEqual(True, sql_manager.strong_pass("user1", pass1))
        pass1 = "1234567abcABC89#"
        self.assertEqual(True, sql_manager.strong_pass("user1", pass1))
        pass1 = "user1234567abcABC89#"
        self.assertEqual(False, sql_manager.strong_pass("user1", pass1))

    def test_register(self):
        # prompts for a stronger password
        # sql_manager.register("user2", "stupidpass")

        self.assertEqual(True, sql_manager.register("user2", "Tu6^^^pass2"))
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()
        select_query = "SELECT id, username, password FROM clients WHERE \
                        username = ? AND password = ? LIMIT 1"
        cursor.execute(select_query, ("user2", sql_manager.hash_pass("Tu6^^^pass2")))
        user = cursor.fetchone()
        self.assertEqual("user2", user[1])
        self.assertEqual(sql_manager.hash_pass("Tu6^^^pass2"), user[2])

    def test_change_pass(self):
        logged_user = sql_manager.login("user1", "Tu6^^^pass1")
        sql_manager.change_pass("new_PASS123", logged_user)
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()
        select_query = "SELECT id, username, password FROM clients WHERE \
                        username = ? AND password = ? LIMIT 1"
        cursor.execute(select_query, ("user1", sql_manager.hash_pass("new_PASS123")))
        user = cursor.fetchone()
        self.assertEqual("user1", user[1])
    #     self.assertEqual(sql_manager.hash_pass("new_PASS123"), user[2])

    def test_hash_pass(self):
        pass1 = "abcd123ABSD_123"
        m = hashlib.sha1()
        m.update(pass1.encode("utf-8"))
        hashed_pass = m.hexdigest()
        self.assertEqual(hashed_pass, sql_manager.hash_pass(pass1))

    """
        fail_login - count = 1,
        fail_login - count = 2,
        fail_login - count = 3,
        fail_login - count = 4,
        fail_login - count = 5, timestamp = timenow
        if timenow < timestamp + 300s:
            print("Profile locked")
    """
    # def test_force_lock(self):
    #     sql_manager.login("user1", "wrong_pass")
    #     sql_manager.login("user1", "wrong_pass")
    #     sql_manager.login("user1", "wrong_pass")
    #     sql_manager.login("user1", "wrong_pass")
    #     sql_manager.login("user1", "wrong_pass")

    def tearDown(self):
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()
        drop_query = "DROP TABLE IF EXISTS clients"
        cursor.execute(drop_query)


if __name__ == '__main__':
    unittest.main()
