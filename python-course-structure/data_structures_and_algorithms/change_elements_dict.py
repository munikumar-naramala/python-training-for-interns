dict1 = {'cafe': 'continental', 'scrambler': 'triumph', 'adventure': 'himalayan'}


def change_value(value):
    dict1['cafe'] = value
    print(dict1)


def check_key(key):
    if key in dict1:
        print('key exists in dict1')


if __name__ == '__main__':
    change_value('interceptor')
    check_key('adventure')

