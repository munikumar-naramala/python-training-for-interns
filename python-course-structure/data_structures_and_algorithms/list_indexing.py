list1 = ['Max', 'Ham', 'Danny', 'Kimi', 'Lando', 'Stroll']


def list_index():
    first_element = list1[0]
    last_element = list1[-1]
    print(first_element, last_element)
    print('---------')


def get_index():
    order = ['Max', 'Ham', 'Danny']
    print(order.index('Max'))
    print("---------")


def range_of_indexes():
    print(list1[1:4])
    print("---------")


def negative_indexing():
    print(list1[-4:-1])
    print("-----------")


if __name__ == '__main__':
    list_index()
    get_index()
    range_of_indexes()
    negative_indexing()
