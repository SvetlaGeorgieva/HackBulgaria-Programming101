import math

def is_prime(n):
    if(n < 0):
        n *= -1
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        count = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if (n % i == 0):
                count += 1
        if (count > 1):
            return False
        else:
            return True

def goldbach(n):
    prime_tuples = []
    for i in range(1, n//2 + 1):
        if(is_prime(i) and is_prime(n - i)):
            a = (i, n - i)
            prime_tuples.append (a)
    return prime_tuples


def main():
    print (goldbach(4)) # [(2,2)]
    print (goldbach(6)) # [(3,3)]
    print (goldbach(8)) # [(3,5)]
    print (goldbach(10)) # [(3,7), (5,5)]
    print (goldbach(100)) # [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]


if __name__ == '__main__':
    main()
