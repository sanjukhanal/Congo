from flask import Blueprint, jsonify, session, render_template
from flask_login import login_required, current_user

from .models import Checkout
from ..cart.models import Cart

blueprint = Blueprint("checkout", __name__, url_prefix="/checkout", static_folder="../static")


@blueprint.route("/add_book/<int:book_id>", methods=['POST'])
@login_required
def add_book(book_id):
    """List members."""
    cart_id = session.get("cart_id")
    if cart_id is None:
        cart = Cart.create(
            user_id=current_user.id
        )
        session["cart_id"] = cart.id
    else:
        cart = Cart.get_by_id(cart_id)

    checkout = Checkout.create(
        cart_id=cart.id,
        book_id=book_id,
    )

    return jsonify({"data": {
        "cart_id": cart.id,
        "book_id": book_id,
        "id": checkout.id
    }})


@blueprint.route("/", methods=['GET', 'POST'])
def home():
    cart_id = session.get("cart_id")
    if cart_id:
        cart = Cart.get_by_id(cart_id)
        checkouts = cart.checkouts
        return render_template("users/checkout.html", checkouts=checkouts)

