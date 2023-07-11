def with_open(filename):
    try:
        with open(filename, 'r') as file1:
            test_content = file1.read()
            print(test_content)
    except BaseException as error:
        print('the exception is : {}'.format(error))


def with_open_write(filename, write, writelines):
    try:
        with open(filename, 'w') as file2:
            file2.write(write)
            file2.writelines(writelines)
    except BaseException as error:
        print('the exception is : {}'.format(error))
    finally:
        file2.close()


if __name__ == '__main__':
    with_open('test.txt')
    with_open_write('test.txt', "This is a bajaj - triumph collaboration", '''This is a dilemma between the options
            the availability of triumph and harley davidson 400 cc and royal enfield options for 350cc''')
    with_open('test.txt')
