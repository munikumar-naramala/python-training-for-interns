class Cars:
    def __init__(self, name, horses):
        self.name = name
        self.horses = horses

    def __str__(self):
        return f'{self.name}({self.horses})'


if __name__ == '__main__':
    c1 = Cars('zonda R', 800)
    print(c1)
