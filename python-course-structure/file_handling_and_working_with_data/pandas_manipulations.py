import pandas as pd


def csv_mods(filename):
    try:
        cars_df = pd.read_csv(filename)
        print(cars_df.head())
        print(cars_df.columns)
    except BaseException as error:
        print('error is : {}'.format(error))
    print("----------")


def apply_func(filename):
    try:
        cars_df = pd.read_csv(filename)
        cars_df['new_col'] = cars_df['    Toppp-speeed'] / 10
        cars_df.new_col = cars_df.new_col.apply(lambda x: x + 3)
        print(cars_df.head())
    except BaseException as error:
        print('the exception is: {}'.format(error))


def rename_columns(filename):
    try:
        cars_df = pd.read_csv(filename)
        cars_df_renamed = cars_df.rename(
            columns={'     Car Name': 'Name', 'Displacement ': "Displacement", 'Enginee': 'Engine',
                     '          hp': 'HorsePower',
                     '   Transmission': 'Transmission', '    Toppp-speeed': 'TopSpeed', '           Cost': 'Cost'})
        print(cars_df_renamed.head())
        print(cars_df_renamed.columns)
    except BaseException as error:
        print('the exception is: {}'.format(error))


if __name__ == '__main__':
    csv_mods('Hyper Cars 2019.csv')
    apply_func('Hyper Cars 2019.csv')
    rename_columns('Hyper Cars 2019.csv')
