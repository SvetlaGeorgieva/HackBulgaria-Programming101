def calculate_coins(sum):
    coin_numbers = [100, 50, 20, 10, 5, 2, 1]
    coin_count = [0]*7
    coin_dict = {1: 0, 2: 0, 100: 0, 5: 0, 10: 0, 50: 0, 20: 0}
    test_sum = sum * 100
    for i in range (0, len(coin_numbers)):
        while (test_sum >= coin_numbers[i]):
            coin_count[i] += 1
            test_sum -= coin_numbers[i]
    for i in range (0, len(coin_numbers)):
        coin_dict[coin_numbers[i]] = coin_count[i]
    return coin_dict

def main():
    print(calculate_coins(0.53))
    print(calculate_coins(8.94))

if __name__ == '__main__':
    main()