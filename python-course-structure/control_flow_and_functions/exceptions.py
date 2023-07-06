def exception_handling():
    # run time errors are exceptions
    # print(2 / 0)

    def try_except():
        try:
            numerator = 10
            denominator = 0

            result = numerator / denominator

            print(result)
        except:
            print("Error: Denominator cannot be 0.")
    try_except()
    print("------------")

    def more_than_one_expect():
        try:
            drivers = ['max', 'kimi', 'alonso']
            print(drivers[4])
        except ZeroDivisionError:
            print("Denominator cannot be zero")
        except IndexError:
            print("List index out of bound")
    more_than_one_expect()
    print("_--------------")

    def try_finally():
        try:
            numerator = 10
            denominator = 0

            result = numerator / denominator

            print(result)
        except:
            print("Error: Denominator cannot be 0.")

        finally:
            print("This is finally block.")
    try_finally()


if __name__ == '__main__':
    exception_handling()
