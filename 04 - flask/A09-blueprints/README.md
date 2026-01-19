# Python Flask blueprints
Blueprints in Flask are modular components of an application that let you group routes, templates, and static files together

<br />
<br />

**Folder structure**
```python
project/app.py - main file to start the project
project/extensions.py - inicjalization SQLAlchemy and LoginManager
project/models.py - definition of model User
project/main and project/auth (folders) - blueprints of main and auth
```

**app.py**
```diff
+ from extensions import db, login_manager
+ from models import User
```
```python
from flask import Flask
from extensions import db, login_manager
from models import User

from main import main_bp
from auth import auth_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = "sekretnyklucz"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**extensions.py**
```python
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
```

**models.py**
```diff
+ from extensions import db
```
```python
from flask_login import UserMixin
from extensions import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(200))
```

**auth/__init__.py and main/__init__.py**
```diff
+ from flask import Blueprint
+ from . import routes
```
```python
from flask import Blueprint

auth_bp = Blueprint("auth", __name__)

from . import routes

---------------- and ----------------

from flask import Blueprint

main_bp = Blueprint("main", __name__)

from . import routes
```

**auth/routes.py**
```diff
+ from . import auth_bp
+ from models import User
+ from extensions import db
```
```python
from flask import request, redirect, url_for, render_template
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import auth_bp
from models import User
from extensions import db

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User(
            username=username,
            password=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("main.index"))

        return "Invalid login credentials!"

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))
```

**main/routes.py**
```diff
+ from . import main_bp
```
```python
from flask import render_template
from flask_login import login_required
from . import main_bp

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/sekret")
@login_required
def sekret():
    return render_template("sekret.html")
```


