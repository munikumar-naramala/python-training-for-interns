import sys


def modules():
    print(sys.path)
    print("------------")

    # searches through these paths for the modules


def imported_example():
    import calc
    print(calc.calc(2, 3))
    print("_-------------")


def built_in():
    import math

    print(math.sqrt(25))

    print(math.pi)

    print(math.factorial(4))

    from datetime import date
    import time

    print(time.time())

    print(date.fromtimestamp(454554))
    print("-------------")


def from_module():
    from random import randint
    print(randint(2, 5))


if __name__ == '__main__':
    modules()
    imported_example()
    built_in()
    from_module()
