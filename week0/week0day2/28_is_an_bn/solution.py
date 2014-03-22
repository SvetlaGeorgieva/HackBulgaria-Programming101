def is_an_bn(word):
    n = len(word)//2
    if(len(word) != n*2):
        return False
    else:
        word_str = "a"*n + "b"*n
        if(word_str == word):
            return True
        else:
            return False


def main():
    print (is_an_bn(""))
    print (is_an_bn("rado"))
    print (is_an_bn("aaabb"))
    print (is_an_bn("aaabbb"))
    print (is_an_bn("aabbaabb"))
    print (is_an_bn("bbbaaa"))
    print (is_an_bn("aaaaabbbbb"))


if __name__ == '__main__':
    main()
