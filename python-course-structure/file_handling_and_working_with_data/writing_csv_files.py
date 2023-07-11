import csv


def write_csv(filename, fields, rows):
    try:
        with open(filename, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)

            csv_writer.writerow(fields)

            csv_writer.writerows(rows)
    except BaseException as e:
        print("Exception occurred : {}".format(e))


def read_csv(filename):
    csv_file = open(filename, 'r')
    csv_reader = csv.reader(csv_file)
    fields = next(csv_reader)
    print(fields)


if __name__ == '__main__':
    write_csv("supercars.csv", ['Brand', 'Model', 'HorsePower', 'TopSpeed'], [['Pagans', 'Zonda', 800, 350],
                                                                              ['Porsche', '911 Carreras S', 450, 306],
                                                                              ['Chevrolet', 'Corvette Z06', 650, 315],
                                                                              ['Ford', 'Mustang Shelby GT500', 760,
                                                                               298],
                                                                              ['Aston Martin', 'Vantage AMR', 503, 314],
                                                                              ['Aston Martin', 'Valkyrie', 1000, 350]])

    read_csv("supercars.csv")
