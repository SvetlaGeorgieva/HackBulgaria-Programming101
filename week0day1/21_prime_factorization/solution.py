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

def prime_factorization(n):
    prime_factors = []
    print (n)
    prime_numbers = []
    prime_count = []
    for i in range(1, n + 1):
        if(is_prime(i) and n % i == 0):
            prime_numbers.append(i)
            prime_count.append(0)
    test_num = n
    for i in range (0, len(prime_numbers)):
        while (test_num % prime_numbers[i] == 0):
            prime_count[i] += 1
            test_num /= prime_numbers[i]
    for i in range (0, len(prime_numbers)):
        prime_factors.append((prime_numbers[i], prime_count[i]))

    return prime_factors


def main():
    print (prime_factorization(10))
    print (prime_factorization(14))
    print (prime_factorization(356))
    print (prime_factorization(89))
    print (prime_factorization(1000))

if __name__ == '__main__':
    main()
