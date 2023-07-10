class Cars:
    def __init__(self, name, horses):
        self.name = name
        self.horses = horses

    def func1(self):
        print("The best car is " + self.name + " " + str(self.horses))


class V8Cars(Cars):
    def __init__(self, name, horses, top_speed):
        self.top_speed = top_speed
        super().__init__(name, horses)
        # self.top_speed = 298

    def func2(self):
        print(f"The car {self.name} has a top speed {self.top_speed}")


if __name__ == '__main__':
    c1 = V8Cars("Ford Mustang Shelby GT500", 760, 298)
    c1.func1()
    c1.func2()
