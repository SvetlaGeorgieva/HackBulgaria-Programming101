def oned_robot(a, minA, maxB):
    position = 0
    for i in a:
        if(i == "R" and position < maxB):
            position += 1
        if(i == "L" and position > (minA * (-1))):
            position -= 1
    return position


def main():
    print (oned_robot("RRLRRLLR", 10, 10)) # 2
    print (oned_robot("RRRRR", 3, 4)) # 4
    print (oned_robot("LLLLLLLLLLR", 2, 6)) # -1
    print (oned_robot("RRRRRRRLRRLRRRRRRRRRRRRLRLRRRRRRRRLRRRRRLRRRRRRRRR", 5, 20)) # 20
    print (oned_robot("RLRLLLLLLLRLLLRLLLLLLLLRLLLLLRLLLRRLLLLLRLLLLLRLLL", 34, 15)) # -30


if __name__ == '__main__':
    main()
