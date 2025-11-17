# Python Flask templates & html
pass value, template inheritance, filters, dynamic url, redirect

<br />
<br />
 
**Basic template and definition**
```python
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')
```
```diff
+ /templates/index.html
```
**Pass values into html - JINJA TEMPLATE ENGINE**
```python
@app.route('/with_values')
def with_values():
    my_value = 'Something'
    my_result = 10 + 20
    my_list = [10, 20, 30, 40, 50]
    return render_template('with_values.html', myvalue = my_value, myresult = my_result, mylist = my_list)
```
```jinja
with_values.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>With values</title>
</head>
<body>
    <h1>Hi</h1>
    <ul>
        {% for item in mylist %}
            {% if item == 30 %}
                <li style='color: red'>{{ item }}</li>
            {% else %}
                <li>{{ item }}</li>
            {% endif %}
        {% endfor %}
    </ul>
    <p>{{ myvalue }}</p>
    <p>{{ myresult }}</p>
</body>
</html>

```
**Template Inheritance**
```jinja
base.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Default title{% endblock %}</title>
</head>
<body>
    <p>This will always be here</p>
    {% block content %}{% endblock %}
</body>
</html>
```    
```jinja
with_values.html

{% extends 'base.html' %}
{% block title %}With values{% endblock %}

{% block content %}
    <h1>Hi</h1>
    <ul>
        {% for item in mylist %}
            {% if item == 30 %}
                <li style='color: red'>{{ item }}</li>
            {% else %}
                <li>{{ item }}</li>
            {% endif %}
        {% endfor %}
    </ul>
    <p>{{ myvalue }}</p>
    <p>{{ myresult }}</p>
{% endblock %}
```    
**Filters**
```python
@app.route('/filters')
def filters():
    some_text = 'Some text'
    return render_template('filters.html', some_text = some_text)
```
custom filters
```python
@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
    return s*times

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
```
```jinja
filters.html

{% extends 'base.html' %}
{% block title %}Filters{% endblock %}

{% block content %}
    <h1>Filters</h1>
    <p>{{ some_text| upper }}</p>
    <p>{{ some_text| lower }}</p>
    <p>{{ some_text| title }}</p>
    <p>{{ some_text| replace('e', 'E') }}</p>

    <p>{{ some_text| reverse_string }}</p>
    <p>{{ some_text| repeat }}</p>
    <p>{{ some_text| repeat(5) }}</p>
    <p>{{ some_text| alternate_case }}</p>
{% endblock %}

``` 
**Dynamic URL**
```python
@app.route('/whateverurlhere')
def filters():
    some_text = 'Some text'
    return render_template('filters.html', some_text = some_text)
```
```jinja
index.html

added this line:
<a href="{{ url_for('filters') }}">Filters</a>
```
**Redirect**
```python
@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('filters'))
```
