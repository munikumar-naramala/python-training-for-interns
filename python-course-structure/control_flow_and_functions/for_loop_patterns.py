def patterns():
    for i in range(1, 5):
        for j in range(i):
            print("*", end=' ')
        print()


if __name__ == '__main__':
    patterns()
