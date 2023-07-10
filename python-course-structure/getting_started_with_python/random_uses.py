import random


def random_uses():
    num = random.randint(2, 10)
    print(num)
    print("________")


def random_randrange():
    num1 = random.randrange(2, 20, 3)
    print(num1)
    print("________")


def random_choice():
    lst1 = [24, 345, 234, 423]
    print(random.choice(lst1))


if __name__ == '__main__':
    random_uses()
    random_randrange()
    random_choice()
