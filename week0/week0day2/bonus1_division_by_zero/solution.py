def division_by_zero(arr):
    n = len(arr)
    if (n == 0 or n == 1):
        return n
    else:
        i = 0
        while(i < n):
            j = 0
            
            while (j < n):
                if (arr[i] > arr[j]):
                    new_num = arr[i]//arr[j]
                    if new_num not in arr:
                        arr.append(new_num)
                        i = -1
                        n = len(arr)
                        break
                    else:
                        j += 1
                else:
                    j += 1

            i += 1

    return n


def main():
    print (division_by_zero([9, 2])) # 3
    print (division_by_zero([8, 2])) # 3
    print (division_by_zero([50])) # 1
    print (division_by_zero([1, 5, 8, 30, 15, 4])) # 11
    print (division_by_zero([1, 2, 4, 8, 16, 32, 64])) # 7
    print (division_by_zero([6, 2, 18])) # 7


if __name__ == '__main__':
    main()
