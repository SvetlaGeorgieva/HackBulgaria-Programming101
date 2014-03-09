def contains_digit(number, digit):
    num_string = str(number)
    for i in num_string:
        if (int(i) == digit):
            return True
    return False

def contains_digits(number, digits):
    if(len(digits) == 0):
        return False
    for digit in digits:
        if(contains_digit(number, digit) == False):
            return False
    return True

def main():
    print (contains_digits(402123, [0, 3, 4]))
    print (contains_digits(666, [6,4]))
    print (contains_digits(123456789, [1,2,3,0]))
    print (contains_digits(456, []))

if __name__ == '__main__':
    main()
