from bottle import route, run, template, static_file, get, post, request


@get('/')
def get_index():
    return template('index')


@post('/multiply')
def post_index():
    # get values from request and store them in variables
    first_number = int(request.forms.get('first_number'))
    second_number = int(request.forms.get('second_number'))

    # calculate and store product in variable
    product = first_number * second_number

    # pass product to index, assign result to result parameter
    return template('index', result=product)


@route('/static/<filepath:path>')
def server_static(filepath):
    """
    Display our images, styles and scripts.
    """
    return static_file(filepath, root='./static')


run(host='localhost', port=8080, reloader=True)
