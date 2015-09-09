#Operators ** * / // + -
4 + 3

4 * 3

(2 + 4) * 3

10 / 3

10 // 3

3 ** 4

#7/0

# Strings are identifed either by single ' ' or double " " quotes
"my class"

'my class'

# parentheses take precedence
# variables are used to store math results, strings or other data
amount = (2 + 4) * 3
print(amount)


# strings can be concatenated
first_name = "John"
last_name = "Smith"
print(first_name + " " + last_name)


# display your results
radius = 7
circumference = 22
pi = circumference / radius
print("pi ", pi)
area = pi * radius ** 2
print("area ", area)

# you can use the multiply operator to create a long string from a small one
count = 4
name = "four "
all_names = count * name
print(all_names)

# you can pull single characters from a string
# strings indexes start at zero  J-0   A-1   C-2   K-3
name = "JACK"
print(name[0])
print(name[2])

# lists are ordered collections of things
color_list = ['red', 'green', 'blue']
print(color_list)

# you can use indexes to use items in a list
# like with string characters, list indexes start at zero
print(color_list[0])

# booleans tell us if something is True or False
# boolean operators   ==  != < > <= >=
some_number = 3
print(some_number == 3)
print(some_number <= 3)

# use     or    or   and    to combine booleans
# if you use and both  expressions must be True to get True
print(some_number > 1 and some_number < 4)
# you could do the same thing with this
print(1 < some_number < 4)

# control statements
# use the if statement and a boolean to decide what code to run
# code to be executed by an if is indented
if True:
    some_number = 2
    print('this code ran', 2)

if False:
    another_number = 4
    print('did this code run?', 4)

age = 9
if age < 10:
    print('too young')

if age >= 10:
    print('old enough')

# there's the else, if one else the other
if True:
    print('something is True')
else:
    print('something is False')

# and also the elif, use if you have more comparisons
count = 10
if count < 8:
    print('too few')
elif count >= 8 or count < 10:
    print('just right')
elif count >= 10:
    print('too many')

# this has the same effect
count = 10
if count < 8:
    print('too few')
elif 8 <= count < 10:
    print('just right')
elif count >= 10:
    print('too many')


# loops let you execute blocks of code multiple times
# the while loop runs until the boolean expression is False

# this will execute forever or until something breaks the loop
# while True:
#     print('ooooooo ')

counter = 2
while counter < 100:
    print('counter ', counter)
    counter = 2 * counter ** 2

for i in range(10):
    print(i)