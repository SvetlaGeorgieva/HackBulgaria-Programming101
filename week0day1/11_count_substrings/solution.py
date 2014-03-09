def count_substrings(haystack, needle):
    index = haystack.find(needle, 0)
    if (index == -1):
        return 0
    else:
        count = 0
        needle_length = len(needle)
        while (index < len(haystack) + 1):
            if (haystack.find(needle, index) != -1):
                index1 = haystack.find(needle, index)
                count += 1
                index = index1 + needle_length
            else:
                break
        return count


def main():
    print (count_substrings("This is a test string", "is"))
    print (count_substrings("babababa", "baba"))
    print (count_substrings("Python is an awesome language to program in!", "o"))
    print (count_substrings("We have nothing in common!", "really?"))
    print (count_substrings("This is this and that is this", "this"))


if __name__ == '__main__':
    main()
