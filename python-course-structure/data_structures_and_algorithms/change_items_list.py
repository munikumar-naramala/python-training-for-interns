def change_items(replace_element):
    motorcycles = ['triumph speed 400', 'triumph scrambler 400x ', 'royal enfield himalayan 450',
                   'royal enfield gt continental 650']
    motorcycles[1] = replace_element
    print(motorcycles)


def change_items_in_a_range(additional_element1, adele2, adele3):
    cars = ['volkswagen', 'mahindra', 'skoda', 'suzuki']
    cars[1:4] = additional_element1, adele2, adele3
    print(cars)


if __name__ == '__main__':
    change_items('bajaj triumph scrambler 400x')
    change_items_in_a_range('mc laren', 'ferrari', 'aston martin')
