def insertion_sort1(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key
    print(arr)


if __name__ == '__main__':
    insertion_sort1([23, 54, 1, 276, 435])
