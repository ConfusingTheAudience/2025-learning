# Python Flask session & cookies
session, cookies, message flashing

<br />
<br />
 
**SESSION - set, get and clear**
```python
@app.route('/set_data')
def set_data():
    session['name'] = 'Mike'
    session['other'] = 'Hello World'

    return render_template('index.html', message='Session data set')

@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
        return render_template('index.html', message=f'Name: {name}, Other: {other}')
    else:
        return render_template('index.html', message='No session found')
    
@app.route('/clear_session')
def clear_session():
    # or to clear all clear() below
    session.clear()
    return render_template('index.html', message='Session cleared')
```
```diff
+ from flask import session
```
```html
index.html

{% extends 'base.html' %}
{% block title %}Index Page{% endblock %}

{% block content %}
    <h1>Hello World</h1>
    <p>{{ message }}</p>

    <a href="{{ url_for('set_data') }}">Set Session Data</a><br>
    <a href="{{ url_for('get_data') }}">Get Session Data</a><br>
    <a href="{{ url_for('clear_session') }}">Clear session</a><br>
{% endblock %}
```

**COOKIES - set, get and clear**
```python
@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message='Cookie set'))
    response.set_cookie('cookie_name', 'cookie_value') # key, value keyword arguments
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index.html', message=f'Cookie value: {cookie_value}')

@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html', message='Cookie removed'))
    response.set_cookie('cookie_name', expires=0)
    return response
```
```diff
+ from flask import make_response
+ from flask import request
```
```html
index.html

{% extends 'base.html' %}
{% block title %}Index Page{% endblock %}

{% block content %}
    <h1>Hello World</h1>
    <p>{{ message }}</p>

    <a href="{{ url_for('set_cookie') }}">Set Cookie</a><br>
    <a href="{{ url_for('get_cookie') }}">Get Cookie</a><br>
    <a href="{{ url_for('remove_cookie') }}">Clear Cookie</a><br>
{% endblock %}
```

**Message flashing**
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'AB' and password == '123':
            flash('Successful login')
            return render_template('index.html', message='')
        else:
            flash('Login failed')
            return render_template('index.html', message='')
```
```diff
+ from flask import flash
```
```html
login.html

{% extends 'base.html' %}
{% block title %}Login Page{% endblock %}

{% block content %}
    <h1>Login</h1>
    <form action="{{ url_for('login') }}" method="POST">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Login">
    </form>
{% endblock %}
```
```html
index.html

{% extends 'base.html' %}
{% block title %}Index Page{% endblock %}

{% block content %}
    <h1>Hello World</h1>
    <p>{{ message }}</p>

    <a href="{{ url_for('login') }}">Login</a><br>
{% endblock %}
```
