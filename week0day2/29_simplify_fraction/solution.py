def min(a,b):
    if(a > b):
        return b
    else:
        return a

def simplify_fraction(fraction):
    a = fraction[0]
    b = fraction[1]
    min_num = min(a,b)

    for i in range(1,min_num+1):
        if(a%i == 0 and b%i == 0):
            a /= i
            b /= i

    return int(a), int(b)


def main():
    print (simplify_fraction((3,9)))
    print (simplify_fraction((1,7)))
    print (simplify_fraction((4,10)))
    print (simplify_fraction((63,462)))


if __name__ == '__main__':
    main()
