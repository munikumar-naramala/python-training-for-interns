def user_defined_exception():
    min_age = 18

    # noinspection PyBroadException
    try:
        age = int(input("Enter your age: "))
        if age < min_age:
            raise Exception
        else:
            print("Eligible to Vote")

    except Exception:
        print("Exception occurred: Invalid Age")


if __name__ == '__main__':
    user_defined_exception()
