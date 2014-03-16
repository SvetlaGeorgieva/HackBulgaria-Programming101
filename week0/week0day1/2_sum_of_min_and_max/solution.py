def sum_of_min_and_max(lst):
    min = lst[0]
    max = lst[0]
    for i in lst:
        if (i < min):
            min = i
        if (i > max):
            max = i
    return min + max


def main():
    print (sum_of_min_and_max([1,2,3,4,5,6,8,9]))
    print (sum_of_min_and_max([-10,5,10,100]))
    print (sum_of_min_and_max([1]))

if __name__ == '__main__':
    main()
