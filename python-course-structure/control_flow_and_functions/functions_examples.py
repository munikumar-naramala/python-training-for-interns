def func_with_args(a, b):
    return a + b


def squared_number(n):
    return n * n


def fun_default_args(a=3, b=3):
    return a + b


def keyword_args(first_name, last_name):
    return first_name, last_name


if __name__ == '__main__':
    print(func_with_args(5, 2))
    print("---------")
    print(squared_number(10))
    print("---------")
    print(fun_default_args())
    print(fun_default_args(4, 4))
    print(fun_default_args(4))
    print("---------")
    print(keyword_args(last_name='Verstappen', first_name='Max'))
    print("---------")
