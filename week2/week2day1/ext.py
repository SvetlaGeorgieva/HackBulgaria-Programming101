import sys

def extension(file_extension):
    file = open(filename, "r")
    content = file.read()
    new_content = tabs_to_spaces(content, 4)
    file.close()

    file = open(filename, "w")
    file.write(new_content)
    file.close()

def main():
    file_extension = sys.argv[1]
    extension(file_extension)


if __name__ == '__main__':
    main()