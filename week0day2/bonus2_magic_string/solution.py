def magic_string(a):
    n = len(a)
    count = 0
    for i in range(0, n//2):
        if (a[i] == "<"):
            count += 1

    for i in range(n//2 , n):
        if (a[i] == ">"):
            count += 1

    return count



def main():
    print (magic_string(">><<><")) # 2
    print (magic_string(">>>><<<<")) # 0
    print (magic_string("<<>>")) # 4
    print (magic_string("<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><")) # 20


if __name__ == '__main__':
    main()
