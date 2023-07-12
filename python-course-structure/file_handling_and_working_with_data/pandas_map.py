import pandas as pd


# data['Survived'].map(lambda x: 'Survived' if x==1 else 'Not-Survived')

def map_func(filename):
    try:
        organizations = pd.read_csv(filename)
        print(organizations.head())

        print(organizations['Founded'].map(lambda x: 90 if x <= 2000 else -1))
    except BaseException as error:
        print('this is an exception: {}'.format(error))


if __name__ == '__main__':
    map_func('Organizations-100.csv')
