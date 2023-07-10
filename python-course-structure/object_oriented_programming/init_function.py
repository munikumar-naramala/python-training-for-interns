class Cars:
    def __init__(self, name, horses):
        self.name = name
        self.horses = horses


c1 = Cars('Zonda R', 800)

if __name__ == '__main__':
    print(c1.name)
    print(c1.horses)
