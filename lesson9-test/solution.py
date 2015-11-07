


# function.py
def power(n, p):
    result = n**p
    return result

answer = power(2,3)
print(answer)


# groups.py
robots = {'r2d2': 'beep twirp beep', 'c3p0':'blah whine blah','bb8':'whirl whirl whirl'}
print(robots['r2d2'])
robots['wall-e'] = 'walleee ooohhh'
print(robots['wall-e'])

colors = ['red', 'green', 'blue']
colors.append('orange')
for color in colors:
    print(color)
    if color == 'blue':
        print('Go Tigers!')


# chat.py
import echo

name = input('What is your name? ')
message = 'Hello, this is ' + name

print('Enter message or "quit" to end')
echo.poll_messages()
while message != 'quit':
    echo.add_message(name, message)
    message = input('? ')

echo.add_message(name, 'has left chat')
echo.stop_poll()
