def break_statement():
    carz = ["red bull", "williams", "merc", "alpha romeo"]

    for car in carz:
        if car == 'merc':
            break
        print(car)
        

if __name__ == '__main__':
    break_statement()
