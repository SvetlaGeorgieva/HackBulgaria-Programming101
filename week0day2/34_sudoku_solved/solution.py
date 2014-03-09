def check(arr):
    for key in arr:
        if(arr[key] != 1):
            return False
        else:
            return True

def subgrid(a,b, sudoku):
    arr_ab = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    list_ab = []
    for i in range(3):
        for j in range(3):
            num = sudoku[a+i][b+j]
            list_ab.append(num)
    for num in list_ab:
        if num in arr_ab:
            arr_ab[num] += 1
    return arr_ab

def sudoku_solved(sudoku):
    arr = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    #sum of rows:
    for i in range(9):
        for key in arr:
            arr[key] = 0
        for j in range(9):
            if(sudoku[i][j] in arr.keys()):
                num = sudoku[i][j]
                arr[num] += 1
        if(check(arr) == False):
            return False

    #sum of columns:
    for j in range(9):
        for key in arr:
            arr[key] = 0
        for i in range(9):
            if(sudoku[i][j] in arr.keys()):
                num = sudoku[i][j]
                arr[num] += 1
        if(check(arr) == False):
            return False

    #sum of subgrids:
    subgrids = []
    subgrids.append(check(subgrid(0,0, sudoku)))
    subgrids.append(check(subgrid(0,3, sudoku)))
    subgrids.append(check(subgrid(0,6, sudoku)))
    subgrids.append(check(subgrid(3,0, sudoku)))
    subgrids.append(check(subgrid(3,3, sudoku)))
    subgrids.append(check(subgrid(3,6, sudoku)))
    subgrids.append(check(subgrid(6,0, sudoku)))
    subgrids.append(check(subgrid(6,3, sudoku)))
    subgrids.append(check(subgrid(6,6, sudoku)))
    for result in subgrids:
        if(result == False):
            return False

    return True


def main():
    print (sudoku_solved([
[4, 5, 2, 3, 8, 9, 7, 1, 6],
[3, 8, 7, 4, 6, 1, 2, 9, 5],
[6, 1, 9, 2, 5, 7, 3, 4 ,8],
[9, 3, 5, 1, 2, 6, 8, 7, 4],
[7, 6, 4, 9, 3, 8, 5, 2, 1],
[1, 2, 8, 5, 7, 4, 6, 3, 9],
[5, 7, 1, 8, 9, 2, 4, 6, 3],
[8, 9, 6, 7, 4, 3, 1, 5 ,2],
[2, 4, 3, 6, 1, 5, 9, 8, 7]
])) # True
    print (sudoku_solved([
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9]
])) #False


if __name__ == '__main__':
    main()
