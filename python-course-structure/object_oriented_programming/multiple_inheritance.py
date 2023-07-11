class Car:
    @staticmethod
    def car_info():
        print("This is my car")


class Bike:
    @staticmethod
    def bike_info():
        print("This is my bike")


class Info(Car, Bike):
    pass


if __name__ == '__main__':
    try:
        b1 = Info()

        b1.car_info()
        b1.bike_info()
    except BaseException as error:
        print('An exception occurred: {}'.format(error))
