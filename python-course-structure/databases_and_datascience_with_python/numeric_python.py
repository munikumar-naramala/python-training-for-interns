import numpy as np

supercars = [
    {"name": "Ferrari 488 GTB", "price": 250000, "horsepower": 660, "top_speed": 205},
    {"name": "Lamborghini Huracan", "price": 280000, "horsepower": 610, "top_speed": 202},
    {"name": "Porsche 911 Turbo S", "price": 200000, "horsepower": 640, "top_speed": 205},
    {"name": "Audi R8", "price": 170000, "horsepower": 610, "top_speed": 205},
    {"name": "McLaren 720S", "price": 280000, "horsepower": 710, "top_speed": 212},
]


def average_price(cars):
    prices = np.array([car['price'] for car in cars])
    avg_price = np.mean(prices)
    return avg_price


def total_horsepower(cars):
    horsepower = np.array([car['horsepower'] for car in cars])
    total_power = np.sum(horsepower)
    return total_power


def highest_top_speed(cars):
    top_speeds = np.array([car['top_speed'] for car in cars])
    max_speed = np.max(top_speeds)
    return max_speed


def price_standard_deviation(cars):
    prices = np.array([car['price'] for car in cars])
    std_dev = np.std(prices)
    return std_dev


if __name__ == '__main__':
    print(average_price(supercars))
    print(total_horsepower(supercars))
    print(highest_top_speed(supercars))
    print(price_standard_deviation(supercars))
