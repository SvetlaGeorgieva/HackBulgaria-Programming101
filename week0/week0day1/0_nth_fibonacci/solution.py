def nth_fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        a = 1
        b = 1
        count = 0
        for i in range(3, n + 1):
            count = a + b
            a = b
            b = count
        return count

def main():
    print (nth_fibonacci(1))
    print (nth_fibonacci(2))
    print (nth_fibonacci(3))
    print (nth_fibonacci(10))

if __name__ == '__main__':
    main()
