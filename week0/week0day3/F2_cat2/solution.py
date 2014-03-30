import sys


def cat2(filenames):
    content_to_print = ""
    for i in filenames:
        file = open(i, "r")
        content = file.read().split("\n")
        content_to_print += "\n".join(content)
        content_to_print += "\n\n"
        file.close()

    content_to_print = content_to_print[0:-2]
    print(content_to_print)
    return content_to_print


def main():
    filenames = []
    filenames = sys.argv[1:]
    cat2(filenames)

if __name__ == '__main__':
    main()
