def find_index(element, list1):
    for i in range(len(list1)):
        if list1[i] == element:
            print(i)


if __name__ == '__main__':
    find_index('aston martin valkyrie', ['ferrari 812 super fast', 'aston martin valkyrie', 'BMW m5'])
