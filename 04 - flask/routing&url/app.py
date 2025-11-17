from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello</h1>'

# another basic route
@app.route('/hello')
def hello():
    return f'Hello World'


# --------------------------------------------------------------------
# URL PROCESSOR
# --------------------------------------------------------------------

# /greet/Sophie -> Hello Sophie
@app.route('/greet/<name>')
def greet_message(name):
    return f'Hello {name}'

# without typecast
# /adding/10/20 -> 1020
@app.route('/adding/<number1>/<number2>')
def adding(number1, number2):
    return f'{number1} + {number2} = {number1 + number2}'

# with typecast
# add/10/20 -> 30
@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    # this or the one above in url path <int:n>
    # number1 = int(number1)
    # number2 = int(number2)
    return f'{number1} + {number2} = {number1 + number2}'
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# HANDLE PARAMS
# --------------------------------------------------------------------

# we need to import request
@app.route('/handle_url_params')
def handle_params():
    # return dictionary
    # return str(request.args)

    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting} {name}'
    else:
        return 'Some parameters are missing'
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# REQUEST METHODS
# --------------------------------------------------------------------

# Every route you create is a GET route by default unless you explicitly specify other HTTP methods
@app.route('/post_method', methods=['POST'])
def post_method():
    return 'We can do only post method!'

@app.route('/get_and_post_method', methods=['GET', 'POST'])
def get_and_post_method():
    if request.method == 'GET':
        return 'This is GET request done'
    elif request.method == 'POST':
        return 'This is POST request done'
    else:
        return 'You will never see this message'
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# SPECIFY STATUS CODE
# --------------------------------------------------------------------

# specify status code
@app.route('/simple')
def simple():
    return f'Simple request with status code', 201

# custom response
# we need to import make_response
# we can change headers if we want
@app.route('/custom_response')
def custom_response():
    response = make_response('Hello world')
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
