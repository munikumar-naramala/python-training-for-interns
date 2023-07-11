import json
import csv


def json_to_csv(json_filename, csv_filename):
    with open(json_filename) as json_file:
        json_data = json.load(json_file)
        data_file = open(csv_filename, 'w', newline='')
    csv_writer = csv.writer(data_file)
    count = 0
    for data in json_data:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
    data_file.close()


if __name__ == '__main__':
    json_to_csv('supercars.json', 'supercars_from_json.csv')
