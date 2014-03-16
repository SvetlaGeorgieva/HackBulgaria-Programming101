import sys

from time import time
from datetime import datetime

#ts = time()
#stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')

#Enter command>take Rado 10.0
#Taking order from Rado for 10.00


def take(args):
    name = args[1]
    money = args[2]
    current_order = "Taking order from " + name + " for " + money
    return current_order





while True:
    command = input("Enter command>")
    args = []
    args = sys.argv[1:]
    print(take(args))

    if (command == "finish"):
        break


def main():
    pass


if __name__ == '__main__':
    main()