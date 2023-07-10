list1 = ['Max', 'Ham', 'Danny']


def copy_lists():
    list2 = []
    for driver in list1:
        list2.append(driver)
    print(list1)
    print(list2)
    print("----------")


def list_length():
    print(len(list1))
    print("---------")


if __name__ == '__main__':
    copy_lists()
    list_length()
