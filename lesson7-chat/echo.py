import requests

ECHO_URL = 'https://fast-oasis-5535.herokuapp.com'


def add_message(name, message):
    url = ECHO_URL + '/message'
    data = {'name': name, 'message': message}
    result = requests.post(url, json=data)
    messages = result.json()['messages']
    return messages


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
