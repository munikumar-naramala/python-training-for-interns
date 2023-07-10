def list_comprehension1():
    bikes = ['triumph speed 400', 'triumph scrambler 400x ', 'royal enfield himalayan 450',
             'royal enfield gt continental 650']
    new_list = [bike for bike in bikes if bike in bikes]
    print(new_list)
    print("-----------")


def excluding_an_element(element):
    bikes = ['triumph speed 400', 'triumph scrambler 400x ', 'royal enfield himalayan 450',
             'royal enfield gt continental 650']
    new_list = [bike for bike in bikes if bike != element]
    print(new_list)
    print("------------")


if __name__ == '__main__':
    list_comprehension1()
    excluding_an_element('royal enfield himalayan 450')
