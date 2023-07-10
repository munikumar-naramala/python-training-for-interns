class Cars:
    def __init__(self, name, horses):
        self.name = name
        self.horses = horses

    def func1(self):
        print("The best car is " + self.name + " " + str(self.horses))


class V8Cars(Cars):
    def __init__(self, name, horses):
        super().__init__(name, horses)
        self.top_speed = 298


if __name__ == '__main__':
    c1 = V8Cars("Ford Mustang Shelby GT500", 760)
    c1.func1()
