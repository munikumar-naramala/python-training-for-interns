def change_tuple():
    tup = ('himalayan', 'tiger', 'gt', 'himalayan', 'speed', 'scrambler')
    list1 = list(tup)
    list1[3] = 'speed twin'
    new_tup = tuple(list1)
    print(new_tup)


if __name__ == '__main__':
    change_tuple()
