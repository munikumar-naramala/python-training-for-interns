class Vehicle:
    def __init__(self, brand, horses):
        self.brand = brand
        self.horses = horses

    def move(self):
        print("V6!")


class V6Car(Vehicle):
    pass


class V8Car(Vehicle):
    def move(self):
        print("V8!")


class V12Car(Vehicle):
    def move(self):
        print("V12!")


if __name__ == '__main__':
    try:

        car1 = V6Car("Porsche 911 Carreras S", 450)
        car2 = V8Car("Ford Mustang GT500", 760)
        car3 = V12Car("Aston Martin Vantage AMR", 503)

        for x in (car1, car2, car3):
            print(x.brand)
            print(x.horses)
            x.move()
    except BaseException as error:
        print('An exception occurred: {}'.format(error))
