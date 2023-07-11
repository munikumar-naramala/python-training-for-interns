import pandas as pd

cars = pd.read_csv('supercars.csv')


def sorting_ascending(column):
    sorted_by_horses = cars.sort_values(column)
    print(sorted_by_horses)
    print("-----------")


def sorting_descending(column):
    sorted_by_horses = cars.sort_values(column, ascending=False)
    print(sorted_by_horses)
    print("-----------")


def sorting_multiple_fields(col1, col2):
    sorted_values = cars.sort_values([col1, col2])
    print(sorted_values)
    print("-----------")


def sorting_multiple_fields_2(col1, col2):
    try:
        sorted_values = cars.sort_values([col1, col2], ascending=[False, True])
        print(sorted_values)
        print("-----------")
    except BaseException as error:
        print('there is an exception: {}'.format(error))


if __name__ == '__main__':
    sorting_ascending('HorsePower')
    sorting_descending('HorsePower')
    sorting_multiple_fields('HorsePower', 'TopSpeed')
    sorting_multiple_fields_2('HorsePower', 'TopSpeed')
