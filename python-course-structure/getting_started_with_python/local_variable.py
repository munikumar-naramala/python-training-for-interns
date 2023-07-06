x = "sad"


def local_variable():
    x = "happy"
    print("print statements inside the function will execute later")
    print("Sanjana is " + x)


print("print statements outside the function will execute first")

print("Sanjana is " + x)
if __name__ == '__main__':
    local_variable()
