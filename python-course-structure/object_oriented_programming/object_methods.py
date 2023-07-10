class Car:
    def __init__(self, name, horses):
        self.name = name
        self.horses = horses

    def func1(self):
        print("The beset car is " + self.name + " " + str(self.horses))


if __name__ == '__main__':
    p1 = Car("Pagani Zonda R ", 800)
    p1.func1()
