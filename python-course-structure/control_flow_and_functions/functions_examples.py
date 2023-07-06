def functions_examples():
    def func_with_args(a, b):
        return a + b

    print(func_with_args(5, 2))
    print("---------")

    def squared_number(n):
        return n * n

    print(squared_number(10))
    print("---------")

    def fun_default_args(a=3, b=3):
        return a + b

    print(fun_default_args())
    print(fun_default_args(4, 4))
    print(fun_default_args(4))
    print("---------")

    def keyword_args(first_name, last_name):
        return first_name, last_name

    print(keyword_args(last_name='Verstappen', first_name='Max'))
    print("---------")


if __name__ == '__main__':
    functions_examples()
