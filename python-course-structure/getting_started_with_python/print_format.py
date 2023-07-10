def print_formats():
    car = 'volkswagen'
    print(f'I drive {car}')
    print("_________")


def print_repr():
    # repr represents the string as it is without any formatting
    str4 = 'Sanjana\n'
    print(repr(str4))
    print(repr(22 / 10))
    print("_________")


def print_other_formatting():
    # '!s' applies str(), and '!r' applies repr()
    str5 = 'Max Verstappen'
    int1 = 7
    print(f'Lewis Hamilton is a {int1!s} time world champion')
    print(f'{str5!r}')
    print("_________")


def print_specifier():
    car = 'Red Bull'
    driver = 'Max Verstappen'
    print(f'The f1 {car=} is driven by {driver=}')
    print("_________")


if __name__ == '__main__':
    print_formats()
    print_repr()
    print_other_formatting()
    print_specifier()
