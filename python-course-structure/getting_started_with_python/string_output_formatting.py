def string_format():
    print("{} is a great driver".format('Max Verstappen'))
    print("----------")


def string_format2():
    print("{} and {}".format('Vettel', 'Kimi'))
    print("{1} and {0}".format('Vettel', 'Kimi'))
    print("----------")


def keyword_formatting():
    print("{} and {} are my fav along with {best}".format('kimi', 'vettel', best='max'))
    print("----------")


if __name__ == '__main__':
    string_format()
    string_format2()
    keyword_formatting()
