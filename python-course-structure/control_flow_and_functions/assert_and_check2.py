def assert_check():
    def example_1(num):
        assert type(num) == int, 'num must be an integer'
        n = int(num)
        return 100 / n

    # print(example_1('Ham'))

    print(example_1(100))


# python -O(capital o) assert_and_check2.py will close all the assert statements
# one advantage over print and check
if __name__ == '__main__':
    assert_check()
