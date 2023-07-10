def from_start(idx):
    str1 = 'pagani zonda is the best car ever'
    print(str1[:idx])


def to_end(idx):
    str1 = 'pagani zonda is the best car ever'
    print(str1[idx:])


def negative_slicing(idx1, idx2):
    str1 = 'pagani zonda is the best car ever'
    print(str1[idx1:idx2])


if __name__ == '__main__':
    from_start(9)
    to_end(9)
    negative_slicing(3, 14)
