def find_index(element, list):
    for i in range(len(list)):
        if list[i] == element:
            print(i)


if __name__ == '__main__':
    find_index('aston martin valkyrie', ['ferrari 812 super fast', 'aston martin valkyrie', 'BMW m5'])
    