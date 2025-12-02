from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager, UserMixin,
    login_user, logout_user,
    login_required, current_user
)
from werkzeug.security import generate_password_hash, check_password_hash

# =================================================================
# 1. Application configuration
# =================================================================
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sekretnyklucz'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

# =================================================================
# 2. User model
# =================================================================
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(200))

# =================================================================
# 3. Flask-Login configuration
# =================================================================
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# =================================================================
# 4. Routes / Views
# =================================================================

@app.route("/")
def index():
    return render_template("index.html")

# ----------- Registration -------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed_pw = generate_password_hash(password)

        user = User(username=username, password=hashed_pw)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")

# ----------- Login --------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("index"))

        return "Invalid login credentials!"

    return render_template("login.html")

# ----------- Protected page -----------------
@app.route("/sekret")
@login_required
def sekret():
    return render_template("sekret.html")

# ----------- Logout -------------------------
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

# =================================================================
# 5. Application start
# =================================================================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
