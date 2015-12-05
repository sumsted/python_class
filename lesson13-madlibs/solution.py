# import the madlibs module
from madlibs import get_template, post_madlib

# get a madlib template object 0 to 3 and store it in a variable
template_id = input('Which template (0-3)? ')
madlib = get_template(int(template_id))

# iterate over the content, replacing tags with values
words = madlib['content'].split(' ')
new_content = ''
for word in words:
    if word[0] == '[':
        new_word = input(word+'? ')
        new_content += new_word + ' '
    else:
        new_content += word + ' '
madlib['content'] = new_content

# update the author value
madlib['author'] = 'me'

# send the madlib template object to the server
print(str(post_madlib(madlib)))