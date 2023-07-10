def string(str1):
    for character in str1:
        print(character, end='')


def check_string(word):
    str2 = 'Max Verstappen rain mode on'
    if word in str2:
        print(f'{word} in str2')


if __name__ == '__main__':
    string('Verstappen')
    check_string('rain')