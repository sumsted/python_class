import threading

import requests
import time

ECHO_URL = 'https://fast-oasis-5535.herokuapp.com'


def add_message(name, message):
    url = ECHO_URL + '/message'
    data = {'name': name, 'message': message, 'timestamp': time.time()}
    result = requests.post(url, json=data)
    messages = result.json()['messages']
    return messages


last_time = 0
alive = True


def poll_messages():
    global last_time
    if alive == False:
        return
    messages = get_messages()
    found = False
    for i, m in enumerate(messages):
        if m['timestamp'] > last_time:
            print('>>>', m['name'], ':', m['message'])
            found = True
        if i == (len(messages) - 1) and found:
            print('?')
    last_time = time.time()
    threading.Timer(3, poll_messages).start()


def stop_poll():
    global alive
    alive = False


def get_messages():
    url = ECHO_URL + '/messages'
    result = requests.get(url)
    messages = result.json()['messages']
    return messages


def clear_messages():
    url = ECHO_URL + '/clear'
    result = requests.get(url)
    messages = result.json()['messages']
    return messages


if __name__ == '__main__':
    print('add_messages()')

    name = 'zedd+sg'
    message = 'want you to know'
    messages = add_message(name, message)
    for m in messages:
        print(m['name'], m['message'])

    print('get_messages()')
    messages = get_messages()
    for m in messages:
        print(m['name'], m['message'])
