Numbers
Whole numbers are called integers or are of type int.
    1   2   3  4  5   13456

Numbers with a decimal component are called floating point numbers and are of type float.
    1.0 2.123 3.14

Operators are symbolds we use to perform arithmetic
+ add   - subtract    * multiply   / divide

// floor division, divide but throw away the decimal component
**  power

Order of operations
+- unary, say you have -10 + 4, the - in front of the 10 is calculated first
** power
() parentheses
* multiply
/ divide
// floor division
+ add
- subtract

Variables
Variables are labels or tags or names that you can assign to a number or to a math operation. They let you store a number or result to use later in your program.
    >>> some_number = 4
    >>> radius = 5
    >>> pi = 3.14159
    >>> area = pi * radius**2

Strings
Strings are a group of characters. A character could be a number, letter, or symbol like an operator or punctuation. Strings can also be made up of characters from other languages.
Strings are identifed either by ' ' single quotes or " " double quotes.
Variables can hold strings. Strings can be combined with the + oeprator.
    >>> first_name = 'Steve'
    >>> last_name = 'Martin'
    >>> full_name = first_name + ' ' + last_name

Lists
A list in Python is grouping or collection of objects, such as a colelction of strings. For example you could have a list that looks like this:
    pokemon = ["Bulbasaur", "Squirtle", "Charmander"]
You might also have a list of numbers, like this:
    ages = [10, 13, 20, 5]
Lists are identified with square brackets [ ].
Each item in a list is separated with a , comma.
Items may be added to an existing list using the append function.
    >>> ages.append(40)
    >>> ages
    [10, 13, 20, 5, 40]

Dictionary
Dictionaries are like Lists in that they are a collection of items.
A Python dictionary is data structure that lets the programmer map a key to a value.
Just like with a real dictionary, you define a set of terms. Each term has a single definition.
Terms or keys may be any data type, such as a string, int, or number. Definitions or values may be any type or object.
Dictionaries are identified with curly braces { }.
Items in a dictionary are separated with a , comma.
Keys are matched to values with a : colon.
    animals = {
        'cow': 'four legged bovine, vegan, sometimes spotted',
        'cat': 'four legged feline, omnivore, usually furry, meows alot',
        'bird': 'winged creature, noisy, tweets constantly'
    }
To find a value in a dictionary, use square braces and the dictionary name
to identify the key. the Value will be returned. If the key is not found then an error
occurs.
    >>> animals['cow']
    four legged bovine, vegan, sometimes spotted

    >>> animals['dog']
    Traceback (most recent call last):
      File "/Applications/PyCharm Edu.app/Contents/helpers/pydev/pydevd.py", line 2351, in <module>
        globals = debugger.run(setup['file'], None, None, is_module)
      File "/Applications/PyCharm Edu.app/Contents/helpers/pydev/pydevd.py", line 1771, in run
        pydev_imports.execfile(file, globals, locals)  # execute the script
      File "/Applications/PyCharm Edu.app/Contents/helpers/pydev/_pydev_imps/_pydev_execfile.py", line 18, in execfile
        exec(compile(contents+"\n", file, 'exec'), glob, loc)
      File "/Users/scottumsted/Library/Preferences/PyCharmEdu20/scratches/scratch_4", line 11, in <module>
        print(animals['dog'])
    KeyError: 'dog'
New key values may be added to a dictionary by assigning a key a value just like
it was a variable.
    >>> animals['bat'] = 'creepy flying rat thing'

Booleans and Comparisons
True or False
You can use comparisons to test if a condition is True or False.
Comparisons will return a boolean.
Comparisons use the following operators.
==   !=    <    >    <=    >=

You may also check to see if an item is in a list or dictionary using the in operator.

    >>> list_of_names = ['bob', 'jack']
    >>> 'bob' in list_of_names
    True

Comparisons can be combined using and or.
    >>> i = 3
    >>> 'bob' in list_of_names and i > 3
    False

Parentheses may be used to combine comparisons.
    >>> ('bob' in list_of_names and i > 3) or i == 3
    True

Print
The print function may be used to display variables, numbers or strings on the screen.
The easiest wat to print several items is to separate them with commas.
Print will place a space between each item in the print function.
    >>>print(i, 'bob', 5)
    3 bob 5
There are several ways to format (make pretty) strings and print output.
You may add items together like we did with strings. Just be sure if you
add items that they are all the same type, all numbers or all strings.
print('name '+'bob')
print(4+'bob')
You can also format the output.
    >>> name = 'jill'
    >>> age = 2
    >>> print('name: %s age: %d' % (name, age))
    name: jill age: 2
The %s will insert a string and %d will insert an integer.

