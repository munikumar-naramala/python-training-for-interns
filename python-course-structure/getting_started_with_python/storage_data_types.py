def list_datatype():
    x = ['Max', 'Vettel', 'Charles', 'Kimi', 32]
    print(x)
    print(type(x))
    print("----------")


def tuple_datatype():
    x = ('Max', 'Vettel', 'Charles', 'Kimi', 32)
    print(x)
    print(type(x))
    print("----------")


def dict_datatype():
    x = {"himalayan": "adv", "gt": "cafe racer", "trident": "adv"}
    print(x)
    print(type(x))
    print("----------")


def set_datatype():
    x = ['Max', 'Vettel', 'max', 'Charles', 'Kimi', 32]
    print(set(x))
    print(type(x))
    print("----------")


def range_type():
    x = range(10)
    print(x)
    print(type(x))
    print("----------")


if __name__ == '__main__':
    list_datatype()
    tuple_datatype()
    dict_datatype()
    set_datatype()
    range_type()
