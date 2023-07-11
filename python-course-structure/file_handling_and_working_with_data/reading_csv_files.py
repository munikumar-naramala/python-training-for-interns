import csv


def csv_read(filename):
    rows = []
    csv_file = open(filename, 'r')
    csv_reader = csv.reader(csv_file)
    fields = next(csv_reader)
    for row in csv_reader:
        rows.append(row)

    print("Total no. of rows: %d" % csv_reader.line_num)

    print('Field names are:' + ', '.join(field for field in fields))

    try:
        print('\nFirst 5 rows are:\n')
        for row in rows[:5]:
            for col in row:
                print(col, end=" ")
            print('\n')
    except BaseException as e:
        print("An exception occurred: {}".format(e))


if __name__ == '__main__':
    csv_read("organizations-100.csv")
