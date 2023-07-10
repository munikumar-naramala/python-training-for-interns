def check_if_element_in_list(bike):
    sample_list1 = ['triumph speed 400', 'triumph scrambler 400x ', 'royal enfield himalayan 450',
                    'royal enfield gt continental 650']
    if bike in sample_list1:
        print(f'{bike} is in the list')
    else:
        print(f'{bike} is not available')


if __name__ == '__main__':
    check_if_element_in_list('triumph scrambler 400x ')
    check_if_element_in_list('bajaj dominar')
