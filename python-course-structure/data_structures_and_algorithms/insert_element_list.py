def insert_into_list(index, element):
    bikes = ['re', 'bajaj', 'bmw']
    bikes.insert(index, element)
    print(bikes)


def reverse_list():
    bikes = ['re', 'bajaj', 'bmw']
    bikes.reverse()
    print(bikes)


if __name__ == '__main__':
    insert_into_list(2, 'triumph')
    reverse_list()
