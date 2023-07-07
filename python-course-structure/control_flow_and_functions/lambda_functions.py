def lambda_functions():
    greet = lambda: print("Hello World")
    greet()

    greet1 = lambda name : print("Hello", name)
    greet1("Max")


if __name__ == '__main__':
    lambda_functions()
