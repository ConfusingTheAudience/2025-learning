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
