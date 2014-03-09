def magic_square(matrix):
    n = len(matrix)

    the_sum = 0
    for i in range(n):
        the_sum += matrix[0][i]

    #sum of rows:
    for i in range(n):
        sum_rowi = 0
        for j in range(n):
            sum_rowi += matrix[i][j]
        if (sum_rowi != the_sum):
            return False

    #sum of columns:
    for j in range(n):
        sum_colj = 0
        for i in range(n):
            sum_colj += matrix[i][j]
        if (sum_colj != the_sum):
            return False

    #sum of main diagonals:
    sum_d1 = 0
    sum_d2 = 0
    for i in range(n):
        sum_d1 += matrix[i][i]
        sum_d2 += matrix[i][n - i - 1]
    if (sum_d1 != the_sum or sum_d2 != the_sum):
        return False

    return True


def main():
    print (magic_square([[1,2,3], [4,5,6], [7,8,9]])) # False
    print (magic_square([[4,9,2], [3,5,7], [8,1,6]])) # True
    print (magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]])) # True
    print (magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]])) # True
    print (magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]])) # False


if __name__ == '__main__':
    main()
