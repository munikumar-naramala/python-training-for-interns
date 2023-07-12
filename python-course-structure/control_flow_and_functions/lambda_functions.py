def lambda_functions():
    x = lambda: print("Hello World")
    x()

    c = lambda name: print("Hello", name)
    c("Max")


def multiply(n):
    return lambda a: a * n


if __name__ == '__main__':
    lambda_functions()
    doubler = multiply(2)
    three_times = multiply(3)
    print(doubler(10))
