def add_element(element):
    tup = ('himalayan', 'tiger', 'gt', 'speed twin', 'speed', 'scrambler')
    list1 = list(tup)
    list1.append(element)
    new_tuple = tuple(list1)
    print(new_tuple)


def tuple_plus_tuple(tup2):
    tup = ('himalayan', 'tiger', 'gt', 'speed twin', 'speed', 'scrambler')
    new_tup = tup + tup2
    print(new_tup)


if __name__ == '__main__':
    add_element('urban motard')
    tuple_plus_tuple(('city monster',))
