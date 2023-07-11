import csv
import json


def csv_to_json(csv_file_path, json_file_path):
    jsonArray = []

    with open(csv_file_path, encoding='utf-8') as csv_file:
        csvReader = csv.DictReader(csv_file)

        for row in csvReader:
            jsonArray.append(row)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        try:
            jsonString = json.dumps(jsonArray, indent=4)
            json_file.write(jsonString)
        except BaseException as error:
            print("there is an exception: {}".format(error))


if __name__ == '__main__':
    csv_to_json('supercars.csv', 'supercars.json')
