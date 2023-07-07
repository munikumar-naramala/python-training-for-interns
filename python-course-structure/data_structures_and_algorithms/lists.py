def lists():
    def copy_lists():
        list1 = ['Max', 'Ham', 'Danny']
        list2 = []
        for driver in list1:
            list2.append(driver)
        print(list1)
        print(list2)
        print("----------")

    copy_lists()

    def list_indexing():
        list1 = ['Max', 'Ham', 'Danny']
        first_element = list1[0]
        last_element = list1[-1]
        print(first_element, last_element)
        print('---------')
    list_indexing()

    def get_index():
        order = ['Max', 'Ham', 'Danny']
        print(order.index('Max'))
        print("---------")
    get_index()


if __name__ == '__main__':
    lists()
