# Python Flask authentication
UserMixin, Configuration, url_for, Hash Password, Protected page

<br />
<br />

**General install + imports to work with authentication**
```diff
+ install flask-login

+ from flask_login import (LoginManager, UserMixin, login_user, logout_user, login_required, current_user)
+ from werkzeug.security import generate_password_hash, check_password_hash
```
**UserMixin**
```python
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(200))
```
**Configuration**
```python
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```
<b>* login_manager = LoginManager()</b> <br />

create an instance of LoginManager <br />
this object handles user session management (logging in, logging out, remembering users, etc.) in your Flask app <br />

<b>* login_manager.init_app(app)</b> <br />

connect the LoginManager to your Flask app. <br />
app is your Flask application instance. <br />
without this, LoginManager won’t know about your app <br />

<b>* login_manager.login_view = "login"</b> <br />
```diff
- "login" does not refer to the URL /login, it refers to the name of the view function -
```
```python
decorator URL change

@app.route("/login")
def login():
    ...

to this

@app.route("/sign-in")
def login():
    ...

Flask-Login will automatically get the new URL /sign-in
If you had written the string "/login" manually, you would need to update it everywhere if the route changes
```
<b>* @login_manager.user_loader</b> <br />
```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```
@login_manager.user_loader tells Flask-Login how to get a user object given its ID. <br />
flask-Login uses this function internally whenever current_user is accessed <br />
user_id is stored in the session (as a string), so we convert it to int <br />
it cannot be called id, because id is already the column in the User class <br />

<br />

**redirect(url_for("login")) vs redirect("/login")**
```python
decorator URL change

@app.route("/login")
def login():
    ...

to this

@app.route("/sign-in")
def login():
    ...

Then redirect(url_for("login")) still works (Flask-Login will use the new URL)
But if you wrote redirect("/login") you would have to manually change every /login to /sign-in
```
**Hash password** - in register endpoint
```python
generate_password_hash(password)
```
**Check hashed password** - in login endpoint
```python
check_password_hash(user.password, password)
```
**Start session**
```python
login_user(user)
```
creates a session for the user, meaning Flask-Login stores their user_id in a cookie <br />

you can automatically log the user in after registration <br />
```python
in register endpoint

user = User(username=username, password=hashed_pw)
db.session.add(user)
db.session.commit()
login_user(user)  # automatically log in after registration

Then the user does not need to go to the login page separately
```
**Protected page**
```python
@login_required
```
protect a route from unauthorized access <br />
when you decorate a view function with @login_required, only logged-in users can access that route <br />
if a user who is not logged in tries to visit it, Flask-Login automatically redirects them to the login page <br />
login_manager.login_view = "login" - this line is responsible for the redirect <br />

**Logout User**
```python
logout_user()
```
removes the user’s ID from the session <br />
<br />
**Current_user**
```python
current_user from import
```
```jinja2
{% if current_user.is_authenticated %}
    <h1>Welcome, {{ current_user.username }}!</h1>
    <a href="/sekret">Go to secret page</a><br>
    <a href="/logout">Log out</a>
{% else %}
    <h1>You are not logged in</h1>
    <a href="/login">Log in</a> |
    <a href="/register">Register</a>
{% endif %}
```
even if we don’t explicitly use current_user in app.py, we still need to import it because it is used in index.html <br />
flask passes the context of current_user to the template, so the template can access it <br />
without importing it in app.py, the template won’t recognize current_user, even if app.py itself doesn’t reference it <br />
<br />

UserMixin provides standard implementations for user-related properties and methods: <br />
```python
current_user.

username (from my class)
password (from my class)

is_authenticated → True for a logged-in user (from UserMixin)
is_active → checks if the user account is active (from UserMixin)
is_anonymous → False for a logged-in user (from UserMixin)
get_id() → returns user.id (from UserMixin)
```



