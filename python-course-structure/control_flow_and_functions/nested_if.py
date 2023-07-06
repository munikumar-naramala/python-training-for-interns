def nested_if():
    car = input("What do you drive: ")
    c = car.lower()
    if "volkswagen" in c:
        print("You have made the best choice of your life!")
        if "polo" in c:
            print("No one can stop you.")
        elif "virtus" in c:
            print("great adv sedan choice")
    elif "mahindra" in c:
        print("you are a patriot or a saver")
        if "thar" in c:
            print("go to wayanad")
    else:
        print("I'll get back to you but I'm glad you drive!")


if __name__ == '__main__':
    nested_if()
