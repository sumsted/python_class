from bottle import route, run, template, static_file, get, post, request
from echo import add_message, get_messages, clear_messages



@get('/')
def get_chat():
    """ get_chat() runs when you load the page """
    messages = get_messages()
    return template('chat',name='', messages=messages)




@post('/message')
def post_message():
    """ post_message() will run when you press the chat button """
    name = request.forms.get('name')
    message = request.forms.get('message')

    messages = add_message(name, message)
    return template('chat', name=name, messages=messages)




@get('/clear')
def get_chat():
    messages = clear_messages()
    return template('chat',name='', messages=messages)




@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


run(host='localhost', port=8080, debug=True, reloader=True)
