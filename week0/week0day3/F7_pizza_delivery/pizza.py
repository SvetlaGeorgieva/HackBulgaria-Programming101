import sys
from time import time
from datetime import datetime

    #args = []
    #args = sys.argv[1:]

#Global arguments
commands = ["finish", "take", "status", "save", "list", "load"]
clients = {
}
orders = []
save_status = True
list_status = False


""" Enter command>take Rado 10.0
    Taking order from Rado for 10.00 """
def take(args):
    global save_status
    global list_status
    name = args[1]
    money = int(args[2])
    current_order = "Taking order from " + name + " for " + str(money)
    if (name not in clients):
        clients[name] = money
    else:
        clients[name] += money
    save_status = False
    list_status = False
    return current_order


""" Enter command>status
    Rado - 20.00
    Ivan - 6.43 """
def status():
    global list_status
    current_status = []
    status_string = ""
    for key in clients:
        client_status = key + " - " + str(clients[key])
        current_status.append(client_status)
        status_string += client_status + "\n"
    status_string = status_string[:-1]
    list_status = False
    return status_string


""" Enter command>save
    Saved the current order to orders_2014_03_01_11_00_08
    Create a timestamped file, named orders_YYYY_mm_dd_hh_mm_ss where 
    YYYY is the current year, mm the current month, dd the current day, 
    hh the current hour, mm the current minutes and ss the current seconds."""
def save():
    global save_status
    global list_status
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    filename = "orders_" + stamp
    message = "Saved the current order to " + filename
    orders.append(filename)
    save_status = True
    list_status = False
    return message


""" Enter command>list
    [1] - orders_2014_03_01_11_00_08
    [2] - orders_2014_03_01_11_00_00 """
def list_orders():
    global list_status
    list_string = ""
    for i in range(len(orders)):
        order_i = "[" + str(i+1) + "] - " + orders[i]
        list_string += order_i + "\n"
    list_string = list_string[:-1]
    list_status = True
    return list_string


def finish():
    global save_status
    global list_status
    if (save_status):
        message = "Finishing order. Goodbye!"
        return message
    else:
        message = "You have not saved your order.\nIf you wish to continue, type finish again.\nIf you want to save your order, type save"
        list_status = False
        return message


def load():
    global list_status
    if (list_status):
        pass
    else:
        print("Use list command before loading")


while True:
    command = input("Enter command>")
    arguments = command.split()

    if (arguments[0] not in commands):
        print("Unknown command!\nTry one of the following:\ntake <name> <price>\n" + 
            "status\nsave\nlist\nload <number>\nfinish")

    if (arguments[0] == "finish"):
        print(finish())
        if(save_status):
            break

    if (arguments[0] == "take"):
        print(take(arguments))

    if (arguments[0] == "status"):
        print(status())

    if (arguments[0] == "save"):
        print(save())

    if (arguments[0] == "list"):
        print(list_orders())

    if (arguments[0] == "load"):
        print(load())


def main():
    pass


if __name__ == '__main__':
    main()