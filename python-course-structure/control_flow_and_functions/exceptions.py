def try_except():
    try:
        numerator = 10
        denominator = 0

        result = numerator / denominator

        print(result)
    except ZeroDivisionError:
        print("Error: Denominator cannot be 0.")


print("------------")


def more_than_one_expect():
    try:
        drivers = ['max', 'kimi', 'alonso']
        print(drivers[4])
    except ZeroDivisionError:
        print("Denominator cannot be zero")
    except IndexError:
        print("List index out of bound")


print("_--------------")


def try_finally():
    try:
        numerator = 10
        denominator = 0

        result = numerator / denominator

        print(result)
    except ZeroDivisionError:
        print("Error: Denominator cannot be 0.")

    finally:
        print("This is finally block.")


if __name__ == '__main__':
    try_except()
    more_than_one_expect()
    try_finally()
