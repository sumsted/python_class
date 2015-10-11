# import the animals.py module

import animals

# ask the user for their favorite animal and store it in a variable called favorite

favorite = input('What is your favorite animal? ')

# using an if statement check to see if favorite is in the animals_dict

if favorite in animals.animals_dict:

    # if favorite is found print favorite and the value or definition of it

    print(favorite, animals.animals_dict[favorite])

else:

    # if favorite is not found print 'sorry, we can't find favorite'

    print('sorry, we can\'t find favorite')