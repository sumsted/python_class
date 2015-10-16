from bottle import route, run, template, static_file, get, post, request

# http://bottlepy.org/docs/dev/tutorial.html



@get('/')
def get_index():
    return template('index',result='')




@post('/calculate')
def calculate():
    # get values from request and store them in variables
    first_number = int(request.forms.get('first-number'))
    second_number = int(request.forms.get('second-number'))
    third_number = int(request.forms.get('third-number'))

    # calculate and store product in variable
    product = first_number + second_number +third_number

    # format result

    result = 'scott says %d + %d + %d = %d' % (first_number, second_number, third_number, product)

    # display form with result
    return template('index', result=result)




@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


run(host='localhost', port=8080)#, reloader=True)
