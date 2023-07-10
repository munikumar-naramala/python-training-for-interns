def dictionary():
    dict1 = {'cafe': 'continental', 'scrambler': 'triumph', 'adventure': 'himalayan'}
    print(dict1)


def get_item(key):
    dict1 = {'cafe': 'continental', 'scrambler': 'triumph', 'adventure': 'himalayan'}
    d = dict1.get(key)
    print(d)


def get_keys():
    dict1 = {'cafe': 'continental', 'scrambler': 'triumph', 'adventure': 'himalayan'}
    d = dict1.keys()
    print(d)


def get_values():
    dict1 = {'cafe': 'continental', 'scrambler': 'triumph', 'adventure': 'himalayan'}
    d = dict1.values()
    print(d)


if __name__ == '__main__':
    dictionary()
    get_item('scrambler')
    get_keys()
    get_values()
