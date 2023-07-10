sample_list = ['triumph speed 400', 'triumph scrambler 400x ', 'royal enfield himalayan 450',
               'royal enfield gt continental 650']


def append_list(add_element):
    sample_list.append(add_element)
    print(sample_list)


def normal_addition(add_new_element):
    sample_list1 = ['triumph speed 400', 'triumph scrambler 400x ', 'royal enfield himalayan 450',
                    'royal enfield gt continental 650']

    sample_list1 = sample_list1 + [add_new_element]
    print(sample_list1)


def extend_list(extension_list):
    bike = ['triumph speed 400', 'triumph scrambler 400x ', 'royal enfield himalayan 450',
            'royal enfield gt continental 650']
    bike.extend(extension_list)
    print(bike)


def extend_list_another_type(extension):
    bike = ['triumph speed 400', 'triumph scrambler 400x ', 'royal enfield himalayan 450',
            'royal enfield gt continental 650']
    bike.extend(extension)
    print(bike)


if __name__ == '__main__':
    append_list('triumph tiger 660')
    normal_addition('Dominar 350')
    extend_list(['royal enfield scram 411', 'ducati scrambler'])
    extend_list_another_type(('royal enfield scram 411', 'ducati scrambler'))
