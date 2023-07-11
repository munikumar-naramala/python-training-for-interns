class SuperCars:

    @staticmethod
    def super_car():
        print("Super Cars are super")


class RaceCars(SuperCars):
    @staticmethod
    def race_cars():
        print("Race cars are modified")


class RoadsterCars(RaceCars):

    @staticmethod
    def road_cars():
        print("Road cars are affordable")


if __name__ == '__main__':
    try:
        d2 = RoadsterCars()
        d2.super_car()

        d2.race_cars()

        d2.road_cars()
    except BaseException as error:
        print('An exception occurred: {}'.format(error))
