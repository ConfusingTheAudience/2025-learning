from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

# we need to import render_template
# we need to do templates directory to store our templates
# and we can specify template_folder for flask

# --------------------------------------------------------------------
# RENDER TEMPLATE
# --------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# PASS VALUES TO HTML - JINJA TEMPLATE ENGINE
# --------------------------------------------------------------------

# left side value name is the one used in html
# with_values.html
@app.route('/with_values')
def with_values():
    my_value = 'Something'
    my_result = 10 + 20
    my_list = [10, 20, 30, 40, 50]
    return render_template('with_values.html', myvalue = my_value, myresult = my_result, mylist = my_list)
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# TEMPLATE INHERITANCE
# base.html is the base structure used in other html files such as with_values.html and filters.html
# --------------------------------------------------------------------



# --------------------------------------------------------------------
# FILTERS (| in html)
# filters.html
# --------------------------------------------------------------------

@app.route('/filters')
def filters():
    some_text = 'Some text'
    return render_template('filters.html', some_text = some_text)

# custom filter
@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
    return s*times

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# DYNAMIC URL (a href in html)
# index.html
# --------------------------------------------------------------------

# @app.route('/whateverurlhere')
# def filters():
#     some_text = 'Some text'
#     return render_template('filters.html', some_text = some_text)
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# REDIRECT
# --------------------------------------------------------------------

# we need to import redirect and url_for
@app.route('/redirect_endpoint')
def redirect_endpoint():
    # return redirect('/filters')
    # or
    return redirect(url_for('filters'))
# --------------------------------------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
