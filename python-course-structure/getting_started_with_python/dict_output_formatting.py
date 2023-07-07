def dict_formatting():
    def print_dict1():
        dict1 = {'red bull': 'max verstappen', 'ferrari': 'charles leclerc', 'mercedes': 'lewis hamilton'}
        for key, value in dict1.items():
            print(f'{key:10} ==> {value:20}')
        print("_________")
        for key in dict1.keys():
            print(f'{key:19} team')
        print("---------")
        for value in dict1.values():
            print(f'{value:20} driver')
        print("---------")
    print_dict1()

    def print_dict2():
        f1 = {'Max': 4127, 'Lewis': 4098, 'Vettel': 8637678}
        print('Max: {0[Max]:d}; Vettel: {0[Vettel]:d}; ''Lewis: {0[Lewis]:d}'.format(f1))
        print("_________")

    print_dict2()



if __name__ == '__main__':
    dict_formatting()
