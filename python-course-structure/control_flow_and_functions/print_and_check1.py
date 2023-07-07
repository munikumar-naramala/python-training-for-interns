def python_debugging_techniques():
    def print_and_check(s):
        count = 0
        for i in range(len(s)):
            count += 1
        print(count)

    # print_and_check(5) typeerror
    print_and_check('Sanjana')


if __name__ == '__main__':
    python_debugging_techniques()
