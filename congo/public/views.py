# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for, session,
)
from flask_login import login_required, logout_user, login_user

from congo.extensions import login_manager
from congo.public.forms import LoginForm
from congo.user.forms import RegisterForm
from congo.user.models import User
from congo.utils import flash_errors

blueprint = Blueprint("public", __name__, static_folder="../static")


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/", methods=["GET", "POST"])
@blueprint.route("/login", methods=["GET", "POST"])
def login():
    """Login Page"""
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.form)
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", "success")
            session["user_id"] = form.user.get_id()
            if form.user.is_admin:
                redirect_url = request.args.get("next") or url_for("admin.home")
            else:
                redirect_url = request.args.get("next") or url_for("user.home")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    else:
        user_id = session.get("user_id")
        user = User.get_by_id(user_id)
        if user:
            if user.is_admin:
                redirect_url = request.args.get("next") or url_for("admin.home")
            else:
                redirect_url = request.args.get("next") or url_for("user.home")
            return redirect(redirect_url)
    return render_template("login.html", form=form)


@blueprint.route("/logout/")
def logout():
    """Logout."""
    logout_user()
    session.clear()
    flash("You are logged out.", "info")
    return redirect(url_for("public.login"))


@blueprint.route("/register/", methods=["GET", "POST"])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            active=True,
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("public.login"))
    else:
        flash_errors(form)
    return render_template("public/register.html", form=form)


@blueprint.route("/about/")
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)
