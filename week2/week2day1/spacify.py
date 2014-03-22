import sys
from string_utils import tabs_to_spaces

def spacify(filename):
    file = open(filename, "r")
    content = file.read()
    new_content = tabs_to_spaces(content, 4)
    file.close()

    file = open(filename, "w")
    file.write(new_content)
    file.close()

def main():
    filename = sys.argv[1]
    spacify(filename)


if __name__ == '__main__':
    main()