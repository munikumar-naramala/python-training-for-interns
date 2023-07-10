def print_statement():
    print("Hello f1")
    print("_________")


def print_separator():
    str1 = 'Max Verstappen'
    str2 = 'Red Bull'
    print('print sep use: ', str1, str2, sep=":")
    print('There are', '10', 'f1 teams', sep=' ')
    print("_________")


def print_end():
    str3 = 'Kimi'
    print('print end use: ', str3, end=".")
    print()
    print("_________")


if __name__ == '__main__':
    print_statement()
    print_separator()
    print_end()
