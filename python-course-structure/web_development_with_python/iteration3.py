class HorsePower:
    def __iter__(self):
        self.a = 800
        return self

    def __next__(self):
        if self.a <= 1000:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


if __name__ == '__main__':
    my_power = HorsePower()
    my_iter = iter(my_power)

    for x in my_iter:
        print(x)
