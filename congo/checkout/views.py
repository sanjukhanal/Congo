from flask import Blueprint, jsonify, session, render_template, redirect, url_for
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


@blueprint.route("/remove_book/<int:checkout_id>", methods=['GET', 'POST'])
@login_required
def remove_book(checkout_id):
    cart_id = session.get("cart_id")
    if cart_id is not None:
        cart = Cart.create(
            user_id=current_user.id
        )
        checkout = Checkout.get_by_id(checkout_id)
        checkout.delete()
        return redirect(url_for('checkout.home'))


@blueprint.route("/", methods=['GET', 'POST'])
def home():
    cart_id = session.get("cart_id")
    if cart_id:
        cart = Cart.get_by_id(cart_id)
        checkouts = cart.checkouts
        total = sum([item.book.price for item in checkouts])
        return render_template("checkout/home.html", checkouts=checkouts, total=total)
    return redirect(url_for('user.home'))


@blueprint.route("/submit", methods=['GET'])
@login_required
def submit():
    cart_id = session.get("cart_id")
    if cart_id:
        cart = Cart.get_by_id(cart_id)
        cart.update({"is_submitted": True})
        checkouts = cart.checkouts
        total = sum([item.book.price for item in checkouts])
        session.pop("cart_id")
        return render_template("checkout/thank_you.html", checkouts=checkouts, total=total)
    return redirect(url_for('user.home'))
