# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, jsonify, session
from flask_login import login_required

from congo.book.models import Book
from congo.cart.models import Cart
from congo.extensions import login_manager
from congo.user.models import User

blueprint = Blueprint("user", __name__, url_prefix="/user", static_folder="../static")


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/")
@login_required
def home():
    """List members."""
    books = Book.query.all()
    cart_id = session.get("cart_id")
    checkouts = []
    if cart_id:
        cart = Cart.get_by_id(cart_id)
        checkouts = cart.checkouts
    return render_template("users/home.html", books=books, cart_id=cart_id, checkouts=checkouts)


@blueprint.route("/current_user", methods=["POST"])
@login_required
def current_logged_user():
    """List members."""
    user_id = session.get("user_id", None)
    if user_id:
        return jsonify({
            "data": {
                "id": user_id
            }
        })
    return jsonify({})
