import pandas as pd


def group_by(filename):
    cars = pd.read_csv(filename)
    new_cars = cars.groupby('Brand').agg({'Model': 'count'})
    print(new_cars)


if __name__ == '__main__':
    group_by('supercars.csv')

