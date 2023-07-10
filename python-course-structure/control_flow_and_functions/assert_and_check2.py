def example_1(num):
    assert type(num) == int, 'num must be an integer'
    n = int(num)
    return 100 / n


# python -O(capital o) assert_and_check2.py will close all the assert statements
# one advantage over print and check
if __name__ == '__main__':
    print(example_1('Ham'))

    print(example_1(100))
