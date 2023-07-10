def for_loop():
    bikes = ['triumph speed 400', 'triumph scrambler 400x ', 'royal enfield himalayan 450',
             'royal enfield gt continental 650']
    for bike in bikes:
        print(bike)
    print("-------------")


def loop_index():
    bikes = ['triumph speed 400', 'triumph scrambler 400x ', 'royal enfield himalayan 450',
             'royal enfield gt continental 650']
    for i in range(len(bikes)):
        print(bikes[i])
    print("-------------")


def while_loop_list():
    bikes = ['triumph speed 400', 'triumph scrambler 400x ', 'royal enfield himalayan 450',
             'royal enfield gt continental 650']
    i = 0
    while i < len(bikes):
        print(bikes[i])
        i += 1
    print("--------------")


def list_comprehension_loop():
    bikes = ['triumph speed 400', 'triumph scrambler 400x ', 'royal enfield himalayan 450',
             'royal enfield gt continental 650']
    [print(bike) for bike in bikes]


if __name__ == '__main__':
    for_loop()
    loop_index()
    while_loop_list()
    list_comprehension_loop()
