def is_number_balanced(n):
    a = str(n)
    num_length = len(a)
    if (num_length == 1):
        return True
    else:
        sum_left = 0
        sum_right = 0
        for i in range(0, num_length // 2):
            sum_left += int(a[i])
        if (num_length % 2 == 0):
            for i in range((num_length // 2 ), num_length):
                sum_right += int(a[i])
        else:
            for i in range((num_length // 2 + 1), num_length):
                sum_right += int(a[i])
        if (sum_left == sum_right):
            return True
        else:
            return False


def main():
    print (is_number_balanced(9))
    print (is_number_balanced(11))
    print (is_number_balanced(13))
    print (is_number_balanced(121))
    print (is_number_balanced(4518))
    print (is_number_balanced(28471))
    print (is_number_balanced(1238033))


if __name__ == '__main__':
    main()
