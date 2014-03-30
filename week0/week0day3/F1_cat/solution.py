import sys


def cat(filename):
    file = open(filename, "r")
    content = file.read().split("\n")
    content_to_print = "\n".join(content)
    print(content_to_print)
    file.close()

    return content_to_print


def main():
    filename = sys.argv[1]
    cat(filename)


if __name__ == '__main__':
    main()
