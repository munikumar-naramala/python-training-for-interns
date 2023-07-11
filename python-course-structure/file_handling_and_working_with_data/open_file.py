def open_file(filename):
    file1 = open(filename)
    for i in file1:
        print(i)


def read_file(filename):
    file1 = open(filename)
    try:
        test_content = file1.read()
        print(test_content)
    except BaseException as error:
        print('There is a problem of:  {}'.format(error))


def close_file(filename):
    file1 = open(filename)
    try:
        test_content = file1.read()
        print(test_content)
    except BaseException as error:
        print('There is a problem of:  {}'.format(error))
    finally:
        file1.close()
        print('file is closed now')


if __name__ == '__main__':
    open_file('test.txt')
    read_file('test.txt')
    close_file('test.txt')
