
# escape characters:
a = "It\'s alright"
print(a)

b = 'this is a \\backslash\\'
print(b)

c = 'this is a \n new line'
print(c)

d = 'this is a \r carriage return'
print(d)

e = 'thia is a \t tab'
print(e)

a = 'sanjana reddy'
print(a.capitalize())  # Sanjana reddy
a = 'SANJana RedDY'
print(a.casefold())  # sanjana reddy
a = 'sanjana'
print(a.center(100))
print(a.count('a'))
print(a.encode())
print(a.format('.s'))

# boolean
print(10 > 1)

print(bool(['apple', 'cherry']))

# null values are false
print(bool(()))
bool(0)


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))  # false


def bool_function():
    return True


if bool_function():
    print("yeahhhh")
else:
    print("nooooo")

# if an object is int or not
x = 200
print(isinstance(x, str))

# operators


# logical operators and or not
print(5 < 2 and 3 < 1)

# identity operators is is not
x = 4
y = 5
print(x is not y)

# membership operators in not in
x = "wagen"
y = "volkswagen"

print(x in y)
print('----------')
# bitwise operators & | ~

#  << zero filled left shift
# >> signed right shift
x = 10  # binary 1010
y = 4  # binary 0100
print(x & y)

# binary representation of 10 is (....0000 1010)[32 bits]

# operator precedence
# PEMDAS left to right
# string methods

a = "volkswagen"
print(a.zfill(15))
print(a.upper())
# -- translate method
my_table = str.maketrans('w', 'v')  # only for string
print(a.translate(my_table))

x = 'gaw'  # to replace x with y
y = 'Sde'
my_tablee = str.maketrans(x, y)
print(a.translate(my_tablee))

z = 'vol'  # to remove this part from the string
my_tablee2 = str.maketrans(x, y, z)
print(a.translate(my_tablee2))

a = 'mahindra thar'
print(a.title())
print(a.capitalize())

a = "MahIndRa tHaR"
print(a.swapcase())
print('-------------')
a = "   mahindra thar    "
print(a.strip())

a = 'volkswagen polo gt tsi'
if a.startswith('v'):
    print('it is volkswagen')
else:
    print('it is not volkswagen')

a = 'this is a multiline \n statement to check \n if the splitlines method is \n working or not\n let\'s see if this will \n break it in the form \n of a list'
print(a.splitlines())

a = 'volkswagen polo gt tsi'

print(a.split())
