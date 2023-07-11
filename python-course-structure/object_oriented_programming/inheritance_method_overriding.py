class Cars:
    def __init__(self, name, horses):
        self.name = name
        self.horses = horses

    def func1(self):
        print("The best car is " + self.name + " " + str(self.horses))

    def horse(self):
        print('the amount of horses is crazy')


class V8Cars(Cars):
    def __init__(self, name, horses):
        self.name = name
        self.horses = horses
        Cars.__init__(self, name, horses)

    def func1(self):
        print(f'The horses produced is {self.horses} by the car {self.name}.')

    def horse(self):
        super().horse()


if __name__ == '__main__':
    try:
        c1 = V8Cars("Ford Mustang Shelby GT500", 760)
        c1.func1()
        c1.horse()
    except BaseException as error:
        print('An exception occurred: {}'.format(error))

# while method overriding, the same method in both parent and child class,
# the method in the child class executes
