def format1(top_speed):
    str1 = 'ferrari 812 superfast 789hp, top_speed: {}, 3.4 sec'
    print(str1.format(top_speed))


def format2(horsepower, top_speed, time):
    str1 = 'ferrari 812 superfast {} hp, top_speed: {}, {} sec'
    print(str1.format(horsepower, top_speed, time))


if __name__ == '__main__':
    format1(340)
    format2(789, 340, 3.4)
