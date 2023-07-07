def continue_statement():
    carz = ["red bull", "williams", "merc", "alpha romeo"]

    for car in carz:
        if car == 'merc':
            continue
        print(car)


if __name__ == '__main__':
    continue_statement()
