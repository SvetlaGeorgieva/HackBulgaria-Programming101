def slope_style_score(scores):
    min = scores[0]
    max = scores[0]
    sum = 0
    for i in scores:
        sum += i
        if (i < min):
            min = i
        if (i > max):
            max = i
    end_score = (sum - min - max)/(len(scores) - 2)
    return float(int(end_score * 100)/100)


def main():
    print (slope_style_score([94, 95, 95, 95, 90]))
    print (slope_style_score([60, 70, 80, 90, 100]))
    print (slope_style_score([96, 95.5, 93, 89, 92]))


if __name__ == '__main__':
    main()
