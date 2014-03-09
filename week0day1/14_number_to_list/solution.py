def number_to_list(n):
    n_str = str(n)
    n_list = []
    for i in n_str:
        n_list.append(int(i))
    return n_list

def main():
    print (number_to_list(123))
    print (number_to_list(99999))
    print (number_to_list(123023))


if __name__ == '__main__':
    main()
