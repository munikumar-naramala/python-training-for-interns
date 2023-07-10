def pop_element(index):
    list1 = ['sanjana', 'volkswagen', 'triumph', 'white']
    list1.pop(index)
    print(list1)


def remove_element(element):
    list2 = ['sanjana', 'volkswagen', 'triumph', 'white']
    list2.remove(element)
    print(list2)


def del_element(index):
    list3 = ['sanjana', 'volkswagen', 'triumph', 'white']
    del list3[index]
    print(list3)


def empty_list_completely():
    list4 = ['sanjana', 'volkswagen', 'triumph', 'white']
    list4.clear()
    print(list4)


if __name__ == '__main__':
    pop_element(0)
    remove_element('white')
    del_element(0)
    empty_list_completely()
