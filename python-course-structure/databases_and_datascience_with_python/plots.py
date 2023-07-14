import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cars = [
    {"name": "Ferrari 488 GTB", "price": 250000, "horsepower": 660, "top_speed": 205},
    {"name": "Lamborghini Huracan", "price": 280000, "horsepower": 610, "top_speed": 202},
    {"name": "Porsche 911 Turbo S", "price": 200000, "horsepower": 640, "top_speed": 205},
    {"name": "Audi R8", "price": 170000, "horsepower": 610, "top_speed": 205},
    {"name": "McLaren 720S", "price": 280000, "horsepower": 710, "top_speed": 212},
]

supercars_df = pd.DataFrame(cars)


def plot_average_price(car):
    avg_price = car['price'].mean()

    plt.bar('Average Price', avg_price)

    plt.title('Average Price of Supercars')
    plt.xlabel('Price')
    plt.ylabel('Count')

    plt.show()


def scatter_horsepower_top_speed(car):
    sns.scatterplot(data=car, x='horsepower', y='top_speed')

    plt.title('Horsepower vs Top Speed of Supercars')
    plt.xlabel('Horsepower')
    plt.ylabel('Top Speed')

    plt.show()


if __name__ == '__main__':
    plot_average_price(supercars_df)
    scatter_horsepower_top_speed(supercars_df)
