x = "serious"


def global_variable():
    print("Sanjana is " + x)

    def global_keyword():
        global x
        x = "happy"
        print("Sanjana is " + x)

    global_keyword()


if __name__ == '__main__':
    global_variable()
