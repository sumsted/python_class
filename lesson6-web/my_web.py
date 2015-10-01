from bottle import route, run, template, static_file, get, post, request


@get('/')
def get_index():
    return template('index',result='')




@post('/multiply')
def post_index():
    # get values from request and store them in variables
    first_number = int(request.forms.get('first-number'))
    second_number = int(request.forms.get('second-number'))

    # calculate and store product in variable
    product = first_number * second_number

    # format result
    result = '%d x %d = %d' % (first_number, second_number, product)

    # display form with result
    return template('index', result=result)




@route('/static/<filepath:path>')
def server_static(filepath):
    """
    Display our images, styles and scripts.
    """
    return static_file(filepath, root='./static')


run(host='localhost', port=8080)#, reloader=True)
