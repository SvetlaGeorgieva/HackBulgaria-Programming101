def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    if n == 2:
        return listB
    if n > 2:
        a = listA
        b = listB
        count = []
        for i in range(3, n + 1):
            count = a + b
            a = b
            b = count
        return count


def main():
    print (nth_fib_lists([1], [2], 1))
    print (nth_fib_lists([1], [2], 2))
    print (nth_fib_lists([1, 2], [1, 3], 3))
    print (nth_fib_lists([], [1, 2, 3], 4))
    print (nth_fib_lists([], [], 100))


if __name__ == '__main__':
    main()
