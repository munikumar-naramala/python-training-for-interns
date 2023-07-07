def identity_operators():
    x = 5
    y = 6
    if x is y-1:
        print(x, y-1)
    if x is not y:
        print(x, y)


if __name__ == '__main__':
    identity_operators()
