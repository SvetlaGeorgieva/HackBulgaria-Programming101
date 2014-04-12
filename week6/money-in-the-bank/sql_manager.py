import hashlib
from time import time
import getpass
import re
import sqlite3
from client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

pass_message = """Please, select a password that:
                    - has more than 8 symbols
                    - has a capital letter, a numbers and a special symbol
                    - doesn't contain your username
               """


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                access_log TIMESTAMP DEFAULT (strftime('%s', 'now')),
                failed_login_count INTEGER DEFAULT 0)'''

    cursor.execute(create_query)


def strong_pass(username, password):
    special_characters = "` ~ ! @ # $ % ^ & * ( ) _ - + = { } [ ] \ | : ; \
            \" \' < > , . ? "
    list_of_spec_chars = special_characters.split()
    if len(password) <= 8:
        # print("less than 9 digits")
        return False

    # is there a digit
    if re.search(r'\d', password) is None:
        # print("no digits")
        return False

    # is there an uppercase letter
    if re.search(r'[A-Z]', password) is None:
        # print("no uppercase letters")
        return False

    # is there a lowercase letter
    if re.search(r'[a-z]', password) is None:
        # print("no lowercase letters")
        return False

    # is there a special character
    count_sp_chars = 0
    for i in list_of_spec_chars:
        if i in password:
            count_sp_chars += 1
    if count_sp_chars == 0:
        # print("no special character")
        return False

    # check if username is a substring of the password
    if password.find(username) >= 0:
        # print("username in the password")
        return False

    return True


def change_pass(new_pass, logged_user):
    username = logged_user.get_username()
    while (not strong_pass(username, new_pass)):
        print(pass_message)
        new_pass = getpass.getpass(prompt="Enter your password: ", stream=None)

    update_query = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_query, (hash_pass(new_pass), logged_user.get_id()))
    conn.commit()


def register(username, password):
    while (not strong_pass(username, password)):
        print(pass_message)
        password = getpass.getpass(prompt="Enter your password: ", stream=None)

    insert_query = "insert into clients (username, password) values (?, ?)"
    cursor.execute(insert_query, (username, hash_pass(password)))
    conn.commit()
    return True


def force_lock():
    pass


def hash_pass(password):
    m = hashlib.sha1()
    m.update(password.encode("utf-8"))
    return m.hexdigest()


def check_pass(password, hashed_pass):
    pass1 = hash_pass(password)
    if pass1 == hashed_pass:
        return True
    else:
        return False


def get_client(username, password):
    select_query = "SELECT id, username, balance, access_log, \
                    failed_login_count FROM clients WHERE username = ? AND \
                    password = ? LIMIT 1"
    cursor.execute(select_query, (username, hash_pass(password)))
    user = cursor.fetchone()
    if user:
        return Client(user[0], user[1], user[2], user[3], user[4])
    else:
        return False


def update_access_log(username):
    update_query = "UPDATE clients SET access_log = ? WHERE username = ?"
    cursor.execute(update_query, (int(time()), username))
    conn.commit()


def login(username, password):
    # checks if there is such a username
    usernames = cursor.execute("SELECT username FROM clients").fetchall()
    if username not in usernames[0]:
        return False

    # gets the user
    client = get_client(username, password)

    # checks the validity of the password
    if client:
        return client
    else:
        update_access_log(username)
        get_time_query = "SELECT access_log FROM clients \
                            WHERE username = ? LIMIT 1"
        timestamp = cursor.execute(get_time_query, (username, ))
        print(timestamp.fetchone()[0])
        # lock_expire = timestamp.fetchone()[0] + 300
        # int(time.time()+300)

        return False
