def string_format():
    print("{} is a great driver".format('Max Verstappen'))
    print("----------")

    def string_format2():
        print("{} and {}".format('Vettel', 'Kimi'))
        print("{1} and {0}".format('Vettel', 'Kimi'))
        print("----------")

    string_format2()

    def keyword_formatting():
        print("{} and {} are my fav along with {best}".format('kimi', 'vettel', best='max'))
        print("----------")

    keyword_formatting()


if __name__ == '__main__':
    string_format()
