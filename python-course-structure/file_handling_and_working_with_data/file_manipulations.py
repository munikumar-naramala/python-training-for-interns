import os


def read_characters(filename, characters):
    try:
        with open(filename, 'r') as file2:
            content = file2.read(characters)
            print(content)
    except BaseException as error:
        print('There is a problem of:  {}'.format(error))


def read_words(filename):
    try:
        with open(filename, 'r') as file2:
            content = file2.readlines()
            for i in content:
                word = i.split(" ")
                print(word)
            print("-----------")
    except BaseException as error:
        print('There is a problem of:  {}'.format(error))


def append_file(filename, text):
    try:
        with open(filename, 'a') as file3:
            file3.write(text)

    except BaseException as error:
        print('There is a problem of:  {}'.format(error))

    finally:
        file3.close()


def rename_file(filename, rename_file1):
    try:
        os.rename(filename, rename_file1)
    except IOError as error:
        print('An error occurred: {}'.format(error))


def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)


if __name__ == '__main__':
    read_characters('test.txt', 8)
    read_words('test.txt')
    append_file('test.txt', 'this is the appended line')
    read_words('test.txt')
    rename_file('test.txt', 'info.txt')
    delete_file('info.txt')
