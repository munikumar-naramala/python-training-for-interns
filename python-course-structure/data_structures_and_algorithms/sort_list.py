def ascending():
    list1 = [123, 312, 43, 56, 456, 45]
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] > list1[j]:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
    print(list1)
    print("----------")


def descending():
    list1 = [123, 312, 43, 56, 456, 45]
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] < list1[j]:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
    print(list1)
    print("----------")


if __name__ == '__main__':
    ascending()
    descending()
