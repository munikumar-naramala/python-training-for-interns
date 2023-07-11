def example(num):
    list1 = [i for i in range(num)]
    print(list1)
    print("------------")


def example2(element):
    bikes = ['triumph speed 400', 'triumph scrambler 400x ', 'royal enfield himalayan 450',
             'royal enfield gt continental 650']
    new_list = [element for element in bikes]
    new_list2 = ['waylay' if bike == 'triumph speed 400' else element for bike in bikes]
    print(new_list)
    print(new_list2)
    print("------------")


if __name__ == '__main__':
    example(10)
    example2('wool')
