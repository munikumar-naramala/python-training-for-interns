def if_elif_else():
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        print("Odd")
    elif num % 2 == 0 and 2 <= num <= 5:
        print("even 2-5")
    elif num % 2 == 0 and 6 <= num <= 20:
        print("even 6-20")
    elif num % 2 == 0 and num > 20:
        print("Not even >20")
    else:
        print("Not in range")


if __name__ == '__main__':
    if_elif_else()
