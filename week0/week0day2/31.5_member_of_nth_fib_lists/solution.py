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

def member_of_nth_fib_lists(listA, listB, needle):
    if(needle == listA or needle == listB):
        return True

    needle_length = len(needle)
    length = 0

    while ( length <= needle_length):
        for i in range(1, needle_length + 1):
            needle_i = nth_fib_lists(listA, listB, i)
            if (needle_i == needle):
                return True
            else:
                length = len(needle_i)
        return False


def main():
    print (member_of_nth_fib_lists([1, 2], [3, 4], [5, 6])) #False
    print (member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4])) #True
    print (member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2])) #True
    print (member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7])) #False


if __name__ == '__main__':
    main()
