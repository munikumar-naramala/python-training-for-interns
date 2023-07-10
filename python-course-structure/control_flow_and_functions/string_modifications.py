def upper_case():
    str1 = 'triumph speed twin'
    print(str1.upper())


def remove_whitespace():
    str1 = '     triumph speed twin     '
    print(str1.strip())


def replace_letter():
    str1 = 'triumph speed twin'
    print(str1.replace('t', 'T'))


def split_string(element):
    str2 = 'aston,martin,valkyrie'
    print(str2.split(element))


if __name__ == '__main__':
    upper_case()
    remove_whitespace()
    replace_letter()
    split_string(',')
