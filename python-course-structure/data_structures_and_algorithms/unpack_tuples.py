def unpack(tuple1):
    (a1, a2, *a3) = tuple1
    print(a1)
    print(a2)
    print(a3)


if __name__ == '__main__':
    unpack(('himalayan', 'tiger', 'gt', 'speed twin', 'speed', 'scrambler'))
