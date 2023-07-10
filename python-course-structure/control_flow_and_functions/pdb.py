def pdb():
    num2 = 0
    num1 = 1000
    result = num1 / num2
    print(result)


def pdb_from_middle():
    s = '0'
    n = int(s)
    breakpoint()

    print(1000 / n)


if __name__ == '__main__':
    pdb()
    pdb_from_middle()

# run in terminal python -m pdb pdb.py
