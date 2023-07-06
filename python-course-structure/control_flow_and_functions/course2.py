# if elif else
"""Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird"""

num = int(input("Enter a number: "))
if num % 2 != 0:
    print("Weird")
elif num % 2 == 0 and 2 <= num <= 5:
    print("Not Weird")
elif num % 2 == 0 and 6 <= num <= 20:
    print("Weird")
elif num % 2 == 0 and num > 20:
    print("Not Weird")
else:
    print("Not in range")

# nested if

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

# for loop through a string
str1 = "Ferrari"
for char in str1:
    print(char, end=" ")

print("---------")

# for loop through a range
for i in range(10):
    print("Super Maxx")

# iterate through data
f1_teams = ["Red bull", "McLaren", 'Ferrari', 'Aston Martin']
for team in f1_teams:
    print(team)

# for with else statement
count = 0
for team in f1_teams:
    count += 1
    print(count)
else:
    print("No teams left")

# for loop for a dictionary:

f1 = {"Red Bull": "Max Verstappen", "Aston Martin": "Fernando Alonso", "Ferrari": "Charles Leclerc",
      "Mercedes": "Lewis Hamilton"}
for key, value in f1.items():
    print(key, " : ", value)

# parallel iteration using zip

f1_driver1 = ["Max", "Ham", "Alonso"]
f1_driver2 = ["Checo", 'George', 'Stroll']
for driver1, driver2 in zip(f1_driver1, f1_driver2):
    print(driver1, driver2)

# nested for loop

terms = ['crazy', 'stupid']
names = ['max', 'kimi', 'lando']
for term in terms:
    for name in names:
        print(term, name)

print("---------")

# break
carz = ["red bull", "williams", "merc", "alpha romeo"]

for car in carz:
    if car == 'merc':
        break
    print(car)
print("--------")
# continue
for car in carz:
    if car == 'merc':
        continue
    print(car)

# for loop to count elements in a list

count = 0
for car in carz:
    count += 1
print(count)

# for loop for patterns

for i in range(1, 5):
    for j in range(i):
        print("*", end=' ')
    print()
