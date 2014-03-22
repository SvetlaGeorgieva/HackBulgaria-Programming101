import sys

def get_content(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

def main():
    command = sys.argv[1]
    filename = sys.argv[2]
    file_content = get_content(filename)
    
    lines = file_content.split("\n")
    lines_count = len(lines)

    words_string = ""
    for i in lines:
        if(i != ""):
            words_string += i + " "

    words = words_string.split(" ")
    words_count = len(words) - 1

    chars_count = 0
    for i in words:
        chars_count += len(i)

    if(command == "lines"):
        print(lines_count)
    elif(command == "words"):
        print(words_count)
    else:
        print(chars_count)


if __name__ == '__main__':
    main()