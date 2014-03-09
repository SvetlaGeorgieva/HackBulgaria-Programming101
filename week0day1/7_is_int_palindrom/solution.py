def is_int_palindrom(n):
    a = str(n)
    num_length = len(a)
    if (num_length == 1):
        return True
    for i in range(0, num_length // 2):
        if (a[i] != a[num_length - i - 1]):
            return False
        else:
            return True


def main():
    print (is_int_palindrom(1))
    print (is_int_palindrom(42))
    print (is_int_palindrom(100001))
    print (is_int_palindrom(999))
    print (is_int_palindrom(123))

if __name__ == '__main__':
    main()