Input
Think of the input function as the opposite of print.
Where as print puts output on the screen, input collects input
from the user. The input is stored in a variable as a string.
    >>> name = input('What is your name? ')
    >>> age = input('How old are you? ')
    >>> next_year = int(age) + 1
    >>> print('Hi %s, next year you will be %d years old!' %(name, age))
    What is your name? Nathan
    How old are you? 24
    Hi Nathan, next year you will be 24 years old!
Notice that we had to convert age to an integer before we could add
it to 1.

Comments

Docstrings allow you make multi-line comments. Docstrings are typically found near the top of Python files and at the top of functions and classes (we'll talk more about these later). Docstrings are used by Python to provide help output and usually describe what a python module, function or class does, what input is needed and what the results will be if the code is run.
Consider the following lines of code from the previous lesson, basics.py.
    '''
    The following code shows you how to accept input from a user, do something with that input and print out a response.
    '''
If you were to start Python and import this file, basics would run. And then if you type help(basics) you would see the docstring for this file.
    >>> import basics
    docstrings would print
Another type of comment is the line comment. Line comments are indicated using the # hashtag. There's one line comment in the previous python file. We typically use line comments to describe complex features or to remind us to come back and change code later.
    # We convert age to an int before we multiply it by 10.

Blocks
Python is an indented language. What this means is that sections of code that we run begin and end with an indentation. Python code blocks are typically indented with 4 spaces. Blocks of code can be found in functions, classes, if, while and for loops.
Consider this code.
    print("I'm out of a code block")
    if True:
        print("I'm in a block")
        number = 4
        print(number * 3)
    print("I'm out of a code block")
There is a code block after the if statement.

If Statment
Use the if statement and a comparison to decide what code blocks should run.
    if True:
        some_number = 2
        print('this code ran', some_number)
The code block beneath an if statement will execute if the comparison is True. Use the else statement if you would like to offer an alternative code block that executes when the coparison is False.
To check if some_number is above a certain value you could do something like this.
    some_number = 3
    if some_number > 4:
        print('some_number is greater than 4')

While Statement
If you need repeatedly run a code block use a loop. Like the if statement the while loop uses a comparison. If the comparison is True the code block will continue to run.
    some_number = 0
    while some_number < 100:
        some_number = some_number + 10
        print('some_number is less than 100', some_number)
    print('some_number is now', some_number)

For Statement
Another type of loop is the for loop. The for loop does not use a comparison like the while loop. The for loop is useful when you would like to use a counter in your code block. Also useful if you would like to pull individual values from a list or collection into your code block. This is called iteration.
You can use the range() function to count numbers.
    sum = 0
    for number in range(10):
        sum = sum + number
        print('number',number,'sum',sum)

Functions
Functions are sections of code that we can reuse throughout our program. Functions usually are defined to do one thing really well. One function that you've used in the previous lessons is the print() function. Print does one thing really well, it pushes data to the screen. Another function we've used previously is range(). This function generates numbers for us that we can loop through.
Range() and print() are examples of system functions. System functions are functions that are available to you in Python. Functions that you create are called user defined functions. You might create a function to calculate the sum of two numbers or to create a greeting. These are special custom functions that you create.
Similar to variables, all functions must have a name. The first line of a function is where we name the function. The def keyword is used to identify the name of a function. It comes before the name. Parentheses come after the name of the function. The code that makes up a function is in an indented block below this line. For example:
    def say_hello():
        print('Hello')

To run or call a function just type the name and the parantheses.
    >>> def hello():
    ...     name = input('Name? ')
    ...     print('Hello', name)
    ...
    >>> hello()
    Name? Jack
    Hello Jack
Parameters are values that you pass into a function from outside a function. You've done this previously with the print() and range() functions. To add parameters to your user defined function add variable names within the parantheses that come after the function name. These variables will be available within the code block of your function.
    >>> def hello(name):
    ...     print('Hello',name)
    ...
    >>> hello('John')
    Hello John
Functions may return results. These results can be displayed on the screen or used in other calculations.
    >>> def power(num, pow):
    ...     return num**pow
    ...
    >>> power(2, 3)
    8

Modules
A Python module is file that contains Python code. Modules help you group togather variables,
functions and classes that are related. For example you might have a module called animals that
contains a list of animals. This module might also contain functions that let you do animal related
things.

The import statement is used to add the code from one module to another.

You could have a module called animals.py that looks like this.

    animals_dict = {
        'cow': 'four legged bovine, vegan, sometimes spotted',
        'cat': 'four legged feline, omnivore, usually furry, meows alot',
        'bird': 'winged creature, noisy, tweets constantly'
    }

    def sorted_animals():
        return sorted(animals)

Then in my_code.py you could import specific objects from the animals.py module.

    from animals import animals_dict

    first = animals_dict['cat']
    print('cat -', first)

