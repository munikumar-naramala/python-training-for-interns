import pandas as pd


def slicing_iloc(filename):
    cars = pd.read_csv(filename)
    print(cars.columns)
    print(cars.iloc[2:4])


def slicing_loc(filename):
    cars = pd.read_csv(filename)
    print("--------")
    print(cars.loc[2:4, 'Brand'])


if __name__ == '__main__':
    slicing_iloc('supercars.csv')
    slicing_loc('supercars.csv')
