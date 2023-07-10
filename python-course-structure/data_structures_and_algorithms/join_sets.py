def union_set():
    bikes = {'himalayan', 'tiger', 'gt'}
    bikes2 = {'speed twin', 'speed', 'scrambler'}
    new_bikes = bikes.union(bikes2)
    print(new_bikes)

def intersection_update():
    bikes1 = {'himalayan', 'tiger', 'gt'}
    bikes3 = {'speed twin', 'speed', 'scrambler', 'himalayan'}
    new_bikes1 = bikes1.intersection(bikes3)
    print(new_bikes1)

def symmetric_difference_set():
    bikes1 = {'himalayan', 'tiger', 'gt'}
    bikes3 = {'speed twin', 'speed', 'scrambler', 'himalayan'}
    new_bikes1 = bikes1.symmetric_difference(bikes3)
    print(new_bikes1)


if __name__ == '__main__':
    union_set()
    intersection_update()
    symmetric_difference_set()
