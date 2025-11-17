# Python Flask routing & url
 
**Basic route**
```python
@app.route('/hello')
def hello():
    return f'Hello World'
```
**URL processor**
```python
@app.route('/greet/<name>')
def greet_message(name):
    return f'Hello {name}'
```
```python
@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1} + {number2} = {number1 + number2}'
```
**Handle params**
```python
@app.route('/handle_url_params')
def handle_params():

    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting} {name}'
    else:
        return 'Some parameters are missing'
```
**Request methods**
```prisma
@app.route('/post_method', methods=['POST'])
def post_method():
    return 'We can do only post method!'
```
```python
@app.route('/get_and_post_method', methods=['GET', 'POST'])
def get_and_post_method():
    if request.method == 'GET':
        return 'This is GET request done'
    elif request.method == 'POST':
        return 'This is POST request done'
    else:
        return 'You will never see this message'
```
**Specify status code**
```python
@app.route('/simple')
def simple():
    return f'Simple request with status code', 201
```
```python
@app.route('/custom_response')
def custom_response():
    response = make_response('Hello world')
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response
```

