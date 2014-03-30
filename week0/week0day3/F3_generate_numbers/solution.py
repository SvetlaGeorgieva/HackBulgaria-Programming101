import sys
from random import randint


def generate_numbers(filename, number):
    file = open(filename, "w")
    content = []

    for i in range(int(number)):
        num = (randint(1, 1000))
        content.append(str(num))

    content = " ".join(content)
    file.write(content)
    file.close()
    print(content)
    return content


def main():
    filename = sys.argv[1]
    number = sys.argv[2]
    generate_numbers(filename, number)

if __name__ == '__main__':
    main()
