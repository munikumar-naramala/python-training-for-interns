import json


def write_json(filename, data):
    try:

        jsonFile = open(filename, 'w')
        json.dump(data, jsonFile)
    except BaseException as e:
        print("An exception occurred: {}".format(e))


def read_json(filename):
    file = open(filename, 'r')
    data = json.load(file)
    print(data)


if __name__ == '__main__':
    write_json("cars.json", {
        "Cars": {
            "Valkyrie": 1000,
            "Zonda R": 800,
            "911 Carreras": 450,
            "Corvette Z06": 650,
            "Mustang Shelby GT500": 760
        }
    })

    read_json("cars.json")
