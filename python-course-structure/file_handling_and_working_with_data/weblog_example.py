import pandas as pd


def weblogs_pandas():
    try:
        logs = pd.read_csv('weblog.csv')
        print(logs.head())
        print("----------")
        print(logs.shape)
        print("----------")
        print(logs.columns.to_list())
        print("----------")
        print(logs.describe())
        print("----------")
        print(logs.info)
        print("----------")
        print(logs.iloc[2:4])
        print("----------")
        logs.rename(columns={'Staus': 'Status'}, inplace=True)
        print(logs.columns.to_list())
        print("------------")
        print(logs['Status'].map(lambda x: 'Success' if x == 200 else x))
    except BaseException as error:
        print('this is an exception: {}'.format(error))


if __name__ == '__main__':
    weblogs_pandas()
