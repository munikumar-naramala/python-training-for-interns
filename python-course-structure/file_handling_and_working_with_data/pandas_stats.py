import pandas as pd

cars = pd.read_csv('supercars.csv')


def pandas_max():
    print(cars.max())


def pandas_argmax():
    print(cars['HorsePower'].argmax())


def value_counts():
    print(cars['Brand'].value_counts())


def argmax_iloc():
    print(cars.iloc[[cars['HorsePower'].argmax()]])
    print(cars.iloc[[cars['HorsePower'].argmax()]]['TopSpeed'])


def argmax_loc():
    print(cars.loc[cars['HorsePower'].argmax(), 'TopSpeed'])


if __name__ == '__main__':
    pandas_max()
    pandas_argmax()
    value_counts()
    argmax_iloc()
    argmax_loc()
