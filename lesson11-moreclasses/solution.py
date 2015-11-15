
class Animal:

    def __init__(self, classification):
        # add a parameter called classification to __init__()
        # store the classification parameter in an instance variable
        self.classification = classification
        pass

    def __eq__(self, other):
        return self.classification == other.classification


# create a class called Fish it inherit Animal
# and it should take in a parameter called name in its __init__()
# create an instance variable called name to store the name parameter
class Fish(Animal):
    def __init__(self, name):
        super().__init__('Fish')
        self.name = name

    def __eq__(self, other):
        return Animal.__eq__(self, other)

# create a class called Bird it inherit Animal
# and it should take in a parameter called name in its __init__()
# create an instance variable called name to store the name parameter
class Bird(Animal):
    def __init__(self, name):
        super().__init__('Bird')
        self.name = name

    def __eq__(self, other):
        return Animal.__eq__(self, other)


# create an object called bass from Fish
# create an object called shark from Fish
# create an object called eagle from Bird
bass = Fish('Billy')
shark = Fish('Sammy')
eagle = Bird('Eddie')

# test to see if bass and shark are the same classification
print(bass == shark)

# test to see if bass and eagle are the same classification
print(eagle == bass)
