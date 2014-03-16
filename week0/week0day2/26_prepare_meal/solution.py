def prepare_meal(n):
    meal = ""
    spam = ""
    eggs = ""
    meal_numbers = {3: 0, 5: 0}
    test_num = n

    for key in meal_numbers:
        while (test_num % key == 0):
            meal_numbers[key] += 1
            test_num /= key

    spam_list = ["spam"]*meal_numbers[3]
    spam = " ".join(spam_list)
    if(meal_numbers[5] != 0):
        eggs = " and eggs"

    if(meal_numbers[5] != 0 and meal_numbers[3] == 0):
        meal = "eggs"
    else:
        meal = spam + eggs
    
    return n, meal


def main():
    print (prepare_meal(5)) #"eggs"
    print (prepare_meal(3)) #"spam"
    print (prepare_meal(27)) #"spam spam spam"
    print (prepare_meal(15)) #"spam and eggs"
    print (prepare_meal(45)) #"spam spam and eggs"
    print (prepare_meal(7)) #""


if __name__ == '__main__':
    main()
