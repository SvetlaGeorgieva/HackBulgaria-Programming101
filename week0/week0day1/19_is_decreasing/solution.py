def is_decreasing(seq):
    min = seq[0]
    for i in range(1, len(seq)):
        if(seq[i] >= seq[i - 1]):
            return False
    return True


def main():
    print (is_decreasing([5,4,3,2,1]))
    print (is_decreasing([1,2,3]))
    print (is_decreasing([100, 50, 20]))
    print (is_decreasing([1,1,1,1]))

if __name__ == '__main__':
    main()
