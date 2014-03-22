balance = 0


def deposit_money(amount):
    global balance
    balance += amount
    return balance


def withdraw_money(amount):
    global balance
    balance -= amount
    return balance