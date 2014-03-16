def list_to_number(digits):
    digit_str = ""
    for i in digits:
        digit_str += str(i)
    return int(digit_str)


def main():
    print (list_to_number([1,2,3]))
    print (list_to_number([9,9,9,9,9]))
    print (list_to_number([1,2,3,0,2,3]))


if __name__ == '__main__':
    main()
