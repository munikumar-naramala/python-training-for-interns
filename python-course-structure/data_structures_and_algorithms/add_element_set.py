def add_elements_set(element):
    bikes = {'himalayan', 'tiger', 'gt', 'speed twin', 'speed', 'scrambler'}
    bikes.add(element)
    print(bikes)


def set_plus_set(set2):
    bikes = {'himalayan', 'tiger', 'gt', 'speed twin', 'speed', 'scrambler'}
    bikes.update(set2)
    print(bikes)


def set_plus_any_storage(additional_storage):
    bikes = {'himalayan', 'tiger', 'gt', 'speed twin', 'speed', 'scrambler'}
    bikes.update(additional_storage)
    print(bikes)


if __name__ == '__main__':
    add_elements_set('urban motor')
    set_plus_set({'icon dark', 'desert sled'})
    set_plus_any_storage(['1100 dark pro', 'a ride in the night'])
