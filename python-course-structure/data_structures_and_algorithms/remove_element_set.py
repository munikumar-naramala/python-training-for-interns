def discard_set(element):
    bikes = {'himalayan', 'tiger', 'gt', 'speed twin', 'speed', 'scrambler'}
    bikes.discard(element)
    print(bikes)
    bikes.remove('continental')


if __name__ == '__main__':
    discard_set('speed')
    discard_set('continental')

# remove will raise an error if the element does not exist
# discard will not raise an error
