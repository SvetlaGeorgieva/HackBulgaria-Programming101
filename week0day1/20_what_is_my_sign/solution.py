def what_is_my_sign(day, month):
    zodiac = {
        "Aeries": [(21,3), (20,4)],
        "Taurus": [(21,4),(21,5)],
        "Gemini": [(22,5),(21,6)],
        "Cancer": [(22,6),(22,7)],
        "Leo": [(23,7),(22,8)],
        "Virgo": [(23,8),(23,9)],
        "Libra": [(24,9),(23,10)],
        "Scorpio": [(24,10),(22,11)],
        "Sagittarius": [(23,11),(21,12)],
        "Capricorn": [(22,12),(20,1)],
        "Aquarius": [(21,1),(19,2)],
        "Pisces": [(20,2),(20,3)]
    }
    for key in zodiac:
        end_month = zodiac[key][1][1]
        start_month = zodiac[key][0][1]
        end_day = zodiac[key][1][0]
        start_day = zodiac[key][0][0]
        if(month == end_month and day <= end_day):
            return key
        if(month == start_month and day >= start_day):
            return key


def main():
    print (what_is_my_sign(5, 8))
    print (what_is_my_sign(29, 1))
    print (what_is_my_sign(30, 6))
    print (what_is_my_sign(31, 5))
    print (what_is_my_sign(2, 2))
    print (what_is_my_sign(8, 5))
    print (what_is_my_sign(9, 1))

if __name__ == '__main__':
    main()
