import sys


def get_content(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content


def concatenate(filenames, filename_to_write):
    file = open(filename_to_write, "a")

    for i in filenames:
        file.write(get_content(i))
        file.write("\n\n")
    file.close()

    file = open(filename_to_write, "r")
    content = file.read()
    file.close()
    return content


def main():
    filenames = sys.argv[1:]
    filename_to_write = "megatron.txt"
    concatenate(filenames, filename_to_write)

if __name__ == '__main__':
    main()
