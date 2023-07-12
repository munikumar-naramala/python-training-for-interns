import pandas as pd

print(pd.__version__)


def pd_basics(filename):
    try:
        cars = pd.read_csv(filename)
        print(cars.head())
        print("____________")
        print('the shape of the file is')
        print(cars.shape)
        print("____________")
        print(cars.describe())
        print("____________")
        print(cars.info)
        print("____________")
        print(cars.values)
        print("____________")
        print(cars.columns)
        print("____________")
        print(cars.index)
        print("____________")
    except BaseException as error:
        print("there is an exception: {}".format(error))


if __name__ == '__main__':
    pd_basics('supercars.csv')
