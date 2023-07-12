import pandas as pd

cars = pd.read_csv('supercars.csv')


def iter_rows():
    for index, row in cars.iterrows():
        print(row)
        if index == 1:
            break


def rows_cols():
    print(cars[['Brand', 'HorsePower']].head())


def rows_cols2():
    print(cars.loc[:, ['Brand', 'HorsePower']].head())
    print("_________")
    print(cars.iloc[0:3, :])


def cleaning():
    print(cars.isnull().sum())


if __name__ == '__main__':
    iter_rows()
    rows_cols()
    rows_cols2()
    cleaning()
