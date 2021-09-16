from flask import Blueprint, render_template

bp = Blueprint("public", __name__, static_folder="../static")


@bp.route("/ping", methods=["GET", "POST"])
def ping():
    """Home page."""
    return "PONG"


@bp.route("/login", methods=["GET", "POST"])
def login():
    """Home page."""
    return render_template("login.html")


@bp.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    return render_template("home.html")