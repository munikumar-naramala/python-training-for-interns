def dict_loop():
    f1 = {"Red Bull": "Max Verstappen", "Aston Martin": "Fernando Alonso", "Ferrari": "Charles Leclerc",
          "Mercedes": "Lewis Hamilton"}
    for key, value in f1.items():
        print(key, " : ", value)


if __name__ == '__main__':
    dict_loop()