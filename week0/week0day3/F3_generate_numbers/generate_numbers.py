import sys
from random import randint


def main():
    filename = sys.argv[1]
    number = sys.argv[2]
    file = open(filename, "w")
    content = []

    for i in range(int(number)):
        from random import randint
        num = (randint(1, 1000))
        content.append(str(num))

    file.write(" ".join(content))
    print(" ".join(content))
    file.close()

if __name__ == '__main__':
    main()