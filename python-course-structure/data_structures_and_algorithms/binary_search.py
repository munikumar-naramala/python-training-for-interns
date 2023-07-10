def find_index1(list1, start, end, element):
    if end < start:
        return -1

    mid = (start + end) // 2
    if list1[mid] < element:
        return find_index1(list1, mid + 1, end, element)
    elif list1[mid] > element:
        return find_index1(list1, start, mid, element)
    else:
        return mid


if __name__ == '__main__':
    print(find_index1([1, 2, 3, 4, 5, 6, 7], 0, 6, 5))
