def count_consonants(str):
    consonants = "bcdfghjklmnpqrstvwxz"
    count = 0
    for i in str:
        if (i.lower() in consonants):
            count += 1
    return count

def main():
    print (count_consonants("Python"))
    print (count_consonants("Theistareykjarbunga"))
    print (count_consonants("grrrrgh!"))
    print (count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
    print (count_consonants("A nice day to code!"))


if __name__ == '__main__':
    main()
