'''
The following code shows you how to accept input from a user, do something with that input and print out a response.
'''
name = input("What is your name? ")
age = input("How old are you "+name+"? ")
print("Hello, ", name, ". You are ", age, " years old.")
print(age," * ", 10, " = ", (int(age) * 10))
print("The first character of your name is ",name[0])
print("Is your age == 11,", int(age) == 11)
    