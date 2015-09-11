##Lesson 1 - Basics##

- Numbers
- Operators
- Order of operations
- Variables
- Strings
- Lists
- Booleans
- Print and input

##Types of numbers##
Whole numbers are called integers or are of type int.

    1   2   3  4  5   13456
    
Numbers with a decimal component are called floating point numbers and are of type float.

    1.0 2.123 3.14

##Operators##
Operators are symbols we use to perform arithmetic on numbers in Python. Some operators may also be used to manipulate strings or words or other objects.

Here are a few examples of arithmetic operators. The examples below use ints. If using ints in operations you will usually receive ints as the result, but in Python 3 the / division operator will return a float.

    >>> 4 + 3
    7
    
    >>> 4 * 3
    12

The result of 10 divided by 3 gives you a float or floating point number.

    >>> 10 / 3
    3.3333333333333335

//  floor division operator, the result has no decimal component. It will return an int.

    >>> 10 // 3
    3

**  power operator

    >>> 3**2   
    9
    
Placing a - minus sign in front of a number makes it negative. The minus sign by itself is called a negative unary operator because it only needs one number to perform a calculation. There's also a positive or + plus sign unary operator, but you'll likely never use it. 

    >>> -4
    -4
    
    >>> -(4-5)
    1
    
    >>> +4
    4
    
    >>> +(4-5)
    -1

##Order of operations###
You are probably familiar with order of operations. Python follows order of operations.

For example:

Here 3 * 5 is calculated before 2 is added to it.

    >>> 2 + 3 * 5
    17

2 to the 3rd power is calculated before 5 is multiplied to the result.

    >>> 2**3 * 4
    32
    
    >>> 12.56 / 2**2
    3.14
    
    >>> 2 * 3 - 4 / 2
    4.0

You may use parentheses to group operations, overriding normal order.

    >>> (2 + 4) * 3
    18
    
    >>> (4 * 2)**2
    64
    
    >>> (9  + 3) * (9 + 6)
    180

Order of operations is:

    +-(unary)  ** ()   *   /   //   +  - 

##Variables##
Variables are labels or tags or names that you can assign to a number or to a math operation. They let you store a number or result to use later in your program.

    >>> some_number = 4
    
    >>> some_number
    4
    
    >>> result = some_number * 8
    
    >>> result
    32
    
    >>> radius = 5
    
    >>> pi = 3.14159
    
    >>> area = pi * radius**2
    
    >>> area
    78.53975

##Strings in Python##
Strings are a group of characters.  A character could be a number, letter, or symbol like an operator or punctuation. Strings can also be made up of characters from other languages.

Strings are identifed either by ' ' single quotes or " " double quotes.

    >>> "what do you call someone with no nose and no body"
    'What do you call someone with no nose and no body?'
    
    >>> 'nobody knows'
    'nobody knows'

Strings may be stuck together to make bigger strings. This is called concatenation. Concatentation uses the + plus operator.

    >>> 'Big' + ' ' + 'Ben'
    'Big Ben'

Having the option of a single or double quote let's you easily add single or double quotes to your string. 

    >>> "Joe's car"
    "Joe's car"
    
    >>> 'John said, "Get off your horse and drink your milk!"'
    'John said, "Get off your horse and drink your milk!"'

Variables can also hold strings.

    >>> first_name = 'Steve'
    
    >>> last_name = 'Martin'
    
    >>> full_name = first_name + ' ' + last_name
    
    >>> full_name
    'Steve Martin'

You may use the multiply operator to create a long string from a small one.

    >>> short_name = "three "
    
    >>> short_string = "three "
    
    >>> long_string = short_string * 3
    
    >>> long_string
    'three three three '

You may use formatting to create a larger string.

    >>> "four : %d" % 4
    'four : 4'

You may pull individual letters from strings by adding [ ] square brackets to the end of the string and specifying the position of the character that you want to pull between the brackets. The first position is 0.

    >>> name = "Jack"
    
    >>> name[0]
    'J'
    
    >>> name[1]
    'a'
    
    >>> name[2]
    'c'
    
    >>> name[3]
    'k'

##Lists##
A list in Python is grouping or collection of objects, such as a colelction of strings. For example you could have a list that looks like this:

    pokemon = ["Bukbasaur", "Squirtle", "Charmander"]
    
You might also have a list of numbers, like this:

    ages = [10, 13, 20, 5]

You can pull individual items from a list using  [ ] square brackets, passing in the index of the value you would like returned. As with strings this index begins at 0.

    ages[0]
    10
    
    pokemon[2]
    'Charmander'
    
We'll study lists more when we look at loops in the next lesson.

##Booleans##
Think of a boolean as True or False, yes or no. Booleans can be identified using comparison operators.

    ==   !=   <   >   <=   >=

    >>> small = 3
    
    >>> small == 3
    True
    
    >>> small == 4
    False
    
    >>> large = 5
    
    >>> small == large
    False
    
    >>> small > large
    False
    
    >>> small < large
    True
    
    >>> small <= large
    True
    
    >>> small >= large
    False
    
    >>> small != large
    True

You may assign a boolean value like True or False to a variable.

    >>> b = True
    
    >>> b == True
    True
    
    >>> b == False
    False

There are some special boolean operations in python.

    >>> 'J' in 'Jack'
    True
    
    >>> 'J' not in 'Jack'
    False
    
    >>> 'k' not in 'Jack'
    False
    
The and operator will return true if the comparisons on both sides are True. The or operator will return true if one of the two comparisons surrounding it is True.

    >>> x = 3
    >>> y = 4
    
    >>> x == 3 and y == 5
    False
    
    >>> x == 3 or y == 5
    True

##Print and input##
Use print to write strings to the screen. You may print messages and string variables. You may also print other data, like numbers and booleans, if you convert those to strings before printing.

To print, surround the text you would like to print with ( ) parentheses.

    >>> print("hello")
    hello

    >>> print("hello " + "John")
    hello John

Numbers may be printed by themselves.

    >>> print(4)
    4

Strings and numbers cannot be added together.

    >>> print("num: " + 4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Can't convert 'int' object to str implicitly

You may print strings and ints together using a , comma to separate the values.  

    >>> print("num: ", 4)
    num: 4

It's more common to format a string that you plan to print. 

    >>> print("num: %d" % 4)
    num: 4

You may ask for a value and assign it to a variable using the input function.

    >>> name = input('What is your name? ')
    What is your name? John
    
    >>> print("Hello %s" % name)
    Hello John

The input function returns a string. If you would like to use the string returned as a number pass it to the int() function.

    >>> age = input("How old are you? ")
    How old are you? 8
    
    >>> age
    '8'
    
    >>> age * 3
    '888'
    
    >>> int(age) * 3
    24

##What we learned##

    >>> name = input("What is your name? ")
    What is your name? John
    
    >>> age = input("How old are you "+name+"? ")
    How old are you John? 12
    
    >>> print("Hello, ", name, ". You are ", age, " years old.")
    Hello,  John . You are  12  years old.
    
    >>> print(age," * ", 10, " = ", (int(age) * 10))
    12  *  10  =  120
    
    >>> print("The first character of your name is ",name[0])
    The first character of your name is  J
    
    >>> print("Is your age == 11,", int(age) == 11)
    Is your age == 11, False

    >>> days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday]
    >>> days_of_the_week[3]
    'Wednesday'
    
    >>> numbers = [1, 3, 5, 7, 11]
    >>> 4 * numbers[1]
    12
