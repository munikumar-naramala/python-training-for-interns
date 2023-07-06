"""run:
python helloworld.py
helloworld.py"""
print("Hello World!")

# indentation:
if 5 > 2:
    print("Five is greater than two")

# variables:
x = 5
y = "Sanjana"  # type string
y = 21  # type int

# This is a comment

# type casting:
x = str(3)
y = int(3.2)
z = float(3)

# find datatype:
print(type(x))

x = "Sanjana"  # is same as
x = 'Sanjana'

# Case sensitive variables:
x = "Sanjana"
X = 'Vonteri'
# these two are completely different variables

# legal variable names:
my_var = 1
_myvar = 1
_my_var = 1
MY_VAR = 1

# camelcase:
myCamelCase = "Sanjana"

# pascal case
MyPascalCase = "Sanjana"

# snake_case
my_snake_case = "Sanjana"

# multiple variables assignment

x, y, z = "Sanjana", "Bhavana", "Meghana"

# multiple variables same assignment

x = y = z = "Sanjana"

# unpacking
cars = ["volkswagen", "mahindra", "skoda"]
x, y, z = cars

# print
x = "Sanjana"
y = "pronouns are"
z = "she/her"

print(x, y, z)  # or
print(x + " " + y + " " + z)

# mathematical operation in print statement
x = 4
y = 6
print(x + y)

# global variables
# variable outside, usage inside a function
x = "serious"


def global_variable_example():
    print("Sanjana is " + x)


global_variable_example()

# local variable
x = "sad"


def local_variable_example():
    x = "happy"
    print("Sanjana is " + x)


local_variable_example()  # this will print happy

print("Sanjana is " + x)  # this will print sad


# global keyword
# - create a global variable inside a function

def global_keyword():
    global g
    g = "sad and happy"
    print("Sanjana is " + g)


global_keyword()

# - to change the value of the gobal variable inside a function, use the global keyword
x = "Happy"


def sad_example():
    global x
    x = "Sad"
    print("Sanjana is " + x)


sad_example()

# Data Types:
a = "Sanjana"  # string
b = 21  # int
c = 21.24  # float
d = 21 + 1j  # complex
cars = ["polo", "thar", "octavia"]  # list
bikes = ("himalayan 411", 'gt continental 650', 'scram 411')  # tuple
e = range(10)  # range
bike_examples = {"himalayan": "adv", "gt": "cafe racer", "trident": "adv"}  # dict
unique_items = {"triumph", "benelli", "harley"}
f = True  # bool
x = b"Hello"  # bytes
v = None
# frozenset
vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
# fSet.add('v')#error because frozenset is immutable
'''for dictionary, 
the frozenset only takes the keys and
returns the output'''

# random number
import random

print(random.randrange(1, 19, 2))

# strings are arrays. There is no char in python
# char is simply a string of length 1
# we can slice strings
a = "Sanjana"
print(a[1])

# loop a string
for i in "Sanjana":
    print(i)

# string length
print(len(a))

# check string
a = "inspire innovation drive change"
print("drive" in a)

print("drive" not in a)

# slicing strings
h = "Volkswagen is best"
print(h[2:6])
print(h[-1: -6])

#
h.upper()
h.lower()
h.strip()  # removes whitespace

# replace
print(h.replace('w', 'W'))

# split
r = "Hello, World!"
print(r.split(","))

# concatenation
a = "polo"
b = "is the "
c = "best"
print(a + " " + b + c)

# string formatting
age = 21
txt = "I am Sanjana, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

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

# - arithmetic + - * / // %  **
print(20 / 5)
print(20 // 5)  # interger division
print(20 % 5)

# assignment operators operator=
a = 5
a += 5
print(a)

# comparision operators
print(3 == 3)

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
