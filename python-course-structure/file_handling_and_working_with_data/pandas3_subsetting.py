import pandas as pd

cars = pd.read_csv('supercars.csv')


def sub_setting_columns(column):
    print(cars[column])
    print("-----------")


def sub_setting_multiple_columns(col1, col2):
    try:
        cols = [col1, col2]
        print(cars[cols])
        print("-----------")
    except BaseException as error:
        print("exception is : {}".format(error))


def sub_setting_rows(row, min_hrs_prs):
    print(cars[row] > min_hrs_prs)
    print("---------------")
    print(cars[cars[row] > min_hrs_prs])
    print("---------------")


def based_on_text(column, value):
    try:
        print(cars[cars[column] == value])
        print("------------")
    except BaseException as error:
        print('the exception is: {}'.format(error))


def example1(col1, val1, col2, val2):
    is_am = cars[col1] == val1
    is_val = cars[col2] == val2
    print(cars[is_am & is_val])


if __name__ == '__main__':
    sub_setting_columns('Brand')
    sub_setting_multiple_columns('Brand', 'Model')
    sub_setting_rows('HorsePower', 550)
    based_on_text('Brand', 'Aston Martin')
    example1('Brand', 'Aston Martin', 'Model', 'Valkyrie')
