import sys


def get_content(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content


def sum_numbers(filename):
    file_content = get_content(filename)
    num_list = file_content.split(" ")

    sum_of_numbers = 0
    for i in num_list:
        sum_of_numbers += int(i)
    print(sum_of_numbers)
    return sum_of_numbers


def main():
    filename = sys.argv[1]
    sum_numbers(filename)


if __name__ == '__main__':
    main()
