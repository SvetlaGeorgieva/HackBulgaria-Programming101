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

def main():
    print (is_prime(1))
    print (is_prime(2))
    print (is_prime(8))
    print (is_prime(11))
    print (is_prime(-10))

if __name__ == '__main__':
    main()
