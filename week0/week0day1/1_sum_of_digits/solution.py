def sum_of_digits(n):
    a = str(n)
    count = 0
    for i in a:
        if (i != '-'):
            count += int(i)
    return count

def main():
    print (sum_of_digits(1325132435356))
    print (sum_of_digits(123))
    print (sum_of_digits(6))
    print (sum_of_digits(-10))

if __name__ == '__main__':
    main()
