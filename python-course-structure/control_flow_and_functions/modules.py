def modules():
    import sys
    print(sys.path)
    print("------------")

    # searches through these paths for the modules

    def imported_example():
        import calc
        print(calc.calc(2, 3))
        print("_-------------")

    imported_example()

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

    built_in()

    def from_module():
        from random import randint
        print(randint(2, 5))

    from_module()


if __name__ == '__main__':
    modules()
