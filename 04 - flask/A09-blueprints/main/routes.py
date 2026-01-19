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
