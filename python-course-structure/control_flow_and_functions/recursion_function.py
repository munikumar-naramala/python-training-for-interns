def recursion_examples():
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    print(factorial(3))


if __name__ == '__main__':
    recursion_examples()
