def unique_words_count(arr):
    words_dict = {}
    for i in arr:
        if i in words_dict:
            words_dict[i] += 1
        else:
            words_dict[i] = 1
    return len(words_dict)

def main():
    print(unique_words_count(["apple", "banana", "apple", "pie"]))
    print(unique_words_count(["python", "python", "python", "ruby"]))
    print(unique_words_count(["HELLO!"] * 10))

if __name__ == '__main__':
    main()                             