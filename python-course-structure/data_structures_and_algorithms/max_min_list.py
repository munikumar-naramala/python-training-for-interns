def max_in_list():
    list1 = [123, 312, 43, 56, 456, 45]
    max_element = list1[0]
    for number in list1:
        if number > max_element:
            max_element = number
    print(max_element)
    print(max(list1))
    print("-----------")


def min_in_list():
    list1 = [123, 312, 43, 56, 456, 45]
    min_element = list1[0]
    for num in list1:
        if num < min_element:
            min_element = num
    print(min_element)
    print(min(list1))
    print("-----------")


if __name__ == '__main__':
    max_in_list()
    min_in_list()
