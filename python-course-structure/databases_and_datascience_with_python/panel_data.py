import pandas as pd

cars = [
    {"name": "Ferrari 488 GTB", "price": 250000, "horsepower": 660, "top_speed": 205},
    {"name": "Lamborghini Huracan", "price": 280000, "horsepower": 610, "top_speed": 202},
    {"name": "Porsche 911 Turbo S", "price": 200000, "horsepower": 640, "top_speed": 205},
    {"name": "Audi R8", "price": 170000, "horsepower": 610, "top_speed": 205},
    {"name": "McLaren 720S", "price": 280000, "horsepower": 710, "top_speed": 212},
]

cars_df = pd.DataFrame(cars)


def average_price(supercars_df):
    avg_price = supercars_df['price'].mean()
    return avg_price


def total_horsepower(supercars_df):
    total_power = supercars_df['horsepower'].sum()
    return total_power


def highest_top_speed(supercars_df):
    max_speed = supercars_df['top_speed'].max()
    return max_speed


def price_standard_deviation(supercars_df):
    std_dev = supercars_df['price'].std()
    return std_dev


def avg_price_per_horsepower(supercars_df):
    supercars_df['price_per_hp'] = supercars_df['price'] / supercars_df['horsepower']
    avg_price_per_hp = supercars_df['price_per_hp'].mean()
    return avg_price_per_hp


if __name__ == '__main__':
    average_price(cars_df)
    total_horsepower(cars_df)
    highest_top_speed(cars_df)
    price_standard_deviation(cars_df)
    avg_price_per_horsepower(cars_df)
