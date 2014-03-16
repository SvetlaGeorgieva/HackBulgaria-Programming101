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

def prime_number_of_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if (n % i == 0):
            count += 1
    return is_prime(count)

def main():
    print (prime_number_of_divisors(7))
    print (prime_number_of_divisors(8))
    print (prime_number_of_divisors(9))

if __name__ == '__main__':
    main()
