class Base:
    def __init__(self):
        self._a = 'Volkswagen'


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self._a)

        self._a = 'Audi'
        print("Calling modified protected member outside class: ",
              self._a)


if __name__ == '__main__':
    obj1 = Derived()

    obj2 = Base()
