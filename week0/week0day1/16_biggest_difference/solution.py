def biggest_difference(arr):
    min = arr[0]
    max = arr[0]
    for i in arr:
        if (i < min):
            min = i
        if (i > max):
            max = i
    return min - max


def main():
    print (biggest_difference([1,2]))
    print (biggest_difference([1,2,3,4,5]))
    print (biggest_difference([-10, -9, -1]))
    print (biggest_difference(range(100)))


if __name__ == '__main__':
    main()
