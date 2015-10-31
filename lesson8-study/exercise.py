# 1. what is the output of the following code
#    place your answer in a comment

x = 3
y = 9

if x >= 0 and y < 9:
    print('yes')
else:
    print('no')


# 2. what is the output of the following code
#    place your answer in a comment

x = -3
y = 8

if x > 0 or y < 9:
    print('yes')
else:
    print('no')


# 3. convert the following equation to Python,
#    replace None with your answer
#            2
#       (2+x)
#  y = -------
#         9

x = 4
y = None
print(y)


# 4. write code that converts Fahrenheit to Celsius
#    1. ask the user to enter a temperature in Fahrenheit, store in variable f
#    2. convert the variable f to an integer
#    3. subtract 32 from f and divide the result by 1.8, store in variable c
#    4. print out the temperature in variable c

f = input('temp in f? ')
f = float(f)
c = (f - 32) / 1.8
print(c)


# 5. write code that loops from 0 to 19 using range()
#    for each iteration raise the current loop value to the power of 3
#    print the result of each iteration




# 6. correct rocket.py so that it only prints to the
#    screen when height is greater than 0.0 and
#    time <= 100.0



# 7. write a function called add_ten
#    the function should take a parameter called
#    number and return the number with 10 added to it
#    call the function passing in a number, print the output



# 8. create a list called my_friends, replace None
#    add your friends names to it
#    then loop through the list to print each name

my_friends = ['bob','jack','karen']

for name in my_friends:
    print(name)


# 9. add the following cities and populations to the dictionary
#    then check to see if 'Dallas' is in the dictionary
#    if Dallas is print the population
#    if Dallas is not in the dictionary print 'not found'
#    New York    8,491,079
#    Los Angeles 3,928,864
#    Chicago	 2,722,389
#    Houston	 2,239,558

city_dict = {}

if None:
    print(city_dict['Dallas'])
else:
    print('not found')


# 10. import the add_message from the echo module
#    call the add_message function pass your name and a message
#    as parameters and print the result

