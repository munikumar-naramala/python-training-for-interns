def ex1(my_cars):
    iter_cars = iter(my_cars)

    print(next(iter_cars))
    print(next(iter_cars))


def ex2(my_car):
    iter_car = iter(my_car)
    print(next(iter_car))
    print(next(iter_car))


if __name__ == '__main__':
    ex1(['Porsche 911', 'Zonda R', 'm5 competition'])
    ex2('Zonda')
