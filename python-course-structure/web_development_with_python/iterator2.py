class HorsePowers:
    def __iter__(self):
        self.a = 800
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


if __name__ == '__main__':
    my_power = HorsePowers()
    my_iter = iter(my_power)

    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
