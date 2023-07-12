import pandas as pd

cars = pd.read_csv('supercars.csv')


def add_column(column):
    cars[column] = cars['HorsePower'] / 1000
    print(cars.head(2))
    print("-----------")


def change_name(column, rename):
    try:
        cars.rename(columns={column: rename}, inplace=True)
        print(cars.columns)
        print("-----------")
    except BaseException as error:
        print('this is an exception: {}'.format(error))


def columns_as_list():
    cars.columns.tolist()


if __name__ == '__main__':
    add_column('torque_dummy')
    change_name('torque_dummy', 'TorqueDummy')
    columns_as_list()
