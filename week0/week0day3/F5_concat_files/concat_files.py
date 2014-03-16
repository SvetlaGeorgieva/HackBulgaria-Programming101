import sys


def get_content(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content


def main():
    filenames = sys.argv[1:]
    file = open("megatron.txt", "a")
    new_content = []

    for i in filenames:
        file.write(get_content(i))
        file.write("\n\n")
    file.close()

if __name__ == '__main__':
    main()