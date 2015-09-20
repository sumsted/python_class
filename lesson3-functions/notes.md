#Lesson 3 - Functions#

- What are functions?
- Define a function
- Use parameters
- Return results


##What are functions?##
Functions are sections of code that we can reuse throughout our program. Functions usually are defined to do one thing really well. One function that you've used in the previous lessons is the print() function. Print does one thing really well, it pushes data to the screen. Another function we've used previously is range(). This function generates numbers for us that we can loop through.

Range() and print() are examples of system functions. System functions are functions that are available to you in Python. Functions that you create are called user defined functions. You might create a function to calculate the sum of two numbers or to create a greeting. These are special custom functions that you create.

##Define a function##
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
    >>> 

##Use parameters##
Parameters are values that you pass into a function from outside a function. You've done this previously with the print() and range() functions. To add parameters to your user defined function add variable names within the parantheses that come after the function name. These variables will be available within the code block of your function.

    >>> def hello(name):
    ...     print('Hello',name)
    ... 
    >>> hello('John')
    Hello John
    
    >>> def to_third_power(num):
    ...     print(num**3)
    ... 
    >>> to_third_power(2)
    8
    
You may define functions with multiple parameters.
    
    >>> def power(num, pow):
    ...     print(num**pow)
    ... 
    >>> power(2, 3)
    8

##Return results##
Functions may return results. These results can be displayed on the screen or used in other calculations.

    >>> def power(num, pow):
    ...     return num**pow
    ... 
    >>> power(2, 3)
    8
    >>> 4 + power(2,3)
    12
    >>> print('power 2**3 =', power(2, 3))
    power 2**3 = 8
    
In Python functions may return multiple values. 
    
    >>> def hello(name, age):
    ...     greeting = 'Hello' + name
    ...     in_ten_years = age + 10
    ...     return greeting, in_ten_years
    >>> g,t = hello('John', 10)
    >>> print(g, t)
    Hello John 20

##What we learned##
    '''
    Show a greeting.
    '''

    def say_hello(name, age):
        print('Hello', name)
        print('Hi', name, ', you are', age,'years old')
        return age * 2

    name = input('What is your name? ')
    age = input('How old are you? ')

    print(say_hello(name, age))
