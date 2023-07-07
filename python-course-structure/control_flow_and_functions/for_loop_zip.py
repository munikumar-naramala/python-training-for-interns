def zip_use():
    f1_driver1 = ["Max", "Ham", "Alonso"]
    f1_driver2 = ["Checo", 'George', 'Stroll']
    for driver1, driver2 in zip(f1_driver1, f1_driver2):
        print(driver1, driver2)


if __name__ == '__main__':
    zip_use()
