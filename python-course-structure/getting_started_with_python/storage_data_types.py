def storage_types():
    def list_datatype():
        x = ['Max', 'Vettel', 'Charles', 'Kimi', 32]
        print(x)
        print(type(x))
        print("----------")

    list_datatype()

    def tuple_datatype():
        x = ('Max', 'Vettel', 'Charles', 'Kimi', 32)
        print(x)
        print(type(x))
        print("----------")

    tuple_datatype()

    def dict_datatype():
        x = {"himalayan": "adv", "gt": "cafe racer", "trident": "adv"}
        print(x)
        print(type(x))
        print("----------")

    dict_datatype()

    def set_datatype():
        x = ['Max', 'Vettel', 'max', 'Charles', 'Kimi', 32]
        print(set(x))
        print(type(x))
        print("----------")
    set_datatype()

    def range_type():
        x = range(10)
        print(x)
        print(type(x))
        print("----------")
    range_type()


if __name__ == '__main__':
    storage_types()
